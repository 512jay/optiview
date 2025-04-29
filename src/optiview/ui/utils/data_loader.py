"""File: src/optiview/ui/utils/data_loader.py
Handles database access and caching.
"""

import pandas as pd
import streamlit as st

# Placeholder for database connection (adjust to your db module)
from optiview.db import query_symbols, query_months, query_models, query_predictions


@st.cache_data
def get_symbols() -> list[str]:
    """Returns available trading symbols."""
    return query_symbols()


@st.cache_data
def get_months_for_symbol(symbol: str) -> list[str]:
    """Returns available months for a given symbol."""
    return query_months(symbol)


@st.cache_data
def get_models() -> list[str]:
    """Returns available prediction models."""
    return query_models()


@st.cache_data
def load_predictions(symbol: str, month: str, model: str) -> pd.DataFrame:
    """Loads predictions for the selected symbol, month, and model."""
    return query_predictions(symbol, month, model)
