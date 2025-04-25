# File: src/optiview/ui/queries.py

from sqlalchemy.orm import Session
from sqlalchemy import select, update
from sqlalchemy import create_engine
from optiview.data.db_path import get_optiview_db_path
from optiview.data.models import PredictedConfig, ModelType
import pandas as pd

def get_engine():
    return create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

def load_latest_top_prediction() -> dict | None:
    engine = get_engine()
    with Session(engine) as session:
        stmt = (
            select(PredictedConfig)
            .where(PredictedConfig.rank == 1)
            .order_by(PredictedConfig.month.desc())
            .limit(1)
        )
        result = session.execute(stmt).scalar_one_or_none()
        if result is None:
            return None
        return {
            "symbol": result.symbol,
            "model": result.model.value if isinstance(result.model, ModelType) else result.model,
            "predicted_profit": result.predicted_profit,
            "confidence_score": result.confidence_score,
            "quality_score": result.quality_score,
            "inputs": result.inputs,
        }

def load_predictions(symbol: str, model: str, month: str) -> pd.DataFrame:
    engine = get_engine()
    with Session(engine) as session:
        stmt = (
            select(PredictedConfig)
            .where(PredictedConfig.symbol == symbol)
            .where(PredictedConfig.model == ModelType(model))
            .where(PredictedConfig.month == month)
            .order_by(PredictedConfig.rank.asc())
        )
        rows = session.execute(stmt).scalars().all()
        if not rows:
            return pd.DataFrame()

        data = []
        for row in rows:
            data.append({
                "rank": row.rank,
                "symbol": row.symbol,
                "model": row.model.value if isinstance(row.model, ModelType) else row.model,
                "month": row.month,
                "predicted_profit": row.predicted_profit,
                "confidence_stars": row.confidence_stars,
                "quality_score": row.quality_score,
                "tags": row.tags,
                "notes": row.notes,
            })

        return pd.DataFrame(data)

def update_tags_notes(symbol: str, model: str, month: str, rank: int, tags: str, notes: str) -> None:
    engine = get_engine()
    with Session(engine) as session:
        stmt = (
            update(PredictedConfig)
            .where(PredictedConfig.symbol == symbol)
            .where(PredictedConfig.model == ModelType(model))
            .where(PredictedConfig.month == month)
            .where(PredictedConfig.rank == rank)
            .values(tags=tags, notes=notes)
        )
        session.execute(stmt)
        session.commit()
