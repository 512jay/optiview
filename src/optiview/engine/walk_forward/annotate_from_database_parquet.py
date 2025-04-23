# File: src/optiview/engine/walk_forward/annotate_from_database_parquet.py

import sqlite3
import pandas as pd
from pathlib import Path
from typing import Optional
from optiview.data.db_path import get_db_path

DB_PATH = get_db_path()
PREDICTIONS_DIR = Path("generated/predictions")
INPUT_TOLERANCE = 1e-4


def load_all_runs() -> list[dict]:
    conn = sqlite3.connect(DB_PATH)
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


def clean_prediction_row(row: dict) -> dict:
    return {k.split(".")[0]: v for k, v in row.items()}


def find_actual_profit(next_runs: list[dict], pred_row: dict) -> Optional[float]:
    for actual in next_runs:
        if all(
            abs(pred_row.get(k, 0) - actual.get(k, 0)) <= INPUT_TOLERANCE
            for k in pred_row
            if k.startswith("input_") and k in actual
        ):
            return actual["profit"]
    return None


def quality_to_stars(score: float) -> str:
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)


def compute_quality_score(
    predicted_profit: float, actual_profit: float, all_actual_profits: list[float]
) -> float:
    if actual_profit <= -100.0:
        return 0.0
    abs_error = abs(actual_profit - predicted_profit)
    closeness = 1 / (1 + abs_error)
    sorted_profits = sorted(all_actual_profits, reverse=True)
    rank = sorted_profits.index(actual_profit) + 1
    rank_score = 1 - (rank - 1) / max(len(sorted_profits) - 1, 1)
    return round(0.7 * closeness + 0.3 * rank_score, 4)


def annotate():
    all_runs = load_all_runs()
    for month_dir in sorted(PREDICTIONS_DIR.iterdir()):
        if not month_dir.is_dir():
            continue
        print(f"📁 Month: {month_dir.name}")
        month_str = month_dir.name

        for symbol_dir in month_dir.iterdir():
            if not symbol_dir.is_dir():
                continue
            symbol = symbol_dir.name
            print(f"  📂 Symbol: {symbol}")
            next_runs = get_next_month_runs(all_runs, symbol, month_str)

            for model_dir in symbol_dir.iterdir():
                if not model_dir.is_dir():
                    continue
                print(f"    🔍 Model: {model_dir.name}")
                pred_path = model_dir / "prediction_summary.parquet"
                if not pred_path.exists():
                    print(f"    ⚠️ Skipped: missing {pred_path}")
                    continue

                df = pd.read_parquet(pred_path)
                df.columns = [c.split(".")[0] for c in df.columns]
                df = df.loc[:, ~df.columns.duplicated()]  # dedupe columns

                actuals, scores, stars = [], [], []
                for row in df.to_dict(orient="records"):
                    clean_row = clean_prediction_row(row)
                    actual_profit = find_actual_profit(next_runs, clean_row)
                    if actual_profit is not None:
                        all_profits = [r["profit"] for r in next_runs if "profit" in r]
                        score = compute_quality_score(
                            clean_row["predicted_profit"], actual_profit, all_profits
                        )
                        actuals.append(actual_profit)
                        scores.append(score)
                        stars.append(quality_to_stars(score))
                    else:
                        actuals.append(None)
                        scores.append(None)
                        stars.append("")

                df["actual_profit"] = actuals
                df["quality_score"] = scores
                df["quality_stars"] = stars
                df = df.loc[:, ~df.columns.duplicated()]  # final dedup

                out_path = model_dir / "annotations.parquet"
                df.to_parquet(out_path, index=False)
                print(f"    ✅ Annotated → {out_path}")


if __name__ == "__main__":
    annotate()
