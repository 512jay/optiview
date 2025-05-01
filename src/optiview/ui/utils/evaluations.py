# src/optiview/ui/utils/evaluations.py
# ---- evaluations.py ----
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from optiview.database.models import EvaluatedSetting
from optiview.database.db_paths import get_optiview_db_path


def load_all_evaluations() -> pd.DataFrame:
    engine: Engine = create_engine(f"sqlite:///{get_optiview_db_path()}")
    with Session(engine) as session:
        df = pd.read_sql(
            session.query(EvaluatedSetting).statement, con=session.connection()
        )
    return df


def load_evaluations_by_month(month: str) -> pd.DataFrame:
    df = load_all_evaluations()
    return df[df["month"] == month].copy()


def get_evaluation_versions() -> list[str]:
    df = load_all_evaluations()
    return sorted(df["evaluator_version"].dropna().unique())
