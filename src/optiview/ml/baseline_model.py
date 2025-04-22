# File: src/optiview/ml/baseline_model.py
# Purpose: Train baseline ML model to predict custom_score from input parameters

import pandas as pd
import sqlite3
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data(db_path: Path) -> pd.DataFrame:
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql("SELECT * FROM runs", conn)
    conn.close()

    # Parse params_json into columns
    df_params = pd.json_normalize(df["params_json"].apply(eval))
    df = pd.concat([df.drop(columns=["params_json"]), df_params], axis=1)

    # Ensure numeric input columns
    for col in df.columns:
        if col.startswith("input_"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["custom_score"] = pd.to_numeric(df["custom_score"], errors="coerce")
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["run_month_label"] = df["start_date"].dt.strftime("%b %Y")

    return df


def train_and_evaluate(df: pd.DataFrame) -> None:
    df = df[df["trades"] > 0]  # remove runs with 0 trades

    # Filter from April 2024 onward
    start_month = pd.to_datetime("2024-04-01")
    df = df[df["start_date"] >= start_month]

    # Feature and target selection
    features = [
        "input_LongStopLossPercent",
        "input_ShortStopLossPercent",
    ]
    target = "custom_score"

    df = df.dropna(subset=features + [target])

    # Split using last full month as test
    latest_month = df["start_date"].dt.to_period("M").max().to_timestamp()
    train_df = df[df["start_date"] < latest_month]
    test_df = df[df["start_date"] >= latest_month]

    print(f"Training on {len(train_df)} runs, testing on {len(test_df)} runs")

    X_train = train_df[features]
    y_train = train_df[target]
    X_test = test_df[features]
    y_test = test_df[target]

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    # Evaluation
    r2 = r2_score(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"R^2 Score: {r2:.3f}")
    print(f"RMSE: {rmse:.2f}\n")

    # Plot Predicted vs Actual
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=y_test, y=preds)
    plt.xlabel("Actual custom_score")
    plt.ylabel("Predicted custom_score")
    plt.title("Predicted vs Actual")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Feature Importance
    importances = model.feature_importances_
    sns.barplot(x=importances, y=features)
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    db_path = Path("db/optibatch.db")
    df = load_data(db_path)
    train_and_evaluate(df)
