# File: src/optiview/database/session.py

"""SQLAlchemy session creation utilities for OptiView database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from optiview.database.db_paths import get_optiview_db_path

# SQLAlchemy engine
# Optiview.db engine
engine_optiview = create_engine(
    f"sqlite:///{get_optiview_db_path()}",
    echo=False,  # Turn on echo=True for debugging SQL queries
    future=True,  # Modern SQLAlchemy 2.0-style behavior
)
# SQLAlchemy session factory
SessionLocalOptiview = sessionmaker(bind=engine_optiview, expire_on_commit=False, class_=Session)


def get_optiview_session() -> Session:
    """Create a new SQLAlchemy session for OptiView database.

    Returns:
        Session: SQLAlchemy ORM session.
    """
    return SessionLocalOptiview()
