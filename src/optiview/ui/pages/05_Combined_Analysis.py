# File: src/optiview/ui/pages/05_Combined_Analysis.py

"""
Streamlit page for analyzing merged prediction and evaluation data.

Includes filters, delta accuracy plots, outlier detection, and confidence diagnostics.
"""

import streamlit as st
import pandas as pd
import altair as alt
from optiview.ui.utils.data_loader import load_predictions_and_evaluations


def main() -> None:
    """Display and filter combined prediction and evaluation results."""
    st.set_page_config(layout="wide")
    st.title("📊 Combined Analysis")
    st.markdown(
        "Explore merged **prediction and evaluation** results by symbol, month, and model."
    )

    df = load_predictions_and_evaluations(strict_model_match=False)

    if df.empty:
        st.warning("No combined prediction/evaluation data available.")
        return

    # Force model column to be sourced from predictions
    if "model_pred" in df.columns:
        df["model"] = df["model_pred"]

    df["model"] = df["model"].astype(str)

    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    months = sorted(df["month"].dropna().unique(), reverse=True)
    symbols = sorted(df["symbol"].dropna().unique())
    models = sorted(df["model"].dropna().unique())

    selected_month = st.sidebar.selectbox("Select Month", options=months)
    selected_symbol = st.sidebar.selectbox("Select Symbol", options=symbols)
    selected_models = st.sidebar.multiselect(
        "Select Models", options=models, default=models
    )

    # Filtered DataFrame
    filtered = df[
        (df["month"] == selected_month)
        & (df["symbol"] == selected_symbol)
        & (df["model"].isin(selected_models))
    ].copy()

    # Derived columns
    filtered["profit_error"] = pd.to_numeric(
        filtered.get("actual_result_eval", filtered.get("actual_result")),
        errors="coerce",
    ) - pd.to_numeric(filtered["predicted_profit_pred"], errors="coerce")
    filtered["abs_error"] = filtered["profit_error"].abs()

    st.subheader("📋 Filtered Table")
    st.dataframe(
        filtered[
            [
                "symbol",
                "month",
                "model",
                "rank",
                "predicted_profit_pred",
                (
                    "actual_result_eval"
                    if "actual_result_eval" in filtered.columns
                    else "actual_result"
                ),
                "profit_error",
                "abs_error",
                "confidence_score_pred",
                "confidence_stars_pred",
                "quality_score",
                "quality_stars",
            ]
        ]
        .sort_values("abs_error", ascending=False)
        .rename(
            columns={
                "predicted_profit_pred": "Predicted Profit",
                "actual_result_eval": "Actual Result",
                "confidence_score_pred": "Confidence",
                "confidence_stars_pred": "⭐",
            }
        ),
        use_container_width=True,
    )

    st.download_button(
        "📥 Download Filtered View",
        data=filtered.to_csv(index=False),
        file_name="combined_filtered.csv",
        mime="text/csv",
    )

    st.markdown("---")
    st.subheader("📊 Profit Error by Model")

    st.altair_chart(
        alt.Chart(filtered)
        .mark_bar()
        .encode(
            x=alt.X("model:N", title="Model"),
            y=alt.Y("mean(abs_error):Q", title="Mean Absolute Profit Error"),
            color="model:N",
            tooltip=["model:N", "mean(abs_error):Q"],
        )
        .properties(height=300, width=600),
        use_container_width=True,
    )

    st.markdown("---")
    st.subheader("🧠 Confidence vs Error")

    st.altair_chart(
        alt.Chart(filtered)
        .mark_circle(size=60)
        .encode(
            x="confidence_score_pred:Q",
            y="abs_error:Q",
            color="model:N",
            tooltip=[
                "model",
                "confidence_score_pred",
                "abs_error",
                "predicted_profit_pred",
                (
                    "actual_result_eval"
                    if "actual_result_eval" in filtered.columns
                    else "actual_result"
                ),
            ],
        )
        .interactive()
        .properties(height=350),
        use_container_width=True,
    )


if __name__ == "__main__":
    main()
