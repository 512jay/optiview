# File: src/optiview/analysis/evaluate_predictions.py
# Purpose: Evaluate month-by-month prediction accuracy and rank performance of top-3 predictions

import pandas as pd
import sqlite3
import numpy as np
from pathlib import Path
from sklearn.metrics import mean_squared_error
from typing import Literal


def load_data(db_path: Path) -> pd.DataFrame:
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql("SELECT * FROM runs", conn)
    conn.close()

    df_params = pd.json_normalize(df["params_json"].apply(eval))
    df = pd.concat([df.drop(columns=["params_json"]), df_params], axis=1)

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["run_month"] = df["start_date"].dt.to_period("M").dt.to_timestamp()
    df["custom_score"] = pd.to_numeric(df["custom_score"], errors="coerce")
    df["profit"] = pd.to_numeric(df["profit"], errors="coerce")

    for col in df.columns:
        if col.startswith("input_"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    required_cols = ["start_date", "run_month", "symbol", "profit"] + [
        col for col in df.columns if col.startswith("input_")
    ]
    return df.dropna(subset=required_cols)


def evaluate_predictions(
    df: pd.DataFrame,
    target_metric: Literal["custom_score", "profit"] = "custom_score",
    months_back: int = 1,
) -> None:
    features = [col for col in df.columns if col.startswith("input_")]
    target = target_metric

    for symbol in df["symbol"].unique():
        print(f"\n================ {symbol} ================")
        symbol_df = df[df["symbol"] == symbol].copy()
        sorted_months = sorted(symbol_df["run_month"].unique())
        print("Found months:", [m.strftime("%b %Y") for m in sorted_months])

        results = []
        rank_stats = {1: 0, 2: 0, 3: 0, "total": 0}

        for i in range(months_back, len(sorted_months)):
            train_month = sorted_months[i - months_back]
            test_month = sorted_months[i]

            train_df = symbol_df[symbol_df["run_month"] == train_month].copy()
            test_df = symbol_df[symbol_df["run_month"] == test_month].copy()

            print(
                f"\n📆 {train_month.strftime('%b %Y')} → {test_month.strftime('%b %Y')}"
            )
            print("Train size before filtering:", len(train_df))
            print("Test size:", len(test_df))

            train_df = train_df[train_df[target].notna()]

            print("Train size after filtering:", len(train_df))

            if train_df.empty or test_df.empty:
                continue

            X_train = train_df[features]
            y_train = train_df[target]
            X_test = test_df[features]

            from sklearn.ensemble import RandomForestRegressor

            model = RandomForestRegressor(random_state=42)
            model.fit(X_train, y_train)
            test_df["predicted_score"] = model.predict(X_test)

            top3 = (
                test_df.sort_values("predicted_score", ascending=False).head(3).copy()
            )
            predicted_avg = top3["predicted_score"].mean()
            actual_avg = top3[target].mean()
            profitable = (top3[target] > 0).any()

            top3 = top3.reset_index(drop=True)
            actual_ranks = top3[target].rank(ascending=False, method="first")
            best_index = actual_ranks.idxmin()
            rank_stats[best_index + 1] += 1
            rank_stats["total"] += 1

            # --- Quality scoring: Roll up from previous month ---
            if i > 0:
                prev_month_str = sorted_months[i - 1].strftime("%Y-%m")
                test_month_str = sorted_months[i].strftime("%Y-%m")

                # Load predictions from previous month
                pred_path = (
                    Path("generated/predictions")
                    / prev_month_str
                    / symbol
                    / "prediction_summary.csv"
                )
                if pred_path.exists():
                    predicted_df = pd.read_csv(pred_path)
                    actual_df = test_df[["symbol", "input_LongStopLossPercent", "input_ShortStopLossPercent", target]].copy()
                    actual_df.rename(columns={target: "profit_actual"}, inplace=True)

                    compute_quality_scores(test_month_str, predicted_df, actual_df)
                else:
                    print(
                        f"⚠️ No prediction_summary.csv found for {symbol} in {prev_month_str}, skipping quality score."
                    )

            results.append(
                {
                    "month": test_month.strftime("%b %Y"),
                    "predicted_avg": predicted_avg,
                    "actual_avg": actual_avg,
                    "delta": actual_avg - predicted_avg,
                    "any_profitable": profitable,
                    "top_actual_rank": best_index + 1,
                }
            )

        results_df = pd.DataFrame(results)
        print("\n📊 Top-3 Avg Prediction Accuracy Summary")
        print(results_df)

        if not results_df.empty:
            rmse = np.sqrt(
                mean_squared_error(
                    results_df["actual_avg"], results_df["predicted_avg"]
                )
            )
            hit_rate = results_df["any_profitable"].mean() * 100
            avg_delta = results_df["delta"].mean()

            print("\n✅ Metrics (Top-3 Avg):")
            print(f"RMSE: {rmse:.2f}")
            print(f"Hit Rate: {hit_rate:.1f}%")
            print(f"Avg. Prediction Error: {avg_delta:.2f}")

            print("\n🏆 Actual Best Performer by Predicted Rank:")
            for rank in [1, 2, 3]:
                pct = (
                    (rank_stats[rank] / rank_stats["total"] * 100)
                    if rank_stats["total"] > 0
                    else 0
                )
                print(
                    f"Predicted Rank #{rank} was best: {rank_stats[rank]}x ({pct:.1f}%)"
                )


def compute_quality_scores(
    month: str, predicted_df: pd.DataFrame, actual_df: pd.DataFrame
) -> pd.DataFrame:
    # Ensure float merge keys are rounded consistently
    for df in [predicted_df, actual_df]:
        df["input_LongStopLossPercent"] = df["input_LongStopLossPercent"].round(6)
        df["input_ShortStopLossPercent"] = df["input_ShortStopLossPercent"].round(6)

    # Merge predicted and actual runs
    merged = predicted_df.merge(
        actual_df,
        on=["symbol", "input_LongStopLossPercent", "input_ShortStopLossPercent"],
        suffixes=("_predicted", "_actual"),
    )

    if merged.empty:
        print(f"⚠️ No matches found when merging predicted and actual for {month}.")
    else:
        print(f"🔗 Merged {len(merged)} rows for {month}.")

    # Calculate quality score
    merged["profit_delta"] = merged["profit_actual"] - merged["predicted_score"]
    merged["quality_score"] = merged["profit_delta"].clip(-500, 500) / 1000 + 0.5

    # Save to same folder as predictions (not in /quality)
    output_dir = Path("generated/predictions") / month
    output_dir.mkdir(parents=True, exist_ok=True)
    merged.to_csv(output_dir / "quality_scores.csv", index=False)

    print(f"✅ Quality scores for {month} saved → {output_dir}/quality_scores.csv")

    return merged


if __name__ == "__main__":
    db_path = Path("db/optibatch.db")
    df = load_data(db_path)
    evaluate_predictions(df, target_metric="profit", months_back=1)
