# File: src/optiview/engine/walk_forward/predict.py

"""Predict the optimal configuration for trading strategies."""

from __future__ import annotations

from typing import Any, Optional, Hashable

import json
import numpy as np
import pandas as pd

from optiview.database.models import PredictedSetting
from optiview.database.session import get_optiview_session
from optiview.engine.walk_forward.scoring_helpers import (
    confidence_score_to_stars,
    estimate_confidence_score,
)
from optiview.engine.walk_forward.train_model import train_model


def prepare_training_data(
    df: pd.DataFrame, predict_month: str, months_back: int
) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    """
    Prepare training and testing data for walk-forward prediction.

    Args:
        df: A DataFrame containing historical run data.
        predict_month: The month for which to generate predictions (format: 'YYYY-MM').
        months_back: The number of prior months to use for training.

    Returns:
        A tuple containing:
        - train_df: DataFrame containing training rows.
        - test_df: Empty DataFrame (reserved for consistency).
        - latest_train_month: The latest month used for training.

    Raises:
        ValueError: If no data is available or insufficient months are present.
    """
    all_months = sorted(df["run_month"].unique())
    if not all_months:
        raise ValueError("No available months in provided data.")

    predict_idx = len(all_months)
    if predict_month in all_months:
        predict_idx = all_months.index(predict_month)

    if predict_idx < months_back:
        raise ValueError(f"Not enough historical months to train for {predict_month}.")

    train_months = all_months[max(0, predict_idx - months_back) : predict_idx]
    train_df = df[df["run_month"].isin(train_months)].copy()
    test_df = pd.DataFrame()
    latest_train_month = train_months[-1] if train_months else all_months[-1]

    return train_df, test_df, latest_train_month


def train_model_wrapper(
    X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, model_name: str
):
    """
    Wrapper for model training.

    Args:
        X_train: Feature matrix for training.
        y_train: Target vector for training.
        X_test: Feature matrix for prediction.
        model_name: The name of the model to use.

    Returns:
        The trained model and its predictions.
    """
    return train_model(
        X_train=X_train, y_train=y_train, X_test=X_test, model_name=model_name
    )


def select_best_prediction(df: pd.DataFrame) -> pd.Series:
    """
    Select the best predicted configuration based on maximum predicted profit.

    Args:
        df: A DataFrame containing prediction results.

    Returns:
        The row with the highest predicted profit.

    Raises:
        ValueError: If the DataFrame is empty.
        TypeError: If the selected row is not a Series.
    """
    if df.empty:
        raise ValueError("Cannot select from an empty DataFrame.")

    best_idx = df["predicted_profit"].idxmax()
    best_row = df.loc[best_idx]

    if isinstance(best_row, pd.DataFrame):
        best_row = best_row.squeeze(axis=0)
    if not isinstance(best_row, pd.Series):
        raise TypeError("Expected best_row to be a Series after squeeze.")

    return best_row


def safe_convert(value: Any) -> Any:
    """
    Convert a NumPy value into a standard Python type.

    Args:
        value: A NumPy scalar or native Python type.

    Returns:
        The equivalent Python-native type.
    """
    if isinstance(value, np.generic):
        return value.item()
    return value


def create_prediction_entry(
    top_row: pd.Series,
    symbol: str,
    model_name: str,
    month_str: str,
    rank: int,
    confidence_score: Optional[float] = None,
    confidence_stars: Optional[str] = None,
) -> dict[str, Any]:
    """
    Create a database-safe prediction dictionary from the top candidate row.

    Args:
        top_row: The top row with prediction results.
        symbol: The trading symbol.
        model_name: The model used.
        month_str: The month being predicted.
        rank: The rank of this prediction (usually 1).
        confidence_score: Optional float for model confidence.
        confidence_stars: Optional string of star representation.

    Returns:
        A dictionary ready for database insertion.
    """
    params: dict[str, Any] = {
        str(k): safe_convert(v)
        for k, v in top_row.items()
        if k not in {"run_id", "symbol", "run_month", "profit", "predicted_profit"}
    }

    return {
        "version": "v1",
        "month": month_str,
        "symbol": symbol,
        "model": model_name,
        "predicted_profit": safe_convert(top_row.get("predicted_profit")),
        "confidence_score": safe_convert(confidence_score),
        "confidence_stars": confidence_stars,
        "rank": rank,
        "inputs": safe_jsonify_dict(params),
        "params_json": safe_jsonify_dict(
            {str(k): v for k, v in top_row.to_dict().items()}
        ),
        "run_id": safe_convert(top_row.get("id")),
        "job_id": top_row.get("job_id"),
        "tags": [],
        "notes": None,
    }


