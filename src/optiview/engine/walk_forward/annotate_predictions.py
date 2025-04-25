# File: src/optiview/engine/walk_forward/annotate_predictions.py

from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from optiview.data.db_path import get_optiview_db_path, get_optibatch_db_path
from optiview.data.models import PredictedConfig
import pandas as pd
import sqlite3
import json
from sqlalchemy import create_engine, select, update

INPUT_TOLERANCE = 1e-4


def load_all_runs() -> list[dict]:
    db_path = get_optibatch_db_path()
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM runs").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_next_month_runs(all_runs: list[dict], symbol: str, month: str) -> list[dict]:
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
    for r in next_runs:
        if all(
            abs(inputs.get(k, 0) - r.get(k, 0)) <= INPUT_TOLERANCE
            for k in inputs
            if isinstance(r.get(k, None), (int, float))
        ):
            return r["profit"]
    return None


def compute_quality_score(predicted_profit: float, actual_profit: float, all_profits: list[float]) -> float:
    if actual_profit <= -100.0:
        return 0.0
    abs_error = abs(actual_profit - predicted_profit)
    closeness = 1 / (1 + abs_error)
    sorted_profits = sorted(all_profits, reverse=True)
    rank = sorted_profits.index(actual_profit) + 1
    rank_score = 1 - (rank - 1) / max(len(sorted_profits) - 1, 1)
    return round(0.7 * closeness + 0.3 * rank_score, 4)


def quality_to_stars(score: float) -> str:
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)


def annotate():
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)
    all_runs = load_all_runs()

    with Session(engine) as session:
        stmt = select(PredictedConfig)
        results = session.execute(stmt).scalars().all()

        print(f"🧠 Annotating {len(results)} predicted configs...")

        for row in results:
            symbol = row.symbol
            month = row.month
            next_runs = get_next_month_runs(all_runs, symbol, month)

            if not next_runs:
                continue

            inputs = row.inputs or {}
            predicted_profit = row.predicted_profit
            actual_profit = match_prediction(inputs, next_runs)

            if actual_profit is not None:
                all_profits = [r["profit"] for r in next_runs if "profit" in r]
                quality_score = compute_quality_score(
                    predicted_profit, actual_profit, all_profits
                )
                stars = quality_to_stars(quality_score)

                upd = (
                    update(PredictedConfig)
                    .where(PredictedConfig.month == row.month)
                    .where(PredictedConfig.symbol == row.symbol)
                    .where(PredictedConfig.model == row.model)
                    .where(PredictedConfig.rank == row.rank)
                    .values(
                        actual_profit=actual_profit,
                        quality_score=quality_score,
                        quality_stars=stars,
                    )
                )
                session.execute(upd)

        session.commit()
        print("✅ Done: re-annotated all predictions.")


if __name__ == "__main__":
    annotate()
