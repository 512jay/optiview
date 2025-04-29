# File: src/optiview/engine/walk_forward/time_utils.py

"""Utility functions for handling month-based time logic in OptiView.

All functions use string-based months in the format 'YYYY-MM'.
Avoids datetime objects for application-layer consistency.
"""

from datetime import datetime


def get_next_month(current_month: str) -> str:
    """Return the next calendar month given a 'YYYY-MM' string.

    Args:
        current_month (str): A string in 'YYYY-MM' format (e.g., '2025-04').

    Returns:
        str: The next month in 'YYYY-MM' format (e.g., '2025-05').
    """
    year, month = map(int, current_month.split("-"))
    if month == 12:
        return f"{year+1}-01"
    return f"{year}-{month+1:02d}"


def get_current_month() -> str:
    """Return the current month as a 'YYYY-MM' string in UTC.

    Returns:
        str: The current calendar month (e.g., '2025-04').
    """
    now = datetime.utcnow()
    return f"{now.year}-{now.month:02d}"
