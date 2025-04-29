# File: src/optiview/engine/walk_forward/tuning_manager.py

"""Helper functions for managing tuning settings in the OptiView database."""

import json
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from src.optiview.database.models import TuningSettings


def get_current_utc_iso_timestamp() -> str:
    """Return the current UTC time in ISO 8601 format (Zulu)."""
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def load_latest_tuning_settings(session: Session) -> dict:
    """Load the most recent tuning settings from the database.

    Args:
        session (Session): SQLAlchemy session.

    Returns:
        dict: A dictionary with keys 'confidence', 'evaluation',
              'version_name', 'created_at', and 'notes'.

    Raises:
        ValueError: If no tuning settings exist in the database.
    """
    latest: Optional[TuningSettings] = (
        session.query(TuningSettings).order_by(TuningSettings.id.desc()).first()
    )

    if latest is None:
        raise ValueError("No tuning settings found. Please create an initial version.")

    return {
        "confidence": json.loads(latest.confidence_settings_json),
        "evaluation": json.loads(latest.evaluation_settings_json),
        "version_name": latest.version_name,
        "created_at": latest.created_at,
        "notes": latest.notes,
    }


def save_new_tuning_settings(
    session: Session,
    confidence_settings: dict,
    evaluation_settings: dict,
    version_name: str,
    notes: str = "",
) -> None:
    """Save a new version of tuning settings to the database.

    Args:
        session (Session): SQLAlchemy session.
        confidence_settings (dict): JSON-serializable confidence config.
        evaluation_settings (dict): JSON-serializable evaluation config.
        version_name (str): User-supplied label for this version.
        notes (str, optional): Additional metadata. Defaults to "".
    """
    new_settings = TuningSettings(
        created_at=get_current_utc_iso_timestamp(),
        version_name=version_name,
        notes=notes,
        confidence_settings_json=json.dumps(confidence_settings),
        evaluation_settings_json=json.dumps(evaluation_settings),
    )

    session.add(new_settings)
    session.commit()
