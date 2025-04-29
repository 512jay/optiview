"""Predict the optimal configuration for trading strategies."""

from __future__ import annotations
from typing import Optional, Any

import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

from optiview.engine.walk_forward.train_model import train_model
from optiview.database.models import PredictedSetting
from optiview.database.session import get_optiview_session
from optiview.engine.walk_forward.scoring_helpers import (
    estimate_confidence_score,
    confidence_score_to_stars,
)


def prepare_training_data(
    df: pd.DataFrame,
    predict_month: str,
    months_back: int,
) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    """Prepare training and testing data for walk-forward prediction.

    Args:
        df (pd.DataFrame): DataFrame containing historical runs.
        predict_month (str): Month to predict for (format: YYYY-MM).
        months_back (int): Number of months to look back for training.

    Returns:
        tuple:
            - pd.DataFrame: Training DataFrame.
            - pd.DataFrame: Empty Testing DataFrame (since future month is synthetic).
            - str: Latest month used for training.

    Raises:
        ValueError: If insufficient training months are available.
    """
    all_months = sorted(df["run_month"].unique())

    # When predicting a true next month, it won't exist yet — do not raise error
    if not all_months:
        raise ValueError("No available months in provided data.")

    predict_idx = len(all_months)  # Assume predict_month is next after last available
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
    """Train model and predict profits."""
    return train_model(
        X_train=X_train, y_train=y_train, X_test=X_test, model_name=model_name
    )


