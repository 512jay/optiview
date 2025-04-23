# 📁 src/optiview/engine/walk_forward/predict.py
"""
This script predicts optimal input parameters for a trading strategy
based on previous optimization runs.

📌 What this script does:
- Loads prior MT5 optimization data.
- Trains a machine learning regressor to learn how inputs (e.g., StopLoss%) affect performance.
- Predicts the best parameter combos for the next month using a selected model (default: XGBoost).
- Saves results to CSV and exports a ready-to-test INI config file.

🧠 Supported models:
- XGBoost (xgb): Great for non-linear data and highly performant.
- Random Forest (rf): Robust and interpretable.
- Gradient Boosting (gbr): Slower but accurate.
- Histogram Gradient Boosting (histgb): Fast, scikit-learn native.
- LightGBM (lgbm): Fast with large datasets.
- CatBoost (cat): Good for categorical data.

🛠️ Model selection:
Use `--model rf` to try Random Forest or leave default as `xgb`.
"""

from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
)
from pathlib import Path
from typing import Literal, Optional, Any
import pandas as pd
from sklearn.preprocessing import StandardScaler
from optiview.data.loader import load_runs
from optiview.engine.walk_forward.export_ini import export_ini_file
import argparse

# These are all the machine learning regressors we support
SUPPORTED_MODELS: dict[str, type] = {
    "xgb": XGBRegressor,  # XGBoost (high performance gradient boosting)
    "rf": RandomForestRegressor,  # Random Forest (bagging ensemble)
    "gbr": GradientBoostingRegressor,  # Standard scikit-learn gradient boosting
    "histgb": HistGradientBoostingRegressor,  # Fast histogram-based boosting
    "lgbm": LGBMRegressor,  # LightGBM (efficient, great with large datasets)
    "cat": CatBoostRegressor,  # CatBoost (great with categorical data)
}


def estimate_confidence(
    quality_scores_df: pd.DataFrame,
    symbol: str,
    model: str,
    predict_month: pd.Timestamp,
    lookback: int = 3,
) -> int:
    quality_scores_df["month"] = pd.to_datetime(quality_scores_df["month"])
    cutoff = predict_month - pd.offsets.MonthBegin(1)

    recent = (
        quality_scores_df[
            (quality_scores_df["symbol"] == symbol)
            & (quality_scores_df["model"] == model)
            & (quality_scores_df["month"] < predict_month)
        ]
        .sort_values("month", ascending=False)
        .head(lookback)
    )

    if recent.empty:
        return 1

    avg_quality = recent["quality_score"].mean()

    # Adjusted mapping for more realistic distribution
    if avg_quality >= 0.35:
        return 5
    elif avg_quality >= 0.32:
        return 4
    elif avg_quality >= 0.30:
        return 3
    elif avg_quality >= 0.28:
        return 2
    else:
        return 1


def get_model(model_name: str) -> Any:
    """Helper function to instantiate a regressor model with appropriate arguments."""
    if model_name not in SUPPORTED_MODELS:
        raise ValueError(f"Unsupported model: {model_name}")

    ModelClass = SUPPORTED_MODELS[model_name]
    extra_args: dict[str, Any] = {}

    # Add model-specific parameters
    if model_name == "xgb":
        extra_args = {
            "learning_rate": 0.1,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "verbosity": 0,
        }
    elif model_name == "cat":
        extra_args = {"verbose": False}
    elif model_name == "lgbm":
        extra_args = {
            "verbosity": -1,
        }

    # Common arguments
    common_args: dict[str, Any] = {
        "max_depth": 4,
        "random_state": 42,
    }

    if model_name in {"xgb", "rf", "gbr", "lgbm"}:
        common_args["n_estimators"] = 100
    elif model_name == "histgb":
        common_args["max_iter"] = 100

    if model_name in {"xgb", "rf", "lgbm"}:
        common_args["n_jobs"] = -1

    return ModelClass(**common_args, **extra_args)


def save_prediction_outputs(
    df: pd.DataFrame,
    symbol: str,
    model_name: str,
    predict_month: pd.Timestamp,
    output_base: Path,
    overwrite: bool,
) -> None:
    out_dir = output_base / predict_month.strftime("%Y-%m") / symbol / model_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "prediction_summary.parquet"

    if not overwrite and out_csv.exists():
        print(
            f"⏩ Skipping {symbol} {predict_month.strftime('%Y-%m')} ({model_name}) — already exists."
        )
        return

    export_ini_file(df, out_dir)

    df.to_parquet(out_csv, index=False)
    print(f"✅ Saved prediction: {out_csv}")

