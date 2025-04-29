# File: src/optiview/data/join_tools.py

"""Utilities for joining predictions with metadata, database helpers, and INI generation."""

from __future__ import annotations

import sqlite3
from typing import Any, Optional

import pandas as pd
from sqlalchemy.orm import Session

from optiview.database.models import PredictedSetting
from optiview.database.session import get_optiview_session


# --- Database Utilities ---
def insert_predictions(predictions: list[dict[str, Any]]) -> None:
    """Insert a list of predicted settings into the database.

    Args:
        predictions (list[dict]): List of predicted setting dictionaries.

    Returns:
        None
    """
    session = get_optiview_session()
    try:
        for pred in predictions:
            setting = PredictedSetting(**pred)
            session.add(setting)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# --- Feature Extraction Utilities ---


def extract_input_matrix(
    df: pd.DataFrame,
    input_keys: list[str],
) -> pd.DataFrame:
    """Extract feature columns from a DataFrame based on input keys.

    Args:
        df (pd.DataFrame): DataFrame containing input parameters.
        input_keys (list[str]): List of input feature names.

    Returns:
        pd.DataFrame: Feature matrix (X) for training or prediction.
    """
    if not input_keys:
        return pd.DataFrame()
    return df[input_keys]


def get_training_features(df: pd.DataFrame) -> list[str]:
    """Identify training feature names based on available params_json keys.

    Args:
        df (pd.DataFrame): DataFrame containing optimization runs.

    Returns:
        list[str]: List of input parameter names.
    """
    if df.empty:
        return []
    sample_params = df["params_json"].dropna().iloc[0]
    if not isinstance(sample_params, dict):
        return []
    return sorted(sample_params.keys())


# --- Prediction Dictionary Utilities ---


def convert_to_prediction_dict(
    row: pd.Series,
    symbol: str,
    model_name: str,
    month: str,
    confidence_score: Optional[float] = None,
    confidence_stars: Optional[str] = None,
    version: Optional[str] = None,
    predicted_profit: Optional[float] = None,
) -> dict[str, Any]:
    """Convert a prediction result row into a dictionary for database insertion.

    Args:
        row (pd.Series): Row containing params_json and results.
        symbol (str): Trading symbol.
        model_name (str): Machine learning model used.
        month (str): Month being predicted ("YYYY-MM").
        confidence_score (Optional[float], optional): Confidence score (0.0–1.0). Defaults to None.
        confidence_stars (Optional[str], optional): Confidence stars ("★☆☆☆☆"). Defaults to None.
        version (Optional[str], optional): Config version tag. Defaults to None.
        predicted_profit (Optional[float], optional): Predicted profit value. Defaults to None.

    Returns:
        dict[str, Any]: Dictionary ready for database insertion.
    """
    params = row.get("params_json", {})
    if not isinstance(params, dict):
        params = {}

    return {
        "month": month,
        "symbol": symbol,
        "model": model_name,
        "confidence_score": confidence_score,
        "confidence_stars": confidence_stars,
        "predicted_profit": predicted_profit,
        "params_json": params,
        "version": version,
    }


def save_prediction_outputs(
    predictions: list[dict[str, Any]],
    session: Optional[Session] = None,
) -> None:
    """Save prediction outputs into the database.

    Args:
        predictions (list[dict]): List of prediction dictionaries.
        session (Optional[Session], optional): Existing database session if available.

    Returns:
        None
    """
    close_session = False
    if session is None:
        session = get_optiview_session()
        close_session = True

    try:
        for pred in predictions:
            setting = PredictedSetting(**pred)
            session.add(setting)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        if close_session:
            session.close()
