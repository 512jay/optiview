# File: src/optiview/engine/walk_forward/train.py

import pandas as pd
from typing import Any

def train_and_predict_profits(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    model_name: str,
) -> pd.Series:
    """
    Train the specified model and predict profits for test configs.

    Args:
        X_train: Training features.
        y_train: Training target (profits).
        X_test: Test features (configs to predict on).
        model_name: Which model to train ("xgb", "rf", etc.).

    Returns:
        A pandas Series of predicted profits aligned with X_test.
    """

    model = train_model(X_train, y_train, model_name)
    predicted = model.predict(X_test)

    return pd.Series(predicted, index=X_test.index)

import xgboost as xgb
import lightgbm as lgb
import catboost as cat
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
)
from typing import Any
import pandas as pd


def train_model(X_train: pd.DataFrame, y_train: pd.Series, model_name: str) -> Any:
    """
    Train a machine learning model based on the selected model name.

    Args:
        X_train: Training features.
        y_train: Training target (profit).
        model_name: Model type ("xgb", "rf", "cat", "lgbm", "gbr", "histgb").

    Returns:
        A trained model ready for prediction.
    """

    if model_name == "xgb":
        model = xgb.XGBRegressor(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            subsample=0.8,
            random_state=42,
        )
    elif model_name == "rf":
        model = RandomForestRegressor(
            n_estimators=100,
            max_depth=6,
            random_state=42,
        )
    elif model_name == "cat":
        model = cat.CatBoostRegressor(
            iterations=100,
            depth=4,
            learning_rate=0.1,
            verbose=False,
            random_state=42,
        )
    elif model_name == "lgbm":
        model = lgb.LGBMRegressor(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
            verbosity=-1,  # ✅ suppress LightGBM warnings
        )

    elif model_name == "gbr":
        model = GradientBoostingRegressor(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
        )
    elif model_name == "histgb":
        model = HistGradientBoostingRegressor(
            max_iter=100,
            max_depth=4,
            random_state=42,
        )
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    model.fit(X_train, y_train)
    return model
