# File: src/optiview/data/loader.py

import sqlite3
import json
from pathlib import Path
import pandas as pd
from pandas import json_normalize
from typing import Any
from optiview.data.db_path import get_optibatch_db_path


def load_runs() -> pd.DataFrame:
    db_path = Path(get_optibatch_db_path())

    """
    Loads optimization run results from the OptiBatch SQLite database.

    Returns:
        pd.DataFrame: DataFrame containing runs and extracted input params.
    """

    if not db_path.exists():
        raise FileNotFoundError(f"Database not found at: {db_path}")

    conn = sqlite3.connect(str(db_path))
    try:
        df = pd.read_sql("SELECT * FROM runs", conn)
        return df
    finally:
        conn.close()


def get_quality_scores(
    symbol: str, model: str, predict_month: str, lookback: int = 3
) -> pd.DataFrame:
    """
    Fetch quality scores for a given symbol/model from predicted_configs
    where evaluation has been completed (quality_score is not null).
    """
    from sqlalchemy import select
    from sqlalchemy.orm import Session
    from optiview.data.models import PredictedConfig, ModelType
    from optiview.data.db_path import get_optiview_db_path
    from sqlalchemy import create_engine

    db_path = get_optiview_db_path()
    engine = create_engine(f"sqlite:///{db_path}", future=True)

    stmt = (
        select(
            PredictedConfig.month,
            PredictedConfig.symbol,
            PredictedConfig.model,
            PredictedConfig.quality_score,
        )
        .where(PredictedConfig.symbol == symbol)
        .where(PredictedConfig.model == ModelType(model))
        .where(PredictedConfig.quality_score.is_not(None))
        .where(PredictedConfig.month < predict_month)
        .order_by(PredictedConfig.month.desc())
        .limit(lookback)
    )

    with Session(engine) as session:
        rows = session.execute(stmt).all()
        df = pd.DataFrame(rows, columns=["month", "symbol", "model", "quality_score"])
        df["month"] = pd.to_datetime(df["month"])
        return df
