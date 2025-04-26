# File: src/optiview/ui/queries.py

from typing import Optional

import pandas as pd
from sqlalchemy import create_engine, distinct, select, update
from sqlalchemy.orm import Session

from optiview.data.db_path import get_optiview_db_path
from optiview.data.models import PredictedConfig, ModelType


def get_engine():
    return create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)


def load_latest_top_prediction() -> Optional[dict]:
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
            "model": (
                result.model.value
                if isinstance(result.model, ModelType)
                else result.model
            ),
            "predicted_profit": result.predicted_profit,
            "confidence_score": result.confidence_score,
            "quality_score": result.quality_score,
            "inputs": result.inputs,
            "month": result.month,
        }


def load_predictions(symbol: str, month: str, strategy: str) -> pd.DataFrame:
    engine = get_engine()
    with Session(engine) as session:
        stmt = (
            select(PredictedConfig)
            .where(PredictedConfig.symbol == symbol)
            .where(PredictedConfig.month == month)
            .where(PredictedConfig.expert_name == strategy)
            .order_by(PredictedConfig.rank.asc())
        )
        result = session.execute(stmt).scalars().all()

        if not result:
            return pd.DataFrame()

        rows = []
        for r in result:
            rows.append(
                {
                    "symbol": r.symbol,
                    "month": r.month,
                    "model": (
                        r.model.value if isinstance(r.model, ModelType) else r.model
                    ),
                    "rank": r.rank,
                    "predicted_profit": r.predicted_profit,
                    "confidence_score": r.confidence_score,
                    "quality_score": r.quality_score,
                    "inputs": r.inputs,
                }
            )

        return pd.DataFrame(rows)


def update_tags_notes(
    symbol: str, model: str, month: str, rank: int, tags: str, notes: str
) -> None:
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


from typing import Optional, Union
import pandas as pd


def get_prediction_filter_options() -> dict[str, list[str]]:
    """
    Returns available strategies (expert_name), symbols, and months
    from the predicted_configs table.
    """
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

    with Session(engine) as session:
        strategies_raw = session.scalars(
            select(distinct(PredictedConfig.expert_name))
            .where(PredictedConfig.expert_name.is_not(None))
            .order_by(PredictedConfig.expert_name)
        ).all()

        symbols_raw = session.scalars(
            select(distinct(PredictedConfig.symbol))
            .where(PredictedConfig.symbol.is_not(None))
            .order_by(PredictedConfig.symbol)
        ).all()

        months_raw = session.scalars(
            select(distinct(PredictedConfig.month))
            .where(PredictedConfig.month.is_not(None))
            .order_by(PredictedConfig.month.desc())
        ).all()

    strategies = sorted([s for s in strategies_raw if s is not None])
    symbols = sorted([s for s in symbols_raw if s is not None])

    months = []
    for m in months_raw:
        if m is None:
            continue
        if isinstance(m, str):
            months.append(m)
        else:
            months.append(m.strftime("%Y-%m"))

    return {
        "strategies": strategies,
        "symbols": symbols,
        "months": months,
    }
