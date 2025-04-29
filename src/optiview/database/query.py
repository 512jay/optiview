# File: src/optiview/database/query.py

"""Database query utilities for OptiView."""

import pandas as pd
from sqlalchemy import create_engine, distinct
from sqlalchemy.orm import Session

from optiview.database.models import PredictedSetting, EvaluatedSetting
from optiview.database.db_paths import get_optiview_db_path


def get_predictions_for_month(month: str) -> pd.DataFrame:
    """Fetch predictions and joined evaluations for a given month.

    Args:
        month (str): Month to filter in 'YYYY-MM' format.

    Returns:
        pd.DataFrame: Predictions with optional evaluation scores.
    """
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

    with Session(engine) as session:
        preds = (
            session.query(PredictedSetting)
            .filter(PredictedSetting.month == month)
            .all()
        )
        evals = (
            session.query(EvaluatedSetting)
            .filter(EvaluatedSetting.month == month)
            .all()
        )

        pred_df = pd.DataFrame([p.__dict__ for p in preds])
        eval_df = pd.DataFrame([e.__dict__ for e in evals])

        for df in (pred_df, eval_df):
            df.drop(columns=["_sa_instance_state"], errors="ignore", inplace=True)

        if eval_df.empty:
            return pred_df

        merged = pred_df.merge(
            eval_df,
            on=["month", "symbol", "model", "rank"],
            how="left",
            suffixes=("", "_eval"),
        )

        return merged


def get_available_prediction_months() -> list[str]:
    """Return sorted months that have predictions available."""
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

    with Session(engine) as session:
        months: list = session.query(distinct(PredictedSetting.month)).all()
        months_list = [m[0] for m in months if m[0]]
        return sorted(months_list, reverse=True)
