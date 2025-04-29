# File: src/optiview/engine/walk_forward/time_utils.py


def get_next_month(current_month: str) -> str:
    """Given a 'YYYY-MM' month string, return the next month string."""
    year, month = map(int, current_month.split("-"))
    if month == 12:
        return f"{year+1}-01"
    else:
        return f"{year}-{month+1:02d}"
