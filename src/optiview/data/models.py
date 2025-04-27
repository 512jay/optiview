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


class PredictedSetting(Base):
    __tablename__ = "predicted_settings"

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


class EvaluatedSetting(Base):
    """Evaluation results linked to a predicted configuration."""

    __tablename__ = "evaluated_settings"

    # --- Primary Key ---
    id: Mapped[int] = mapped_column(primary_key=True)

    # --- Link to Prediction ---
    month: Mapped[str] = mapped_column(String)  # Redundant for easy JOINs
    symbol: Mapped[str] = mapped_column(String)
    model: Mapped[ModelType] = mapped_column(Enum(ModelType))
    rank: Mapped[int] = mapped_column()

    # --- Evaluation Version Info ---
    evaluator_version: Mapped[str] = mapped_column(
        String
    )  # e.g. 'baseline_v1', 'v2_experiment'

    # --- Evaluation Metrics ---
    quality_score: Mapped[Optional[float]]  # Final backtested quality
    quality_stars: Mapped[Optional[str]]  # e.g. '★★★☆☆'
    confidence_score: Mapped[Optional[float]]  # Predicted confidence at eval time
    confidence_stars: Mapped[Optional[str]]  # e.g. '★★★★☆'

    # --- Metadata ---
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # Human notes
    metrics_json: Mapped[Optional[dict]] = mapped_column(
        JSON, nullable=True
    )  # Future metrics

    # --- Audit Info ---
    evaluated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    __table_args__ = (PrimaryKeyConstraint("id"),)
