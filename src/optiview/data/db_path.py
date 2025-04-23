# File: src/optiview/data/db_path.py

from pathlib import Path
import os


def get_db_path() -> Path:
    """
    Returns the path to the OptiView SQLite database using the OPTIVIEW_DB_PATH
    environment variable. Raises a clear error if not set or file not found.
    """
    raw = os.getenv("OPTIVIEW_DB_PATH")
    if not raw:
        raise RuntimeError("Environment variable OPTIVIEW_DB_PATH is not set.")
    path = Path(raw)
    if not path.exists():
        raise FileNotFoundError(f"Database not found at: {path}")
    return path
