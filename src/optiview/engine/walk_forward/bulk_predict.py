# 📁 src/optiview/engine/walk_forward/bulk_predict.py

import argparse
import pandas as pd
from pathlib import Path
from optiview.engine.walk_forward.predict import (
    predict_optimal_config,
    SUPPORTED_MODELS,
)
from optiview.data.loader import load_runs


def main() -> None:
    # CLI args: allow overwrite of existing predicted configs
    parser = argparse.ArgumentParser(
        description="Run walk-forward predictions for all models."
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Force overwrite of existing predicted configs.",
    )
    args = parser.parse_args()

    # Load the full optimization dataset
    df = load_runs(Path("optibatch.db"))
    symbols = df["symbol"].dropna().unique()
    months = sorted(df["run_month"].dropna().unique())

    # Skip the final month since we don't have future data for evaluation
    predictable_months = months[1:]

    for model_name in SUPPORTED_MODELS.keys():
        print(f"\n📦 MODEL: {model_name.upper()}")

        for month in predictable_months:
            month_str = pd.to_datetime(month).strftime("%Y-%m")
            for symbol in symbols:
                print(f"🔮 Predicting: {symbol} for {month_str} ...")

                try:
                    predict_optimal_config(
                        df,
                        symbol=symbol,
                        predict_month=pd.to_datetime(month_str + "-01"),
                        target="profit",
                        override_model=model_name,
                        overwrite=args.overwrite,
                    )
                except Exception as e:
                    print(f"❌ Failed: {symbol} {month_str} ({model_name}) → {e}")


if __name__ == "__main__":
    main()
