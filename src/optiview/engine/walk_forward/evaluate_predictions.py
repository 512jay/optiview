# File: src/optiview/engine/walk_forward/evaluate_predictions.py

"""Evaluate predictions and insert results into EvaluatedSetting."""

from pathlib import Path
from typing import Optional
import pandas as pd
import sqlite3

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from optiview.database.db_paths import get_optiview_db_path, get_optibatch_db_path
from optiview.database.models import PredictedSetting, EvaluatedSetting

# Constants
INPUT_TOLERANCE = 1e-4
EVALUATOR_VERSION = "baseline_v1"

# --- Loading Functions ---


def load_all_runs() -> list[dict]:
    """Load all OptiBatch runs from the external database."""
    db_path = get_optibatch_db_path()
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM runs").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def load_predicted_settings() -> list[PredictedSetting]:
    """Load all predicted settings from the OptiView database."""
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)
    with Session(engine) as session:
        stmt = select(PredictedSetting)
        return list(session.execute(stmt).scalars().all())


# --- Matching Functions ---


def get_next_month_runs(all_runs: list[dict], symbol: str, month: str) -> list[dict]:
    """Filter runs to only the full next month runs for a given symbol."""
    next_month = pd.to_datetime(month) + pd.DateOffset(months=1)
    start = next_month.replace(day=1).strftime("%Y-%m-%d")
    end = (next_month + pd.offsets.MonthEnd(0)).strftime("%Y-%m-%d")
    return [
        r
        for r in all_runs
        if r["symbol"] == symbol
        and r["start_date"] == start
        and r["end_date"] == end
        and r["is_full_month"] == 1
    ]


def match_prediction(inputs: dict, next_runs: list[dict]) -> Optional[float]:
    """Find matching actual profit for predicted inputs."""
    for r in next_runs:
        if all(
            abs(inputs.get(k, 0) - r.get(k, 0)) <= INPUT_TOLERANCE
            for k in inputs
            if isinstance(r.get(k, None), (int, float))
        ):
            return r.get("profit")
    return None


# --- Evaluation Functions ---


def compute_quality_score(
    predicted_profit: float, actual_profit: float, all_profits: list[float]
) -> float:
    """Compute a quality score based on accuracy and ranking."""
    if actual_profit <= -100.0:
        return 0.0
    abs_error = abs(actual_profit - predicted_profit)
    closeness = 1 / (1 + abs_error)
    sorted_profits = sorted(all_profits, reverse=True)
    rank = sorted_profits.index(actual_profit) + 1
    rank_score = 1 - (rank - 1) / max(len(sorted_profits) - 1, 1)
    return round(0.7 * closeness + 0.3 * rank_score, 4)


def quality_to_stars(score: float) -> str:
    """Convert quality score to star rating."""
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)


# --- Main Evaluation Pipeline ---


def evaluate_predictions() -> None:
    """Evaluate all predictions and insert evaluations."""
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)
    all_runs = load_all_runs()
    predicted_settings = load_predicted_settings()

    print(f"🧠 Evaluating {len(predicted_settings)} predicted settings...")

    new_evaluations = []

    for pred in predicted_settings:
        symbol = pred.symbol
        month = pred.month
        next_runs = get_next_month_runs(all_runs, symbol, month)

        if not next_runs:
            continue

        actual_profit = match_prediction(pred.inputs or {}, next_runs)

        if actual_profit is not None:
            all_profits = [r["profit"] for r in next_runs if "profit" in r]
            quality_score = compute_quality_score(
                pred.predicted_profit, actual_profit, all_profits
            )
            quality_stars = quality_to_stars(quality_score)

            eval_row = EvaluatedSetting(
                month=pred.month,
                symbol=pred.symbol,
                model=pred.model,
                rank=pred.rank,
                evaluator_version=EVALUATOR_VERSION,
                quality_score=quality_score,
                quality_stars=quality_stars,
                confidence_score=pred.confidence_score,
                confidence_stars=pred.confidence_stars,
                notes=None,
                metrics_json=None,
            )
            new_evaluations.append(eval_row)

    # Insert new evaluations
    with Session(engine) as session:
        session.add_all(new_evaluations)
        session.commit()

    print(f"✅ Done: Inserted {len(new_evaluations)} evaluated settings.")


# --- CLI Entrypoint ---

if __name__ == "__main__":
    evaluate_predictions()
