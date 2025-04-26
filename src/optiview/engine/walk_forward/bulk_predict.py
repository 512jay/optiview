# File: src/optiview/engine/walk_forward/bulk_predict.py

import argparse
import pandas as pd
from typing import List
from optiview.engine.walk_forward.predict import predict_optimal_config
from optiview.data.loader import load_runs
from optiview.maintenance.missing_months_report import generate_missing_months_report


def find_predictable_months_for_symbol(
    symbol_runs: pd.DataFrame, min_history: int = 3
) -> List[str]:
    """
    Find months for which we can predict, for a given symbol's historical runs.

    Args:
        symbol_runs (pd.DataFrame): DataFrame containing runs for a single symbol.
        min_history (int): Minimum number of past months required to predict.

    Returns:
        List[str]: List of months ("YYYY-MM") eligible for prediction.
    """
    months = symbol_runs["run_month"].dropna().unique()
    months_sorted = sorted(months)

    if len(months_sorted) <= min_history:
        return []

    return months_sorted[min_history:]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run bulk predictions.")
    parser.add_argument(
        "--months_back",
        type=int,
        default=3,
        help="How many months back to use for training.",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="profit",
        help="Target column name.",
    )
    parser.add_argument(
        "--prediction_col",
        type=str,
        default="predicted_profit",
        help="Prediction column name.",
    )
    parser.add_argument(
        "--prediction_error_penalty",
        type=float,
        default=1.0,
        help="Penalty weight for prediction error.",
    )
    parser.add_argument(
        "--full-history",
        action="store_true",
        help="Predict across all months instead of only the latest month.",
    )
    args = parser.parse_args()

    print("🔄 Starting automatic bulk prediction process...")

    df = load_runs()

    if df.empty:
        print("❌ No runs found to predict from.")
        return

    symbols = sorted(df["symbol"].unique())
    models = ["xgb", "rf", "cat", "lgbm", "gbr", "histgb"]

    for symbol in symbols:
        symbol_runs = df[df["symbol"] == symbol]

        if symbol_runs.empty:
            print(f"⚠️ No data for symbol: {symbol}. Skipping...")
            continue

        if args.full_history:
            predict_months = find_predictable_months_for_symbol(
                symbol_runs, min_history=args.months_back
            )
            if not predict_months:
                print(f"⚠️ Not enough historical months for {symbol}. Skipping...")
                continue
        else:
            months = symbol_runs["run_month"].dropna().unique()
            months = sorted(months)
            if len(months) <= args.months_back:
                print(f"⚠️ Not enough historical months for {symbol}. Skipping...")
                continue
            latest_month = months[-1]
            year_str, month_str = latest_month.split("-")
            year = int(year_str)
            month = int(month_str)
            if month == 12:
                next_month = f"{year + 1}-01"
            else:
                next_month = f"{year}-{month + 1:02d}"
            predict_months = [next_month]

        for predict_month in predict_months:
            for model in models:
                print(f"🔮 Predicting {symbol} ({model}) for {predict_month}...")

                try:
                    predict_optimal_config(
                        df=symbol_runs,
                        symbol=symbol,
                        predict_month=predict_month,  # ✅ Passed as a string, no Timestamp
                        months_back=args.months_back,
                        target=args.target,
                        prediction_col=args.prediction_col,
                        prediction_error_penalty=args.prediction_error_penalty,
                        override_model=model,
                    )
                except Exception as e:
                    print(
                        f"❌ Prediction failed for {symbol} ({model}) in {predict_month}: {e}"
                    )

    print("\n✅ Bulk prediction complete.")

    print("\n🧹 Checking for missing prediction months...")
    report = generate_missing_months_report(lookback_months=12)

    if report.empty:
        print("✅ No missing months detected.")
    else:
        print("⚠️ Missing months detected:")
        print(report.to_string(index=False))


if __name__ == "__main__":
    main()
