# File: src/optiview/engine/walk_forward/model_configs.py

"""Model hyperparameter configurations and versioning for OptiView training."""

CONFIG_VERSION = "v1"

MODEL_CONFIGS = {
    "xgb": {
        "n_estimators": 100,
        "max_depth": 4,
        "learning_rate": 0.1,
        "subsample": 0.8,
        "random_state": 42,
        "n_jobs": -1,
    },
    "rf": {
        "n_estimators": 100,
        "max_depth": 6,
        "random_state": 42,
        "n_jobs": -1,
    },
    "cat": {
        "iterations": 100,
        "depth": 4,
        "learning_rate": 0.1,
        "verbose": False,
        "random_state": 42,
    },
    "lgbm": {
        "n_estimators": 100,
        "max_depth": 4,
        "learning_rate": 0.1,
        "random_state": 42,
        "verbosity": -1,
    },
    "gbr": {
        "n_estimators": 100,
        "max_depth": 4,
        "learning_rate": 0.1,
        "random_state": 42,
    },
    "histgb": {
        "max_iter": 100,
        "max_depth": 4,
        "random_state": 42,
    },
}

# Supported models derived from hyperparameter configs
ALL_MODELS = list(MODEL_CONFIGS.keys())
