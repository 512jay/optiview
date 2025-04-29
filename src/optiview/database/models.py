# File: src/optiview/database/models.py

from __future__ import annotations
import enum
from datetime import datetime
from typing import Optional, Any
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
    Column,
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
    version = Column(String, nullable=True)

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

    # --- Machine Learning training data ---
    params_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)


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


class SyncedJob(Base):
    """Lightweight mirror of relevant fields from OptiBatch jobs table."""

    __tablename__ = "synced_jobs"

    id: Mapped[str] = mapped_column(primary_key=True)  # job_id
    expert_name: Mapped[str]
    expert_path: Mapped[str]
    period: Mapped[str]
    deposit: Mapped[float]
    currency: Mapped[str]
    leverage: Mapped[str]
    model: Mapped[Optional[str]] = mapped_column(nullable=True)
    optimization_mode: Mapped[Optional[str]] = mapped_column(nullable=True)
    optimization_criterion: Mapped[Optional[str]] = mapped_column(nullable=True)
    tester_inputs: Mapped[dict[str, Any]] = mapped_column(JSON)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
