# File: src/optiview/engine/walk_forward/annotate_predictions.py

from pathlib import Path
import pandas as pd
import numpy as np
from typing import Optional

PREDICTIONS_DIR = Path("generated/predictions")
INPUT_TOLERANCE = 1e-6
CONFIDENCE_STAR_THRESHOLDS = [0.2, 0.4, 0.6, 0.8]


def find_actual_profit(actual_df: pd.DataFrame, pred_row: pd.Series) -> Optional[float]:
    """Match by fuzzy input matching with tolerance."""
    filtered = actual_df.copy()
    for col in actual_df.columns:
        if col.startswith("input_") and col in pred_row:
            filtered = filtered[
                np.isclose(filtered[col], pred_row[col], atol=INPUT_TOLERANCE)
            ]
    if not filtered.empty:
        return filtered["profit"].iloc[0]
    return None


from typing import Optional
import pandas as pd


def compute_quality_score(
    predicted_profit: float,
    actual_profit: float,
    all_actual_profits: list[float],
    max_loss_threshold: float = -100.0,
    weight_error: float = 0.7,
    weight_rank: float = 0.3,
) -> float:
    """
    Compute a quality score based on:
    1. How close the actual profit was to the predicted profit.
    2. Whether the actual profit was better than other configs.
    3. Penalize hard drawdown.

    Args:
        predicted_profit: The predicted value for this config.
        actual_profit: The actual result it achieved.
        all_actual_profits: List of all actual profits from other configs in the same month/symbol.
        max_loss_threshold: If actual_profit drops below this, score is zero.
        weight_error: Weight for error closeness.
        weight_rank: Weight for actual rank (top performer = best).

    Returns:
        A float between 0.0 and 1.0 indicating predictive quality.
    """
    if actual_profit <= max_loss_threshold:
        return 0.0

    # Score closeness of prediction (lower error = higher score)
    abs_error = abs(actual_profit - predicted_profit)
    closeness_score = 1.0 / (1.0 + abs_error)  # scales down smoothly with error

    # Score based on rank in actual performance
    sorted_profits = sorted(all_actual_profits, reverse=True)
    rank = sorted_profits.index(actual_profit) + 1
    rank_score = 1.0 - (rank - 1) / max(len(sorted_profits) - 1, 1)

    # Combine scores
    quality_score = weight_error * closeness_score + weight_rank * rank_score
    return round(quality_score, 4)


def quality_to_stars(score: float) -> str:
    count = sum(score >= t for t in CONFIDENCE_STAR_THRESHOLDS) + 1
    return "★" * count + "☆" * (5 - count)


def reorder_eval_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure evaluation columns are grouped next to predicted_profit."""
    if "predicted_profit" not in df.columns:
        return df
    cols = list(df.columns)
    insert_at = cols.index("predicted_profit") + 1
    eval_cols = ["actual_profit", "quality_score", "confidence_stars"]
    new_cols = (
        cols[:insert_at]
        + [col for col in eval_cols if col in df.columns]
        + [col for col in cols if col not in eval_cols or col == "predicted_profit"]
    )
    return df[new_cols]


def annotate_predictions() -> None:
    for month_dir in sorted(PREDICTIONS_DIR.iterdir()):
        if not month_dir.is_dir():
            continue

        next_month = pd.to_datetime(month_dir.name) + pd.DateOffset(months=1)
        next_month_str = next_month.strftime("%Y-%m")

        for symbol_dir in month_dir.iterdir():
            if not symbol_dir.is_dir():
                continue

            top_rows = []

            for model_dir in symbol_dir.iterdir():
                if not model_dir.is_dir():
                    continue

                pred_path = model_dir / "prediction_summary.csv"
                next_path = (
                    PREDICTIONS_DIR
                    / next_month_str
                    / symbol_dir.name
                    / model_dir.name
                    / "prediction_summary.csv"
                )

                if not pred_path.exists() or not next_path.exists():
                    print(
                        f"⚠️  Skipped {model_dir.name} (missing predictions or actuals)"
                    )
                    continue

                pred_df = pd.read_csv(pred_path)
                actual_df = pd.read_csv(next_path).dropna(subset=["profit"])
                actual_df["profit"] = actual_df["profit"].astype(float)

                # Gather all actual profits from next month
                all_profits = actual_df["profit"].tolist()

                actuals = []
                scores = []
                stars = []

                for _, row in pred_df.iterrows():
                    actual_profit = find_actual_profit(actual_df, row)
                    if actual_profit is not None:
                        predicted = row.get("predicted_profit", np.nan)
                        if pd.isna(predicted):
                            score = np.nan
                            star = ""
                        else:
                            score = compute_quality_score(predicted, actual_profit, all_profits)
                            star = quality_to_stars(score)

                        actuals.append(actual_profit)
                        scores.append(score)
                        stars.append(star)
                    else:
                        actuals.append(np.nan)
                        scores.append(np.nan)
                        stars.append("")

                pred_df["actual_profit"] = actuals
                pred_df["quality_score"] = scores
                pred_df["confidence_stars"] = stars

                pred_df = reorder_eval_columns(pred_df)
                pred_df.to_csv(pred_path, index=False)

                if not pred_df.empty:
                    top_rows.append(pred_df.iloc[[0]].assign(model=model_dir.name))

            if top_rows:
                df_all = pd.concat(top_rows, ignore_index=True)
                df_all.to_csv(symbol_dir / "all_models.csv", index=False)
                print(
                    f"✅ Annotated {symbol_dir.name} in {month_dir.name} → {symbol_dir / 'all_models.csv'}"
                )


if __name__ == "__main__":
    annotate_predictions()
