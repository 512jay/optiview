# File: src/optiview/ml/model_comparison.py
# Purpose: Compare different regressors for 1-month walk-forward prediction

import pandas as pd
import sqlite3
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from collections import defaultdict
from typing import Any, DefaultDict


def load_data(db_path: Path) -> pd.DataFrame:
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql("SELECT * FROM runs", conn)
    conn.close()

    # Unpack params_json
    df_params = pd.json_normalize(df["params_json"].apply(eval))
    df = pd.concat([df.drop(columns=["params_json"]), df_params], axis=1)

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["run_month"] = df["start_date"].dt.to_period("M").dt.to_timestamp()
    df["custom_score"] = pd.to_numeric(df["custom_score"], errors="coerce")

    for col in df.columns:
        if col.startswith("input_"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def try_models(df: pd.DataFrame) -> None:
    regressors: dict[str, Any] = {
        "Random Forest": RandomForestRegressor(random_state=42),
        "RidgeCV": RidgeCV(alphas=(0.1, 1.0, 10.0)),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
    }

    features = [col for col in df.columns if col.startswith("input_")]
    target = "custom_score"
    df = df.dropna(subset=features + [target])

    sorted_months: list[pd.Timestamp] = sorted(
        pd.to_datetime(df["run_month"].dropna().unique())
    )

    all_results: DefaultDict[str, dict[str, list[float | str]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for model_name, model_cls in regressors.items():
        print(f"\n🔍 Testing model: {model_name}")

        for i in range(1, len(sorted_months)):
            train_month = sorted_months[i - 1]
            test_month = sorted_months[i]

            train_df = df[df["run_month"] == train_month].copy()
            test_df = df[df["run_month"] == test_month].copy()

            # Filter low-quality training runs
            train_df = train_df[train_df[target].notna()]

            X_train = train_df[features]
            y_train = train_df[target]
            X_test = test_df[features]
            y_test = test_df[target]

            if X_train.empty or X_test.empty:
                continue

            # Apply Z-score scaling
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            model = model_cls
            model.fit(X_train_scaled, y_train)
            preds = model.predict(X_test_scaled)

            r2 = r2_score(y_test, preds)
            rmse = np.sqrt(mean_squared_error(y_test, preds))

            all_results[model_name]["month"].append(test_month.strftime("%b %Y"))
            all_results[model_name]["r2"].append(r2)
            all_results[model_name]["rmse"].append(rmse)

            print(
                f"{train_month.strftime('%b')} → {test_month.strftime('%b')} | R^2: {r2:.3f}, RMSE: {rmse:.1f}"
            )

    # Plot comparison
    for metric in ["r2", "rmse"]:
        plt.figure(figsize=(10, 4))
        for model_name, results in all_results.items():
            plt.plot(results["month"], results[metric], marker="o", label=model_name)
        plt.title(f"{metric.upper()} Over Time by Regressor")
        plt.ylabel(metric.upper())
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    db_path = Path("db/optibatch.db")
    df = load_data(db_path)
    try_models(df)
