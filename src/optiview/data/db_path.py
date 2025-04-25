# File: src/optiview/data/db_path.py
import os
from pathlib import Path


def get_optiview_db_path() -> str:
    return str(Path(__file__).parent / "optiview.db")


def get_optibatch_db_path() -> str:
    """Get the OptiBatch DB path from env var, fallback empty string."""
    return os.getenv("OPTIBATCH_DB_PATH", "")
