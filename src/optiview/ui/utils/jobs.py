# src/optiview/ui/utils/jobs.py
# ---- jobs.py ----
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from sqlalchemy.engine import Engine
from optiview.database.models import SyncedJob
from optiview.database.db_paths import get_optiview_db_path


def load_all_jobs() -> pd.DataFrame:
    engine: Engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)
    with Session(engine) as session:
        df = pd.read_sql(select(SyncedJob), con=session.connection())
    return df


def get_job_metadata(job_id: str) -> dict:
    df = load_all_jobs()
    row = df[df["id"] == job_id]
    return row.to_dict("records")[0] if not row.empty else {}
