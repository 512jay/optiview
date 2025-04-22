# File: src/optiview/ml/walk_forward_model.py
# Purpose: Train month-by-month walk-forward models to predict custom_score

import pandas as pd
import sqlite3
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


def load_data(db_path: Path) -> pd.DataFrame:
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql("SELECT * FROM runs", conn)
    conn.close()

    # Parse JSON inputs
    df_params = pd.json_normalize(df["params_json"].apply(eval))
    df = pd.concat([df.drop(columns=["params_json"]), df_params], axis=1)

    # Ensure datetime and numeric columns
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["run_month_label"] = df["start_date"].dt.strftime("%b %Y")
    df["run_month"] = df["start_date"].dt.to_period("M").dt.to_timestamp()
    df["custom_score"] = pd.to_numeric(df["custom_score"], errors="coerce")

    for col in df.columns:
        if col.startswith("input_"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def walk_forward_model(df: pd.DataFrame) -> None:
    features = [col for col in df.columns if col.startswith("input_")]
    target = "custom_score"
    df = df.dropna(subset=features + [target])

    sorted_months: list[pd.Timestamp] = sorted(
        pd.to_datetime(df["run_month"].dropna().unique())
    )

    results = defaultdict(list)

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

        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        r2 = r2_score(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))

        results["month"].append(test_month.strftime("%b %Y"))
        results["r2"].append(r2)
        results["rmse"].append(rmse)

        print(
            f"{train_month.strftime('%b %Y')} → {test_month.strftime('%b %Y')} | R^2: {r2:.3f}, RMSE: {rmse:.1f}"
        )

    # Plot results
    plt.figure(figsize=(10, 4))
    plt.plot(results["month"], results["r2"], marker="o")
    plt.title("R^2 Score Over Time (Filtered Training)")
    plt.ylabel("R^2 Score")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(results["month"], results["rmse"], marker="o", color="orange")
    plt.title("RMSE Over Time (Filtered Training)")
    plt.ylabel("RMSE")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    db_path = Path("db/optibatch.db")
    df = load_data(db_path)
    walk_forward_model(df)
