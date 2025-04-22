# File: src/optiview/engine/predict_optimal_config.py
# Purpose: Train on latest N months and predict best configs for next month

import pandas as pd
import sqlite3
from pathlib import Path
from typing import Literal
from sklearn.ensemble import RandomForestRegressor


def load_data(db_path: Path) -> pd.DataFrame:
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql("SELECT * FROM runs", conn)
    conn.close()

    df_params = pd.json_normalize(df["params_json"].apply(eval))
    df = pd.concat([df.drop(columns=["params_json"]), df_params], axis=1)

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["run_month"] = df["start_date"].dt.to_period("M").dt.to_timestamp()
    df["custom_score"] = pd.to_numeric(df["custom_score"], errors="coerce")

    for col in df.columns:
        if col.startswith("input_"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    required_cols = ["start_date", "run_month", "custom_score"] + [
            col for col in df.columns if col.startswith("input_")
        ]
    return df.dropna(subset=required_cols)


def predict_best_configs(
    df: pd.DataFrame,
    months_back: int = 3,
    top_n: int = 5,
    model_type: Literal["random_forest"] = "random_forest",
) -> pd.DataFrame:
    features = [col for col in df.columns if col.startswith("input_")]
    target = "custom_score"

    # Sort and get recent months
    months = sorted(df["run_month"].unique())
    print("Available months:", [m.strftime("%b %Y") for m in months])
    print("Required: at least", months_back + 1, "months to proceed")

    if len(months) < months_back + 1:
        raise ValueError("Not enough monthly data to predict next month")

    train_months = months[-(months_back + 1) : -1]  # e.g., last 3 full months
    test_month = months[-1]

    print("Training months:", [m.strftime("%b %Y") for m in train_months])
    print("Predicting for:", test_month.strftime("%b %Y"))

    train_df = df[df["run_month"].isin(train_months)].copy()
    test_df = df[df["run_month"] == test_month].copy()

    # Optional: filter training data
    train_df = train_df[train_df[target].notna()]

    X_train = train_df[features]
    y_train = train_df[target]
    X_test = test_df[features]

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    test_df["predicted_score"] = model.predict(X_test)

    best = test_df.sort_values("predicted_score", ascending=False).head(top_n)
    return best[["start_date", "symbol", "predicted_score"] + features]


if __name__ == "__main__":
    db_path = Path("db/optibatch.db")
    df = load_data(db_path)
    top_configs = predict_best_configs(df)
    print("\n📈 Top Configs for Next Month")
    print(top_configs.to_string(index=False))
