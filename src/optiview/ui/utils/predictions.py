# src/optiview/ui/utils/predictions.py
# ---- predictions.py ----
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, distinct
from sqlalchemy.engine import Engine
from optiview.database.models import PredictedSetting
from optiview.database.db_paths import get_optiview_db_path


def get_available_prediction_months() -> list[str]:
    """Return sorted months that have predictions available."""
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)
    with Session(engine) as session:
        months: list = session.query(distinct(PredictedSetting.month)).all()
        return sorted([m[0] for m in months if m[0]], reverse=True)


def load_all_predictions() -> pd.DataFrame:
    engine: Engine = create_engine(f"sqlite:///{get_optiview_db_path()}")
    with Session(engine) as session:
        df = pd.read_sql(
            session.query(PredictedSetting).statement, con=session.connection()
        )

    # Fix: convert model Enum to raw string (e.g., 'xgb')
    if "model" in df.columns and df["model"].dtype == object:
        df["model"] = df["model"].apply(
            lambda m: m.value if hasattr(m, "value") else str(m)
        )

    return df


def load_predictions_by_month(month: str) -> pd.DataFrame:
    df = load_all_predictions()
    return df[df["month"] == month].copy()


def get_prediction_symbols() -> list[str]:
    df = load_all_predictions()
    return sorted(df["symbol"].unique())