def insert_predictions(predictions: list[dict[str, Any]]) -> None:
    """Insert or update prediction entries into the database."""
    session = get_optiview_session()

    for pred in predictions:
        existing = (
            session.query(PredictedSetting)
            .filter_by(
                month=pred["month"],
                symbol=pred["symbol"],
                model=pred["model"],
                rank=pred["rank"],
            )
            .first()
        )
        if existing:
            existing.version = pred["version"]
            existing.predicted_profit = pred["predicted_profit"]
            existing.confidence_score = pred["confidence_score"]
            existing.confidence_stars = pred["confidence_stars"]
            existing.inputs = pred["inputs"]
            existing.params_json = pred["params_json"]
            existing.tags = pred.get("tags", [])
            existing.notes = pred.get("notes", None)
            existing.job_id = pred["job_id"]
            existing.run_id = pred["run_id"]
        else:
            session.add(PredictedSetting(**pred))

    session.commit()


def predict_optimal_config(
    df: pd.DataFrame,
    symbol: str,
    predict_month: str,
    months_back: int = 3,
    override_model: Optional[str] = None,
    target: str = "profit",
) -> None:
    """
    Predict the optimal configuration for a given symbol and month.

    Args:
        df: DataFrame containing past runs.
        symbol: Trading symbol to predict.
        predict_month: Month string for prediction.
        months_back: Number of months to train on.
        override_model: Optional ML model to override default.
        target: Performance metric to optimize.

    Raises:
        ValueError: If training or test data is invalid.
    """
    model_name = override_model if override_model else "xgb"
    train_df, _, latest_train_month = prepare_training_data(
        df, predict_month, months_back
    )
    test_df = df[df["run_month"] == latest_train_month].copy()

    if test_df.empty:
        return


    if "params_json" in test_df.columns:
        test_df["params_json"] = test_df["params_json"].apply(json.loads)
    if "params_json" in train_df.columns:
        train_df["params_json"] = train_df["params_json"].apply(json.loads)

    train_df, X_train_inputs, _ = expand_testerinputs(train_df)
    test_df, X_test_inputs, _ = expand_testerinputs(test_df)

    if X_train_inputs.empty or X_test_inputs.empty:
        return

    if X_test_inputs.isnull().values.any():
        raise ValueError(f"Cannot predict for {symbol} in {predict_month} due to NaNs.")

    X_train = X_train_inputs
    y_train = train_df[target]
    mask = y_train.notna() & np.isfinite(y_train)
    X_train = X_train.loc[mask]
    y_train = y_train.loc[mask]

    if X_train.empty or y_train.empty:
        return

    model, predicted_profits = train_model_wrapper(
        X_train, y_train, X_test_inputs, model_name
    )

    if len(predicted_profits) != len(X_test_inputs):
        raise ValueError(
            f"Prediction output size mismatch for {symbol} {predict_month}."
        )

    test_df = test_df.reset_index(drop=True)
    test_df["predicted_profit"] = predicted_profits.values
    top_row = select_best_prediction(test_df)

    confidence_score = estimate_confidence_score(y_train.values, model.predict(X_train))
    confidence_stars = confidence_score_to_stars(confidence_score)

    pred_entry = create_prediction_entry(
        top_row=top_row,
        symbol=symbol,
        model_name=model_name,
        month_str=predict_month,
        rank=1,
        confidence_score=confidence_score,
        confidence_stars=confidence_stars,
    )

    insert_predictions([pred_entry])
    print(
        f"🔮 Predicting {symbol:<8} {predict_month} ({model_name:<6}) → profit: ${top_row.get('predicted_profit'):7.2f} {confidence_stars}"
    )


def expand_testerinputs(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """
    Expand the 'params_json' column into individual input feature columns.

    Args:
        df: DataFrame containing a 'params_json' column.

    Returns:
        A tuple containing:
        - df: Updated DataFrame with expanded inputs.
        - X_inputs: DataFrame of input features only.
        - input_columns: Names of the input feature columns.

    Raises:
        ValueError: If the params_json column is missing or invalid.
    """
    if "params_json" not in df.columns:
        raise ValueError("DataFrame must contain a 'params_json' column.")

    if df["params_json"].isnull().all():
        raise ValueError("All params_json entries are null; cannot expand features.")

    if not isinstance(df["params_json"].iloc[0], dict):
        raise ValueError("params_json must contain dictionaries.")

    expanded_df = pd.json_normalize(df["params_json"].tolist())
    if expanded_df.empty:
        raise ValueError("Expanded params_json is empty. No features extracted.")

    input_columns = list(expanded_df.columns)
    if not input_columns:
        raise ValueError("No columns found after expanding params_json.")

    df = df.drop(columns=["params_json"], errors="ignore")
    df = pd.concat(
        [df.reset_index(drop=True), expanded_df.reset_index(drop=True)], axis=1
    )
    X_inputs = df[input_columns]

    return df, X_inputs, input_columns


def safe_jsonify_dict(d: dict[Any, Any]) -> dict[str, Any]:
    """
    Convert numpy types inside dictionary to pure Python types recursively.

    Args:
        d: Dictionary possibly containing NumPy scalar types.

    Returns:
        Dictionary safe for JSON serialization.
    """

    def convert_value(val: Any) -> Any:
        if isinstance(val, np.generic):
            return val.item()
        if isinstance(val, dict):
            return {str(k): convert_value(v) for k, v in val.items()}
        if isinstance(val, list):
            return [convert_value(x) for x in val]
        return val

    return convert_value(d)
