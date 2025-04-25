# File: src/optiview/data/models.py

from __future__ import annotations
import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import (
    String,
    Float,
    Integer,
    JSON,
    Text,
    DateTime,
    Enum,
    func,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class ModelType(enum.Enum):
    xgb = "xgb"
    rf = "rf"
    gbr = "gbr"
    histgb = "histgb"
    lgbm = "lgbm"
    cat = "cat"


class PredictedConfig(Base):
    __tablename__ = "predicted_configs"

    # --- Composite Primary Key ---
    month: Mapped[str] = mapped_column(String)  # e.g. '2025-03'
    symbol: Mapped[str] = mapped_column(String)  # e.g. 'EURUSD'
    model: Mapped[ModelType] = mapped_column(Enum(ModelType))  # e.g. 'xgb'
    rank: Mapped[int] = mapped_column()  # Rank within the top-N predictions

    __table_args__ = (PrimaryKeyConstraint("month", "symbol", "model", "rank"),)

    # --- Prediction Results ---
    predicted_profit: Mapped[float]
    confidence_score: Mapped[Optional[float]]  # 0.0 - 1.0 confidence score
    confidence_stars: Mapped[Optional[str]]  # e.g. '★★★☆☆'

    # --- Evaluation Results (post-backtest) ---
    actual_profit: Mapped[Optional[float]]  # Realized profit (if known)
    quality_score: Mapped[Optional[float]]  # Backtested quality score (if known)
    quality_stars: Mapped[Optional[str]]  # e.g. '★★★★☆'

    # --- Strategy Metadata ---
    expert_name: Mapped[Optional[str]]  # EA name (display only)
    inputs: Mapped[dict] = mapped_column(JSON)  # Input parameters as JSON
    run_id: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )  # Link to OptiBatch run

    # --- User Annotation Fields ---
    tags: Mapped[list[str]] = mapped_column(
        JSON, default=list
    )  # Arbitrary tags for filtering
    notes: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True
    )  # Notes or rationale

    # --- Audit Info ---
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
