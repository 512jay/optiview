# File: src/optiview/engine/walk_forward/train_model.py

"""Training and prediction utilities for OptiView machine learning models."""

import pandas as pd
import numpy as np
from typing import Any, Tuple, cast, Dict

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
)
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from optiview.engine.walk_forward.model_configs import MODEL_CONFIGS


def train_and_predict_profits(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    model_name: str,
) -> Tuple[Any, pd.Series]:
    """Train a model and predict profits on a test set.

    Args:
        X_train (pd.DataFrame): Training input features.
        y_train (pd.Series): Training target profits.
        X_test (pd.DataFrame): Test input features.
        model_name (str): Model identifier ("xgb", "rf", "cat", "lgbm", "gbr", "histgb").

    Returns:
        Tuple[Any, pd.Series]: Trained model and predicted profits for X_test.
    """
    try:
        params = MODEL_CONFIGS[model_name]
    except KeyError:
        raise ValueError(f"Unsupported model: {model_name}")

    # ⛑️ Special case: Drop NaNs for GradientBoostingRegressor
    if model_name == "gbr":
        original_size = len(X_train)
        valid_idx = X_train.dropna().index
        X_train = X_train.loc[valid_idx]
        y_train = y_train.loc[valid_idx]
        dropped = original_size - len(X_train)
        if dropped > 0:
            print(f"⚠️ GBR: Dropped {dropped} rows with NaNs before training.")

    if model_name == "xgb":
        model = XGBRegressor(**cast(Dict[str, Any], params))
    elif model_name == "rf":
        model = RandomForestRegressor(**params)
    elif model_name == "cat":
        model = CatBoostRegressor(**params)
    elif model_name == "lgbm":
        model = LGBMRegressor(**cast(Dict[str, Any], params))
    elif model_name == "gbr":
        model = GradientBoostingRegressor(**params)
    elif model_name == "histgb":
        model = HistGradientBoostingRegressor(**params)
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    return model, pd.Series(preds)


# Alias for consistency
train_model = train_and_predict_profits
