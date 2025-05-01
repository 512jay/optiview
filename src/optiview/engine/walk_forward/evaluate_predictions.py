# File: src/optiview/engine/walk_forward/evaluate_predictions.py

"""
Evaluate predictions by comparing to actual runs from the same month.

This version aligns with:
- OptiView architecture: predictions are stored in the evaluation month
- Realistic scaling: loads runs symbol-by-month
- Correct input matching: parses params_json and filters only input fields
"""

import enum
import json
from typing import Optional, Any

import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from optiview.database.db_paths import get_optiview_db_path
from optiview.database.models import PredictedSetting, EvaluatedSetting
from optiview.database.loader import load_symbol_months_runs
from optiview.engine.walk_forward.time_utils import get_current_month

# --- Config ---
INPUT_TOLERANCE = 0.05
EVALUATOR_VERSION = "baseline_v1"


def safe_enum(value: Any) -> Any:
    """Return the string value of an Enum, or the value itself if not an Enum.

    Args:
        value: Possibly an Enum instance.

    Returns:
        A string representation of the value.
    """
    return value.value if isinstance(value, enum.Enum) else value


def match_prediction(
    predicted_inputs: dict, actual_runs: list[dict]
) -> Optional[float]:
    """Find the actual profit from runs that closely match predicted strategy parameters.

    Args:
        predicted_inputs: Predicted configuration inputs.
        actual_runs: List of run records from the evaluation month.

    Returns:
        Actual run profit if match is found, otherwise None.
    """
    filtered_predicted_inputs = {
        k: v for k, v in predicted_inputs.items() if k.startswith("input_")
    }

    for run in actual_runs:
        params_json = run.get("params_json")
        if not params_json:
            continue

        try:
            actual_inputs = json.loads(params_json)
        except Exception:
            continue

        mismatches = []
        for k in filtered_predicted_inputs:
            if k in actual_inputs and isinstance(actual_inputs[k], (int, float)):
                diff = abs(filtered_predicted_inputs[k] - actual_inputs[k])
                if diff > INPUT_TOLERANCE:
                    mismatches.append(
                        (k, filtered_predicted_inputs[k], actual_inputs[k], diff)
                    )

        if not mismatches:
            return run.get("profit")

    return None


def compute_quality_score(
    predicted_profit: float, actual_profit: float, all_profits: list[float]
) -> float:
    """Compute a quality score based on prediction accuracy and rank position.

    Args:
        predicted_profit: Profit predicted by the model.
        actual_profit: Profit from actual run.
        all_profits: List of all profits in that month.

    Returns:
        Quality score as a float between 0 and 1.
    """
    if actual_profit <= -100.0:
        return 0.0
    abs_error = abs(actual_profit - predicted_profit)
    closeness = 1 / (1 + abs_error)
    sorted_profits = sorted(all_profits, reverse=True)
    rank = sorted_profits.index(actual_profit) + 1
    rank_score = 1 - (rank - 1) / max(len(sorted_profits) - 1, 1)
    return round(0.7 * closeness + 0.3 * rank_score, 4)


def quality_to_stars(score: float) -> str:
    """Convert a numeric quality score to a 1–5 star rating.

    Args:
        score: Quality score.

    Returns:
        Star string representation.
    """
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)


def evaluate_predictions() -> None:
    """Evaluate all predicted settings and store evaluation results."""
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

    with Session(engine) as session:
        predictions: list[PredictedSetting] = (
            session.query(PredictedSetting)
            .order_by(PredictedSetting.symbol, PredictedSetting.month)
            .all()
        )

    print(f"🧠 Evaluating {len(predictions)} predicted settings...")

    current_month = get_current_month()
    evaluations: list[EvaluatedSetting] = []

    for pred in predictions:
        if pred.month >= current_month:
            continue  # Skip current or future months

        runs_df = load_symbol_months_runs(pred.symbol, [pred.month])
        if runs_df.empty:
            continue

        actual_profit = match_prediction(pred.inputs or {}, runs_df.to_dict("records"))
        if actual_profit is None:
            continue

        all_profits = runs_df["profit"].dropna().tolist()
        quality_score = compute_quality_score(
            pred.predicted_profit, actual_profit, all_profits
        )
        quality_stars = quality_to_stars(quality_score)

        evaluation = EvaluatedSetting(
            month=pred.month,
            symbol=pred.symbol,
            model=safe_enum(pred.model),
            rank=pred.rank,
            evaluator_version=EVALUATOR_VERSION,
            quality_score=quality_score,
            quality_stars=quality_stars,
            confidence_score=pred.confidence_score,
            confidence_stars=pred.confidence_stars,
            predicted_profit=pred.predicted_profit,
            actual_result=actual_profit,
            matched_run_id=pred.run_id,
            matched_job_id=pred.job_id,
            notes=None,
            metrics_json=None,
        )
        evaluations.append(evaluation)

    if not evaluations:
        print("⚠️ No matching evaluations found.")
        return

    with Session(engine) as session:
        session.add_all(evaluations)
        session.commit()

    print(f"✅ Done: Inserted {len(evaluations)} evaluated settings.")


if __name__ == "__main__":
    evaluate_predictions()
