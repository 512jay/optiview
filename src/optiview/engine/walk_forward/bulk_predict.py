# File: src/optiview/engine/walk_forward/bulk_predict.py

import argparse
import pandas as pd
from optiview.engine.walk_forward.predict import predict_optimal_config
from optiview.data.loader import load_runs
from optiview.maintenance.missing_months_report import generate_missing_months_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Run bulk predictions.")
    parser.add_argument(
        "--months_back",
        type=int,
        default=3,
        help="How many months back to use for training.",
    )
    parser.add_argument(
        "--target", type=str, default="profit", help="Target column name."
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
    args = parser.parse_args()

    print("🔄 Starting automatic bulk prediction process...")

    df = load_runs()

    if df.empty:
        print("❌ No runs found to predict from.")
        return

    symbols = sorted(df["symbol"].unique())

    models = ["xgb", "rf", "cat", "lgbm", "gbr", "histgb"]

    # Automatically detect next month to predict
    all_months = pd.to_datetime(df["run_month"].dropna().unique())
    if all_months.empty:
        print("❌ No historical months available.")
        return

    latest_month = all_months.max()
    predict_month = (latest_month + pd.offsets.MonthBegin(1)).strftime("%Y-%m")

    for symbol in symbols:
        symbol_runs = df[df["symbol"] == symbol]

        if symbol_runs.empty:
            print(f"⚠️ No data for symbol: {symbol}")
            continue

        for model in models:
            print(f"🔮 Predicting {symbol} ({model}) for {predict_month}...")

            try:
                predict_optimal_config(
                    df=symbol_runs,
                    symbol=symbol,
                    predict_month=predict_month,
                    months_back=args.months_back,
                    target=args.target,
                    prediction_col=args.prediction_col,
                    prediction_error_penalty=args.prediction_error_penalty,
                    override_model=model,
                )
            except Exception as e:
                print(f"❌ Prediction failed for {symbol} ({model}): {e}")

    print("✅ Bulk prediction complete.\n")

    print("🧹 Checking for missing prediction months...")


if __name__ == "__main__":
    main()
    print("\n🧹 Checking for missing prediction months...")

    report = generate_missing_months_report(lookback_months=12)

    if report.empty:
        print("✅ No missing months detected.")
    else:
        print("⚠️ Missing months detected:")
        print(report.to_string(index=False))