def prepare_train_test_split(
    df: pd.DataFrame,
    symbol: str,
    predict_month: Optional[pd.Timestamp],
    months_back: int,
    target: str,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    df = df[df["symbol"] == symbol].copy()
    df["run_month"] = pd.to_datetime(df["run_month"])
    months = sorted(df["run_month"].dropna().unique())

    if predict_month is None:
        train_months = months[-(months_back + 1):-1]
        predict_month = months[-1]
    else:
        idx = months.index(predict_month)
        train_months = months[max(0, idx - months_back):idx]

    features = [col for col in df.columns if col.startswith("input_")]
    train_df = df[df["run_month"].isin(train_months) & df[target].notna()]
    test_df = df[df["run_month"] == predict_month]
    test_df = test_df[test_df[features].notna().all(axis=1)]

    # Remove duplicate columns in test_df
    test_df = test_df.loc[:, ~test_df.columns.duplicated()]

    return train_df, test_df, features


def predict_optimal_config(
    df: pd.DataFrame,
    predict_month: pd.Timestamp,
    months_back: int = 1,
    symbol: str = "EURUSD",
    target: Literal["profit", "custom_score"] = "profit",
    top_n: int = 3,
    output_base: Path = Path("generated/predictions"),
    override_model: Optional[str] = None,
    overwrite: bool = False,
) -> pd.DataFrame:  # 1. Prepare training and test datasets
    train_df, test_df, features = prepare_train_test_split(df, symbol, predict_month, months_back, target)

    if train_df.empty or test_df.empty:
        print(f"⚠️ Skipping {symbol} for {predict_month.strftime('%Y-%m')} — no usable data")
        return pd.DataFrame()

    # 2. Train model
    model_name = override_model or "xgb"
    model = get_model(model_name)

    X_train, y_train = train_df[features], train_df[target]
    X_test = test_df[features]

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model.fit(X_train_scaled, y_train)

    # 3. Generate predictions
    test_df["predicted_profit"] = model.predict(X_test_scaled)

    # 4. Select top configs
    top_configs = (
        test_df.sort_values("predicted_profit", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    top_configs.insert(0, "rank", top_configs.index + 1)

    # 5. Estimate and attach confidence stars
    from pathlib import Path

    # Load prior model quality scores
    quality_file = Path("generated/predictions/quality_scores.csv")
    if quality_file.exists():
        quality_df = pd.read_csv(quality_file, parse_dates=["month"])
    else:
        quality_df = pd.DataFrame(columns=["month", "symbol", "model", "quality_score"])

    confidence = estimate_confidence(
        quality_scores_df=quality_df,
        symbol=symbol,
        model=model_name,
        predict_month=predict_month,
    )

    top_configs["confidence_stars"] = "★" * confidence + "☆" * (5 - confidence)

    cols = list(top_configs.columns)
    if "predicted_profit" in cols and "confidence_stars" in cols:
        i = cols.index("predicted_profit")
        cols = (
            cols[: i + 1]
            + ["confidence_stars"]
            + [
                col
                for col in cols
                if col not in {"confidence_stars"} or col == "predicted_profit"
            ]
        )
        top_configs = top_configs[cols]

    # Final deduplication before saving
    top_configs = top_configs.loc[:, ~top_configs.columns.duplicated()]

    # 6. Add placeholders for evaluation and write output
    save_prediction_outputs(top_configs, symbol, model_name, predict_month, output_base, overwrite)

    return top_configs


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run month-ahead predictions.")
    parser.add_argument(
        "--month",
        type=str,
        required=True,
        help="Training month in YYYY-MM format (e.g. 2025-02)",
    )
    parser.add_argument(
        "--symbol",
        type=str,
        default=None,
        help="Optionally restrict to a single symbol (e.g. GBPUSD)",
    )
    parser.add_argument(
        "--target",
        type=str,
        choices=["profit", "custom_score"],
        default="profit",
        help="Which target to predict: profit (default) or custom_score",
    )
    parser.add_argument(
        "--model",
        choices=SUPPORTED_MODELS.keys(),
        default="xgb",
        help="Model to use for prediction",
    )

    args = parser.parse_args()

    df = load_runs(Path("optibatch.db"))
    predict_month = pd.to_datetime(args.month + "-01")
    symbols = df["symbol"].dropna().unique()

    for symbol in symbols:
        if args.symbol and symbol != args.symbol:
            continue

        print(f"\n🔮 Predicting for {symbol}...")
        top = predict_optimal_config (
            df,
            symbol=symbol,
            predict_month=predict_month,
            target=args.target,
            override_model=args.model,
        )
        if top.empty:
            print(f"⚠️ No predictions available for {symbol} in {args.month}.")
            continue
        print(
            top[
                ["rank", "run_month", "symbol", "predicted_profit"]
                + [c for c in top.columns if c.startswith("input_")]
            ]
        )
