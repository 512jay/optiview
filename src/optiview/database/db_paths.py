# File: src/optiview/database/db_paths.py

"""Provides database paths for OptiView and OptiBatch."""

from pathlib import Path
import os


def get_optiview_db_path() -> Path:
    """Return the OptiView database path."""
    return Path(__file__).parent / "optiview.db"


def get_optibatch_db_path() -> Path:
    """Get the OptiBatch DB path from environment variable."""
    return Path(os.getenv("OPTIBATCH_DB_PATH", ""))

