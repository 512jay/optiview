# src/optiview/engine/metrics/metrics_engine.py

"""
metrics_engine.py

Compute alpha performance metrics such as IC, IR, and Breadth for OptiView predictions.
"""

import numpy as np
import pandas as pd
from scipy.stats import spearmanr


def calculate_ic(predicted, actual):
    """Compute Spearman Information Coefficient (IC)."""
    ic, _ = spearmanr(predicted, actual)
    return ic


def calculate_ir(active_returns):
    """Compute Information Ratio (mean active return / std deviation)."""
    mean = np.mean(active_returns)
    std = np.std(active_returns)
    return mean / std if std != 0 else np.nan


def calculate_breadth(df):
    """Estimate Breadth as count of independent evaluated predictions."""
    return len(df)
