# File: src/optiview/engine/walk_forward/predict.py

import pandas as pd
import numpy as np
from typing import Optional
from optiview.data.join_tools import (
    convert_to_prediction_dict,
    insert_predictions,
    get_training_features,
    extract_input_matrix,
    get_expert_name_for_run,
)
from optiview.engine.walk_forward.train_model import train_and_predict_profits


def predict_optimal_config(
    df: pd.DataFrame,
    symbol: str,
    predict_month: str,
    months_back: int = 3,
    target: str = "profit",
    override_model: Optional[str] = None,
) -> None:
    """
    Predicts the optimal EA input setting for a given symbol and month.

    Trains a machine learning model using past backtest results and predicts the
    best-performing configuration for the specified future month.

    Args:
        df (pd.DataFrame): Historical backtest results, including input parameters and profit metrics.
        symbol (str): Trading symbol to predict (e.g., "EURUSD").
        predict_month (str): Target month to predict for, in format "YYYY-MM".
        months_back (int, optional): Number of past months to use for training. Defaults to 3.
        target (str, optional): Column name for realized profit to train on. Defaults to "profit".
        override_model (Optional[str], optional): Model name to override default. Defaults to None.

    Raises:
        ValueError: If training data or candidate configurations are insufficient.

    Returns:
        None
    """

    if df.empty:
        raise ValueError(f"No training data available for {symbol}")

    df = df.copy()
    df["run_month"] = df["run_month"].astype(str)

    available_months = sorted(
        m for m in df["run_month"].dropna().unique() if m < predict_month
    )

    if not available_months:
        raise ValueError(
            f"No available backtest months for {symbol} before {predict_month}."
        )

    if len(available_months) >= months_back:
        train_months = available_months[-months_back:]
    else:
        train_months = available_months

    train_df = df[df["run_month"].isin(train_months)].copy()

    if train_df.empty:
        raise ValueError(f"No training data for {symbol} in the selected months.")

    # Inject dummy model if missing
    model_name = override_model if override_model else "xgb"
    train_df["model"] = model_name

    # Expand params_json into actual columns
    input_keys = get_training_features(train_df)
    X_inputs = extract_input_matrix(train_df, input_keys)
    train_df = pd.concat(
        [train_df.reset_index(drop=True), X_inputs.reset_index(drop=True)], axis=1
    )

    # Prepare training features and labels
    X_train = train_df[input_keys]
    y_train = train_df[target]

    # Prepare test set: all configs for latest available month
    latest_train_month = max(train_months)
    test_df = df[df["run_month"] == latest_train_month].copy()

    if test_df.empty:
        raise ValueError(
            f"No candidate configs available for prediction in {latest_train_month}."
        )

    X_test_inputs = extract_input_matrix(test_df, input_keys)

    # Predict profits for configs
    predicted_profits = train_and_predict_profits(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test_inputs,
        model_name=model_name,
    )

    # Attach predictions back to test DataFrame
    test_df = test_df.reset_index(drop=True)
    test_df["predicted_profit"] = predicted_profits.values

    # Select the best predicted config
    top_row = test_df.sort_values("predicted_profit", ascending=False).iloc[0]

    # Prepare and insert prediction
    month_str = predict_month

    run_id_value = top_row.get("run_id")
    run_id_int = (
        int(run_id_value)
        if run_id_value is not None and not pd.isna(run_id_value)
        else None
    )

    expert_name = (
        get_expert_name_for_run(run_id_int) if run_id_int is not None else None
    )

    pred = convert_to_prediction_dict(
        row=top_row,
        symbol=symbol,
        model_name=model_name,
        month=month_str,
        expert_name=expert_name,
        confidence_score=None,  # To be filled after annotation
        confidence_stars=None,  # To be filled after annotation
        predicted_profit=float(top_row["predicted_profit"]),
    )

    insert_predictions([pred])

    print(
        f"✅ Saved prediction for {symbol} ({model_name}) into database for {month_str}."
    )
