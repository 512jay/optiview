# File: src/optiview/engine/walk_forward/bulk_predict.py

"""Bulk prediction engine for OptiView: scalable to 10M+ runs."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List

import pandas as pd

from optiview.engine.walk_forward.predict import predict_optimal_config
from optiview.engine.walk_forward.time_utils import get_next_month
from optiview.database.loader import get_all_symbols, load_symbol_months_runs


# --- Helper Functions ---


def load_target_symbols() -> list[str]:
    """Load list of target symbols to predict for.

    Returns:
        List of symbols. If 'predict_symbols.txt' exists, uses it.
        Otherwise loads all symbols available in database.
    """
    file_path = Path("scripts/database/predict_symbols.txt")
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            symbols = [line.strip() for line in f if line.strip()]
        print(f"✅ Loaded {len(symbols)} symbols from predict_symbols.txt")
        return symbols
    else:
        print(
            "ℹ️ No predict_symbols.txt found — scanning available symbols from OptiBatch runs."
        )
        return get_all_symbols()


def get_available_months_for_symbol(symbol: str) -> list[str]:
    """Get list of months that have completed backtests for a symbol.

    Args:
        symbol: The trading symbol.

    Returns:
        Sorted list of months (YYYY-MM) that have data.
    """
    df = load_symbol_months_runs(symbol, [])
    if df.empty:
        return []
    return sorted(df["run_month"].dropna().unique())


def get_previous_months(
    all_months: list[str],
    target_month: str,
    months_back: int,
) -> list[str]:
    """Get previous months for training, even if the target month is not in available months.

    This function computes the training window by selecting the `months_back` months
    immediately preceding the `target_month`. If `target_month` is not present in
    `all_months`, it is assumed to be the next chronological month after the last
    entry in `all_months`.

    Args:
        all_months (list[str]): Chronologically sorted list of available months (format: YYYY-MM).
        target_month (str): The month to predict for (format: YYYY-MM).
        months_back (int): The number of prior months to use for training.

    Returns:
        list[str]: A list of previous months to use for training. Returns an empty list
        if there are insufficient historical months available.
    """
    if target_month in all_months:
        target_idx = all_months.index(target_month)
    else:
        target_idx = len(all_months)

    if target_idx < months_back:
        return []

    return all_months[target_idx - months_back : target_idx]


def validate_months_window(
    training_months: list[str], available_months: list[str]
) -> bool:
    """Ensure that all months in the training window actually exist.

    Args:
        training_months: Months we want to use for training.
        available_months: All months we have data for.

    Returns:
        True if valid, False if any months missing.
    """
    missing = [m for m in training_months if m not in available_months]
    if missing:
        print(f"⚠️ Missing months in training window: {missing}. Skipping prediction.")
        return False
    return True


# --- Main Prediction Runner ---


def bulk_predict(full_history: bool = False, months_back: int = 3) -> None:
    """Bulk predict optimal configurations for multiple symbols and months.

    Args:
        full_history: If True, predict for all historical months possible.
                      If False, predict for the next upcoming month only.
        months_back: How many previous months to use when training the model.
    """
    print("🔄 Starting bulk prediction process...")

    symbols = load_target_symbols()

    for symbol in symbols:
        print(f"\n🔎 Processing symbol: {symbol}")

        available_months = get_available_months_for_symbol(symbol)
        if len(available_months) <= months_back:
            print(f"⚠️ Not enough historical months for {symbol}. Skipping.")
            continue

        # Determine which months to predict
        if full_history:
            target_months = available_months[months_back:]
        else:
            latest_month = available_months[-1]
            next_month = get_next_month(latest_month)
            target_months = [next_month]

        for predict_month in target_months:
            # Build training window
            training_months = get_previous_months(
                available_months, predict_month, months_back
            )
            if not training_months:
                print(
                    f"⚠️ Not enough training months for {symbol} {predict_month}. Skipping."
                )
                continue

            if not validate_months_window(training_months, available_months):
                continue

            months_to_load = training_months + [predict_month]
            runs_df = load_symbol_months_runs(symbol, months_to_load)

            if runs_df.empty:
                print(f"⚠️ No runs loaded for {symbol} in {months_to_load}. Skipping.")
                continue

            # Predict across all supported models
            for model in ["xgb", "rf", "cat", "lgbm", "gbr", "histgb"]:
                try:
                    print(f"🔮 Predicting {symbol} {predict_month} ({model})...")
                    predict_optimal_config(
                        df=runs_df,
                        symbol=symbol,
                        predict_month=predict_month,
                        months_back=months_back,
                        override_model=model,
                    )
                except Exception as e:
                    print(
                        f"❌ Prediction failed for {symbol} {predict_month} ({model}): {e}"
                    )

    print("\n✅ Bulk prediction complete.")


if __name__ == "__main__":
    # Allow CLI usage: python bulk_predict.py --full-history
    full_history_flag = "--full-history" in sys.argv
    bulk_predict(full_history=full_history_flag)
