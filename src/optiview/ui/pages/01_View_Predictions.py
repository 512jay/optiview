"""File: src/optiview/ui/pages/01_View_Predictions.py
View and filter predictions by symbol, month, and model.
"""

import streamlit as st
from optiview.ui.utils.data_loader import (
    get_symbols,
    get_months_for_symbol,
    get_models,
    load_predictions,
)
import pandas as pd

st.set_page_config(page_title="View Predictions", layout="wide")


def main() -> None:
    """Main function for the View Predictions page."""
    st.header("🔍 View Predictions")

    # Load dropdown options
    symbols: list[str] = get_symbols()
    selected_symbol: str | None = st.selectbox("Select Symbol", symbols)

    if selected_symbol:
        months: list[str] = get_months_for_symbol(selected_symbol)
        selected_month: str | None = st.selectbox("Select Month", months)

        models: list[str] = get_models()
        selected_model: str | None = st.selectbox("Select Model", models)

        if selected_month and selected_model:
            predictions: pd.DataFrame = load_predictions(
                selected_symbol, selected_month, selected_model
            )

            if not predictions.empty:
                st.dataframe(predictions)
            else:
                st.info("No predictions found for the selected criteria.")


if __name__ == "__main__":
    main()
