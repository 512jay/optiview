# File: src/optiview/ui/pages/00_Overview.py

"""OptiView Dashboard Overview Page.

Displays a summary of predictions for the selected month,
including confidence and evaluation scores across all symbols.
"""

import streamlit as st
import pandas as pd
import altair as alt
from typing import Optional

from optiview.ui.utils.data_loader import (
    load_predictions_for_month,
    load_available_prediction_months,
)
from optiview.engine.walk_forward.time_utils import get_current_month


def main() -> None:
    """Main function to render the Overview page."""
    st.title("📈 OptiView Dashboard Overview")

    st.sidebar.header("Navigation")
    available_months = load_available_prediction_months()

    if not available_months:
        st.warning("No prediction data available yet. Please run predictions first.")
        return

    selected_month: str = st.sidebar.selectbox(
        "Select Month", options=available_months, index=0
    )

    predictions_df = load_predictions_for_month(selected_month)

    if predictions_df.empty:
        st.info(f"No predictions found for {selected_month}.")
        return

    render_predictions_table(predictions_df)
    render_confidence_chart(predictions_df)
    render_evaluation_chart(predictions_df, selected_month)


def render_predictions_table(predictions_df: pd.DataFrame) -> None:
    """Render the main predictions overview table.

    Args:
        predictions_df (pd.DataFrame): DataFrame of predictions for the selected month.
    """
    st.subheader("Predictions Summary")

    table_data = predictions_df.copy()

    if "quality_score" in table_data.columns:
        table_data["Evaluation"] = table_data["quality_score"].fillna("—")
    else:
        table_data["Evaluation"] = "—"
        st.info("Evaluation scores not found in prediction data.")

    st.dataframe(
        table_data[
            ["symbol", "predicted_profit", "confidence_stars", "Evaluation"]
        ].rename(
            columns={
                "symbol": "Symbol",
                "predicted_profit": "Predicted Profit",
                "confidence_stars": "Confidence",
            }
        ),
        hide_index=True,
    )


def render_confidence_chart(predictions_df: pd.DataFrame) -> None:
    """Render a bar chart showing average confidence score by symbol.

    Args:
        predictions_df (pd.DataFrame): DataFrame of predictions.
    """
    st.subheader("Confidence Levels by Symbol")

    confidence_chart = (
        alt.Chart(predictions_df)
        .mark_bar()
        .encode(
            x="symbol:N", y="confidence_score:Q", tooltip=["symbol", "confidence_score"]
        )
        .properties(height=400)
    )
    st.altair_chart(confidence_chart, use_container_width=True)


def render_evaluation_chart(predictions_df: pd.DataFrame, selected_month: str) -> None:
    """Render a bar chart showing average evaluation score by symbol.

    Args:
        predictions_df (pd.DataFrame): DataFrame of predictions.
        selected_month (str): The selected month (format 'YYYY-MM').
    """
    st.subheader("Evaluation Scores by Symbol")

    current_month = get_current_month()

    if "quality_score" not in predictions_df.columns:
        return

    evaluation_data = predictions_df.dropna(subset=["quality_score"])

    if evaluation_data.empty:
        if selected_month < current_month:
            st.warning(f"No evaluation scores available for {selected_month}.")
        return

    evaluation_chart = (
        alt.Chart(evaluation_data)
        .mark_bar()
        .encode(x="symbol:N", y="quality_score:Q", tooltip=["symbol", "quality_score"])
        .properties(height=400)
    )
    st.altair_chart(evaluation_chart, use_container_width=True)


if __name__ == "__main__":
    main()