def select_best_prediction(df: pd.DataFrame) -> pd.Series:
    """Select the best predicted configuration based on predicted_profit."""
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
    """Convert NumPy types to pure Python types recursively."""
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
    """Create a prediction entry for insertion into the database.

    Args:
        top_row (pd.Series): Top selected configuration row.
        symbol (str): Trading symbol.
        model_name (str): Name of the ML model used.
        month_str (str): Target month for prediction (format: YYYY-MM).
        rank (int): Prediction rank (usually 1).
        confidence_score (Optional[float]): Estimated confidence score.
        confidence_stars (Optional[str]): Confidence score as stars.

    Returns:
        dict[str, Any]: Safe dictionary ready for database insertion.
    """
    params = {
        k: safe_convert(v)
        for k, v in top_row.items()
        if k
        not in {
            "run_id",
            "symbol",
            "run_month",
            "profit",
            "predicted_profit",
        }
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
        "params_json": safe_jsonify_dict(top_row.to_dict()),
        "run_id": None,
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
            # Update existing prediction fields
            existing.version = pred["version"]
            existing.predicted_profit = pred["predicted_profit"]
            existing.confidence_score = pred["confidence_score"]
            existing.confidence_stars = pred["confidence_stars"]
            existing.inputs = pred["inputs"]
            existing.params_json = pred["params_json"]
            existing.tags = pred.get("tags", [])
            existing.notes = pred.get("notes", None)
            print(
                f"🔄 Updated prediction for {pred['symbol']} {pred['month']} ({pred['model']})"
            )
        else:
            # Insert new prediction
            setting = PredictedSetting(**pred)
            session.add(setting)
            print(
                f"➕ Inserted new prediction for {pred['symbol']} {pred['month']} ({pred['model']})"
            )

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
        df: The raw historical runs DataFrame.
        symbol: The trading symbol to predict for.
        predict_month: The month we want to generate a prediction for (YYYY-MM).
        months_back: How many previous months of training data to use.
        override_model: Optional - specific ML model to force (e.g., 'xgb', 'rf', etc.).
        target: The optimization metric to predict (default: 'profit').

    Raises:
        ValueError: If prediction input contains NaNs or there is a data mismatch.
    """

    # Step 1: Pick model to use
    model_name = override_model if override_model else "xgb"

    # Step 2: Prepare training and test data
    train_df, _, latest_train_month = prepare_training_data(
        df, predict_month, months_back
    )

    # ✅ IMPORTANT FIX: always pick candidates from latest available training month, not predict_month
    test_df = df[df["run_month"] == latest_train_month].copy()
    print(f"🔎 Loaded {len(test_df)} rows for {symbol} {predict_month} (raw before expand)")
    print(f"🔎 Columns available before expand: {list(test_df.columns)}")

    print(
        f"🔎 Predicting for {symbol} {predict_month} based on candidates from {latest_train_month}"
    )
    print(f"Test Data months loaded: {test_df['run_month'].unique()}")

    if test_df.empty:
        print(
            f"⚠️ No test candidates available for {symbol} in {predict_month}. Skipping."
        )
        return
    
    # Step 3: Ensure params_json is parsed properly
    if "params_json" in test_df.columns:
        test_df["params_json"] = test_df["params_json"].apply(json.loads)

    if "params_json" in train_df.columns:
        train_df["params_json"] = train_df["params_json"].apply(json.loads)

    # Step 4: Expand the input features from params_json
    train_df, X_train_inputs, input_keys = expand_testerinputs(train_df)
    print(f"🔎 Training on {len(input_keys)} input features: {input_keys}")
    test_df, X_test_inputs, _ = expand_testerinputs(test_df)

    print(f"🔎 Expanded test inputs: {X_test_inputs.shape} shape")
    print(f"🔎 First few expanded test inputs:")
    print(X_test_inputs.head(5))

    # Now X_train_inputs and X_test_inputs have model-ready features

    if X_train_inputs.empty or X_test_inputs.empty:
        print(f"⚠️ No usable input features for {symbol} in {predict_month}. Skipping.")
        return

    # Step 5: Check for NaNs in test data
    if X_test_inputs.isnull().values.any():
        nan_summary_test = X_test_inputs.isnull().sum()
        print("⚠️ NaN values detected in X_test inputs before prediction:")
        print(nan_summary_test[nan_summary_test > 0])
        print("🔍 First few bad rows in X_test_inputs with NaNs:")
        print(X_test_inputs[X_test_inputs.isnull().any(axis=1)].head())
        raise ValueError(
            f"Cannot predict for {symbol} in {predict_month} because test inputs contain NaNs."
        )

    # Step 6: Prepare X_train and y_train for fitting
    X_train = X_train_inputs
    y_train = train_df[target]

    # Clean the training data: remove NaN or infinite values
    mask = y_train.notna() & np.isfinite(y_train)
    X_train = X_train.loc[mask]
    y_train = y_train.loc[mask]

    if X_train.empty or y_train.empty:
        print(
            f"⚠️ Skipping {symbol} {predict_month}: no valid training data after NaN filtering."
        )
        return

    # Step 7: Sanity check before fitting model
    if X_train.isnull().values.any():
        nan_summary_train = X_train.isnull().sum()
        print("⚠️ NaN values detected in X_train:")
        print(nan_summary_train[nan_summary_train > 0])
        raise ValueError(
            f"Cannot train model {model_name} for {symbol} {predict_month} due to NaNs."
        )

    # Step 8: Train model and make predictions
    model, predicted_profits = train_model_wrapper(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test_inputs,
        model_name=model_name,
    )

    if len(predicted_profits) != len(X_test_inputs):
        raise ValueError(
            f"⚠️ Prediction output size mismatch for {symbol} {predict_month}. Cannot proceed."
        )

    # Step 9: Attach predictions to test_df
    test_df = test_df.reset_index(drop=True)
    test_df["predicted_profit"] = predicted_profits.values

    # Step 10: Select the best predicted configuration
    top_row = select_best_prediction(test_df)

    # Step 11: Estimate confidence of the model
    train_preds = model.predict(X_train)
    confidence_score = estimate_confidence_score(y_train.values, train_preds)
    confidence_stars = confidence_score_to_stars(confidence_score)

    # Step 12: Create a prediction entry
    pred_entry = create_prediction_entry(
        top_row=top_row,
        symbol=symbol,
        model_name=model_name,
        month_str=predict_month,
        rank=1,
        confidence_score=confidence_score,
        confidence_stars=confidence_stars,
    )

    # Step 13: Insert or update into database
    insert_predictions([pred_entry])

    print(
        f"✅ Saved prediction for {symbol} ({model_name}) into database for {predict_month} with profit {top_row.get('predicted_profit'):.2f}."
    )

def expand_testerinputs(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """
    Expands the 'params_json' field into separate input feature columns.

    Args:
        df: DataFrame containing a 'params_json' column with encoded parameters.

    Returns:
        Tuple of:
            - Updated full DataFrame (original columns + expanded input features)
            - X_inputs DataFrame (only input feature columns)
            - List of input column names (feature names)

    Raises:
        ValueError: If params_json missing, expansion fails, or no columns found.
    """

    # Step 1: Validate input
    if "params_json" not in df.columns:
        raise ValueError("DataFrame must contain a 'params_json' column.")

    print(f"🔎 Loaded {len(df)} rows for {df['symbol'].iloc[0]}")

    if df["params_json"].isnull().all():
        raise ValueError("All params_json entries are null; cannot expand features.")

    if isinstance(df["params_json"].iloc[0], dict):
        raw_data: list[dict[str, Any]] = df["params_json"].tolist()
    else:
        raise ValueError(
            "params_json must contain dictionaries. Found unexpected type."
        )

    # Step 2: Expand params_json
    expanded_df = pd.json_normalize(raw_data)
    print(f"🔎 Expanded params_json into {len(expanded_df.columns)} columns")

    if expanded_df.empty:
        raise ValueError("Expanded params_json is empty. No features extracted.")

    # Step 3: Use ALL columns now
    input_columns: list[str] = list(expanded_df.columns)
    if not input_columns:
        raise ValueError("No columns found after expanding params_json.")

    print(f"🔎 Expanded input columns: {input_columns}")

    # Step 4: Attach expanded features back to original DataFrame
    df = df.drop(columns=["params_json"], errors="ignore")
    df = pd.concat(
        [df.reset_index(drop=True), expanded_df.reset_index(drop=True)], axis=1
    )

    print(f"🔎 Expanded DataFrame shape: {df.shape}")

    # Step 5: Build X_inputs DataFrame (only model inputs)
    X_inputs = df[input_columns]
    print(f"🔎 X_inputs shape: {X_inputs.shape}")

    return df, X_inputs, input_columns


def safe_expand_testerinputs(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """
    Safely expands params_json for UI or flexible pipelines.

    If anything goes wrong (e.g., missing params_json), returns empty X_inputs
    but does NOT crash the program.

    Args:
        df: DataFrame that should contain 'params_json' column.

    Returns:
        Tuple of:
            - Updated DataFrame (with expanded input columns if possible)
            - X_inputs DataFrame (empty if expansion fails)
            - List of input column names (empty if expansion fails)
    """
    if "params_json" not in df.columns:
        print("⚠️ Warning: No 'params_json' column found. Skipping expansion.")
        return df, pd.DataFrame(), []

    try:
        expanded = pd.json_normalize(df["params_json"].tolist())
    except Exception as e:
        print(f"⚠️ Warning: Failed to normalize params_json. Reason: {e}")
        return df, pd.DataFrame(), []

    if expanded.empty:
        print("⚠️ Warning: Expansion produced empty DataFrame.")
        return df, pd.DataFrame(), []

    df = df.copy()
    df = df.drop(columns=["params_json"], errors="ignore")
    df = pd.concat([df.reset_index(drop=True), expanded.reset_index(drop=True)], axis=1)

    # ✅ Use all expanded columns now, not only input_
    input_columns: list[str] = list(expanded.columns)

    if not input_columns:
        print("⚠️ Warning: No columns found after expansion.")
        return df, pd.DataFrame(), []

    X_inputs = df[input_columns]

    return df, X_inputs, input_columns


def safe_jsonify_dict(d: dict[str, Any]) -> dict[str, Any]:
    """Convert numpy types inside dictionary to pure Python types recursively."""

    def convert_value(val: Any) -> Any:
        if isinstance(val, np.generic):
            return val.item()  # convert np.int64, np.float64, etc
        if isinstance(val, dict):
            return {k: convert_value(v) for k, v in val.items()}
        if isinstance(val, list):
            return [convert_value(x) for x in val]
        return val

    return convert_value(d)
