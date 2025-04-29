# File: src/optiview/engine/walk_forward/scoring_helpers.py

"""Helper functions for estimating prediction confidence scores."""

from __future__ import annotations

from typing import Tuple

import numpy as np
from sklearn.metrics import r2_score, root_mean_squared_error


def estimate_confidence_score(
    y_true: np.ndarray,
    y_pred: np.ndarray,
) -> float:
    """Estimate a composite confidence score based on R² and RMSE.

    Args:
        y_true (np.ndarray): Ground truth target values.
        y_pred (np.ndarray): Predicted target values.

    Returns:
        float: Composite confidence score between 0.0 and 1.0.
    """
    if len(y_true) == 0:
        return 0.0

    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)

    mean_target = np.mean(np.abs(y_true)) if np.mean(np.abs(y_true)) != 0 else 1.0

    rmse_penalty = 1.0 - (rmse / mean_target)
    rmse_penalty = max(0.0, min(1.0, rmse_penalty))  # Clamp between 0-1

    confidence = 0.7 * max(0.0, r2) + 0.3 * rmse_penalty
    confidence = max(0.0, min(1.0, confidence))  # Clamp final score

    return round(confidence, 4)


def confidence_score_to_stars(score: float) -> str:
    """Convert a numeric confidence score into a star rating.

    Args:
        score (float): Confidence score between 0.0 and 1.0.

    Returns:
        str: Star rating string (e.g., '★★★☆☆').
    """
    thresholds = [0.2, 0.4, 0.6, 0.8]
    stars = sum(score >= t for t in thresholds) + 1
    return "★" * stars + "☆" * (5 - stars)
