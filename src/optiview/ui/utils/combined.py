# src/optiview/ui/utils/combined.py
# ---- combined.py ----
import pandas as pd
from .predictions import load_all_predictions
from .evaluations import load_all_evaluations


def normalize_model_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].astype(str).str.extract(r"(\\w+)", expand=False).str.lower()
    return df


def load_predictions_and_evaluations(strict_model_match: bool = True) -> pd.DataFrame:
    preds = load_all_predictions().copy()
    evals = load_all_evaluations().copy()

    # Skip re-normalizing if already converted to strings in predictions.py
    # Just rename it safely
    preds.rename(columns={"model": "model_pred"}, inplace=True)
    evals = normalize_model_column(evals, "model")

    # Rename model in preds to model_pred BEFORE the merge
    preds.rename(columns={"model": "model_pred"}, inplace=True)

    join_keys = (
        ["month", "symbol", "model_pred", "rank"]
        if strict_model_match
        else ["month", "symbol", "rank"]
    )
    evals.rename(columns={"model": "model_eval"}, inplace=True)

    combined = pd.merge(
        preds,
        evals,
        on=join_keys,
        suffixes=("_pred", "_eval"),
        how="inner",
    )

    # For convenience in downstream UI
    combined["model"] = combined["model_pred"]

    if "actual_result" in combined.columns:
        combined = combined.rename(columns={"actual_result": "actual_result_eval"})

    return combined
