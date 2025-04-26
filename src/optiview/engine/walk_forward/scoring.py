# File: src/optiview/engine/walk_forward/scoring.py

from typing import List
import pandas as pd
import numpy as np


def compute_stable_score(
    df: pd.DataFrame,
    input_keys: List[str],
    target: str = "profit",
    prediction_col: str = "predicted_profit",
    prediction_error_penalty: float = 1.0,
) -> pd.Series:
    """
    Computes a stability score for each unique config.
    If predicted profits are not present, just use average actual profit.
    If predicted profits are available, penalize based on prediction error.
    """
    if df.empty:
        raise ValueError("Training dataframe is empty.")

    group_keys = ["symbol", "model"] + input_keys
    grouped = df.groupby(group_keys)

    avg_profit = grouped[target].mean()

    if prediction_col not in df.columns:
        # We're in training mode — just rank by realized profit
        return avg_profit

    # Prediction/annotation mode — penalize prediction error
    df["prediction_error"] = np.abs(df[prediction_col] - df[target])
    avg_error = grouped["prediction_error"].mean()
    return avg_profit - (prediction_error_penalty * avg_error)
