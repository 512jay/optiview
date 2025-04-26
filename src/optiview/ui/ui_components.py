# optiview/ui_components.py
# Placeholder for shared components.
import pandas as pd


def format_month(month_str: str) -> str:
    """
    Convert '2025-03' to 'March 2025'.
    """
    try:
        return pd.to_datetime(month_str).strftime("%B %Y")
    except Exception:
        return month_str  # fallback to raw string if malformed
