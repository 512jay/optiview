# File: tests/engine/walk_forward/test_predict.py

"""Unit tests for predict.py helper functions."""

import pandas as pd
import numpy as np
import pytest
from typing import Any, Tuple

from optiview.engine.walk_forward.predict import (
    prepare_training_data,
    expand_input_features,
    select_best_prediction,
)

# Dummy Data
EXAMPLE_DATA = pd.DataFrame(
    {
        "run_month": ["2025-01", "2025-02", "2025-03", "2025-03"],
        "params_json": [
            '{"input_A": 1, "input_B": 2}',
            '{"input_A": 2, "input_B": 3}',
            '{"input_A": 3, "input_B": 4}',
            '{"input_A": 4, "input_B": 5}',
        ],
        "profit": [10, 15, 20, 25],
    }
)


def test_prepare_training_data_success():
    train_df, test_df, latest_month = prepare_training_data(
        EXAMPLE_DATA, predict_month="2025-04", months_back=2
    )
    assert not train_df.empty
    assert not test_df.empty
    assert latest_month == "2025-03"


def test_expand_input_features_success():
    expanded_df, X_inputs, input_keys = expand_input_features(EXAMPLE_DATA.copy())
    assert "input_A" in expanded_df.columns
    assert "input_B" in expanded_df.columns
    assert "input_A" in X_inputs.columns
    assert "input_B" in X_inputs.columns
    assert "input_A" in input_keys
    assert "input_B" in input_keys


def test_select_best_prediction_success():
    df = EXAMPLE_DATA.copy()
    df["predicted_profit"] = [5, 10, 30, 15]  # Simulated prediction outputs
    best_row = select_best_prediction(df)
    assert best_row["predicted_profit"] == 30
    assert best_row["run_month"] == "2025-03"
