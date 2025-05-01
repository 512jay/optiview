# File: src/optiview/ui/pages/00_Overview.py

"""OptiView Dashboard Overview Page.

Displays a summary of predictions for the selected month,
including confidence and evaluation scores across all symbols.
Now includes filters, download button, summary metrics, and tabbed layout.
"""

import streamlit as st
import pandas as pd
import altair as alt
from typing import Optional

from optiview.ui.utils.data_loader import (
    load_predictions_by_month,
    get_available_prediction_months,
)
from optiview.engine.walk_forward.time_utils import get_current_month


def main() -> None:
    """Main function to render the Overview page."""
    st.title("\U0001f4c8 OptiView Dashboard Overview")

    st.sidebar.header("Navigation")
    available_months = get_available_prediction_months()

    if not available_months:
        st.warning("No prediction data available yet. Please run predictions first.")
        return

    selected_month: str = st.sidebar.selectbox(
        "Select Month", options=available_months, index=0
    )
    predictions_df = load_predictions_by_month(selected_month)

    if predictions_df.empty:
        st.info(f"No predictions found for {selected_month}.")
        return

    for col in ["confidence_score", "quality_score", "confidence_stars"]:
        if col not in predictions_df.columns:
            predictions_df[col] = None

    if "model" in predictions_df.columns:
        predictions_df["model"] = predictions_df["model"].astype(str)

    symbols = sorted(predictions_df["symbol"].unique())

    st.sidebar.markdown("### Filter by Symbol")
    show_all = st.sidebar.checkbox("Show all symbols", value=False)

    if show_all or len(symbols) <= 50:
        selected_symbols = st.sidebar.multiselect(
            "Select Symbols", symbols, default=symbols[:10]
        )
    else:
        top_symbols = predictions_df["symbol"].value_counts().head(30).index.tolist()
        selected_symbol = st.sidebar.selectbox("Select Top Symbol", top_symbols)
        selected_symbols = [selected_symbol]

    filtered_df = predictions_df[predictions_df["symbol"].isin(selected_symbols)]
    top_n = st.sidebar.slider(
        "Max rows in table", min_value=10, max_value=200, value=50, step=10
    )
    filtered_df = filtered_df.sort_values("predicted_profit", ascending=False).head(
        top_n
    )

    st.subheader("\U0001f4ca Summary Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Symbols Predicted", len(filtered_df["symbol"].unique()))
    col2.metric("Avg Confidence", round(filtered_df["confidence_score"].mean(), 3))
    col3.metric(
        "Avg Eval Score",
        round(filtered_df.get("quality_score", pd.Series(dtype=float)).mean(), 3),
    )

    st.download_button(
        label="\U0001f4e5 Download Predictions as CSV",
        data=filtered_df.to_csv(index=False),
        file_name=f"predictions_{selected_month}.csv",
        mime="text/csv",
    )

    tab1, tab2 = st.tabs(["\U0001f4cb Table View", "\U0001f4ca Charts"])

    with tab1:
        render_predictions_table(filtered_df)

    with tab2:
        render_confidence_chart(filtered_df)
        render_evaluation_chart(filtered_df, selected_month)


def render_predictions_table(predictions_df: pd.DataFrame) -> None:
    st.subheader("Predictions Summary")
    table_data = predictions_df.copy()

    if "quality_stars" in table_data.columns:
        table_data["Evaluation"] = table_data["quality_stars"].fillna("—")
    elif "quality_score" in table_data.columns:
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
