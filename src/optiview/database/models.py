# File: src/optiview/database/models.py

"""
Database models for the OptiView project.

Includes predicted settings, evaluated results, synced jobs, and tuning metadata.
Adheres to PEP 8, PEP 257, and uses SQLAlchemy 2.0 typing style.
"""

from datetime import datetime
from typing import Optional, Any
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Text,
    JSON,
    DateTime,
    Enum,
    PrimaryKeyConstraint,
    UniqueConstraint,
    MetaData,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
import enum

# --- SQLAlchemy Base ---
metadata = MetaData()


class Base(DeclarativeBase):
    metadata = metadata


# --- Enum for model types ---
class ModelType(enum.Enum):
    xgb = "xgb"
    rf = "rf"
    gbr = "gbr"
    histgb = "histgb"
    lgbm = "lgbm"
    cat = "cat"


# --- Prediction Results ---
class PredictedSetting(Base):
    """Machine learning predictions for a specific symbol and month."""

    __tablename__ = "predicted_settings"

    # Composite key per prediction
    month: Mapped[str] = mapped_column(String)
    symbol: Mapped[str] = mapped_column(String)
    model: Mapped[ModelType] = mapped_column(Enum(ModelType))
    rank: Mapped[int] = mapped_column(Integer)

    __table_args__ = (PrimaryKeyConstraint("month", "symbol", "model", "rank"),)

    version: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    predicted_profit: Mapped[float]
    confidence_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    confidence_stars: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Serialized configuration
    inputs: Mapped[dict] = mapped_column(JSON)
    params_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    # Run metadata
    run_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    job_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    predicted_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # User-defined annotations
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )


# --- Evaluation Results ---
class EvaluatedSetting(Base):
    """Stores actual performance for predicted configurations and scoring metadata."""

    __tablename__ = "evaluated_settings"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Prediction reference
    month: Mapped[str] = mapped_column(String)
    symbol: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    rank: Mapped[int] = mapped_column(Integer)
    evaluator_version: Mapped[str] = mapped_column(String)

    # Scoring outputs
    quality_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    quality_stars: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    confidence_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    confidence_stars: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Result values
    actual_result: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    predicted_profit: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    matched_run_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    matched_job_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    evaluated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Optional info
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    metrics_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint("id"),
        UniqueConstraint(
            "month",
            "symbol",
            "model",
            "rank",
            "evaluator_version",
            name="uq_evaluated_config_versioned",
        ),
    )


# --- Synced Jobs from OptiBatch ---
class SyncedJob(Base):
    """Lightweight mirror of OptiBatch jobs with metadata and tester inputs."""

    __tablename__ = "synced_jobs"

    id: Mapped[str] = mapped_column(primary_key=True)
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


# --- Tuning Configurations ---
class TuningSettings(Base):
    """Stores versioned scoring logic and confidence weighting rules."""

    __tablename__ = "tuning_settings"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[str] = mapped_column(
        String, nullable=False
    )  # ISO8601 UTC timestamp
    version_name: Mapped[str] = mapped_column(String, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    confidence_settings_json: Mapped[str] = mapped_column(Text, nullable=False)
    evaluation_settings_json: Mapped[str] = mapped_column(Text, nullable=False)
