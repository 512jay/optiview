# File: src/optiview/ui/utils/data_loader.py

"""Handles database access and caching for the Streamlit UI."""

import pandas as pd
import streamlit as st

from optiview.database.query import (
    get_predictions_for_month,
    get_available_prediction_months,
)


@st.cache_data
def load_predictions_for_month(month: str) -> pd.DataFrame:
    """Load predictions and evaluations for a month.

    Args:
        month (str): Month to load.

    Returns:
        pd.DataFrame: Joined predictions + evaluations.
    """
    return get_predictions_for_month(month)


@st.cache_data
def load_available_prediction_months() -> list[str]:
    """Load available prediction months.

    Returns:
        list[str]: List of months in 'YYYY-MM' format.
    """
    return get_available_prediction_months()
