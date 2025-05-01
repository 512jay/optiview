# File: src/optiview/ui/pages/01_View_Predictions.py

"""
Detailed view of predictions for a specific symbol and month.

Allows inspection of all predicted configurations, confidence and evaluation scores,
and key input parameters, plus visual insights to assess prediction reliability.
Remembers last viewed symbol/month via session state.
"""

import streamlit as st
import pandas as pd
import altair as alt
import ast
from enum import Enum

from optiview.ui.utils.data_loader import (
    load_predictions_by_month,
    get_available_prediction_months,
    get_prediction_symbols,
    load_all_jobs,
)


def main() -> None:
    """Render the View Predictions page."""
    st.set_page_config(layout="wide")
    st.title("🔍 View Predictions by Symbol")

    all_symbols = get_prediction_symbols()
    if not all_symbols:
        st.warning("No prediction data available yet.")
        return

    default_symbol = st.session_state.get("last_selected_symbol", all_symbols[0])
    selected_symbol: str = st.selectbox(
        "Select Symbol", options=all_symbols, index=all_symbols.index(default_symbol)
    )
    st.session_state["last_selected_symbol"] = selected_symbol

    # Load months dynamically for the selected symbol
    months = get_available_prediction_months()
    if not months:
        st.warning("No available months found.")
        return

    full_df = pd.concat(
        [load_predictions_by_month(m) for m in months],
        ignore_index=True
    )
    symbol_df = full_df[full_df["symbol"] == selected_symbol].copy()

    if symbol_df.empty:
        st.info(f"No predictions found for symbol: {selected_symbol}.")
        return

    available_months = sorted(symbol_df["month"].unique(), reverse=True)
    default_month = st.session_state.get("last_selected_month", available_months[0])
    selected_month: str = st.selectbox(
        "Select Month",
        options=available_months,
        index=available_months.index(default_month),
    )
    st.session_state["last_selected_month"] = selected_month

    predictions_df = symbol_df[symbol_df["month"] == selected_month].copy()

    predictions_df = predictions_df.applymap(
        lambda x: str(x) if isinstance(x, Enum) else x
    )

    if "model" in predictions_df.columns:
        predictions_df["model"] = predictions_df["model"].astype(str)

    if "quality_score" not in predictions_df.columns:
        predictions_df["quality_score"] = "—"
    if "quality_stars" not in predictions_df.columns:
        predictions_df["quality_stars"] = "—"

    def extract_inputs(row: str) -> dict:
        try:
            parsed = ast.literal_eval(row) if isinstance(row, str) else row
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}

    extracted = predictions_df["inputs"].apply(extract_inputs).apply(pd.Series)
    for col in [
        "custom_score",
        "drawdown",
        "expected_payoff",
        "input_LongStopLossPercent",
        "input_ShortStopLossPercent",
        "result",
        "recovery_factor",
    ]:
        predictions_df[col] = extracted.get(col, "—")

    jobs_df = load_all_jobs()
    job_deposit_map = jobs_df.set_index("id")["deposit"].to_dict()
    predictions_df["deposit"] = predictions_df["job_id"].map(job_deposit_map).fillna(1000.0)

    predictions_df["bt_net_profit"] = (
        pd.to_numeric(predictions_df["result"], errors="coerce")
        - predictions_df["deposit"]
    )
    predictions_df["bt_profit_pct"] = (
        predictions_df["bt_net_profit"] / predictions_df["deposit"]
    ) * 100
    predictions_df["bt_profit_pct"] = predictions_df["bt_profit_pct"].round(2)

    st.subheader(f"Configurations for {selected_symbol} ({selected_month})")
    st.dataframe(
        predictions_df[
            [
                "predicted_profit",
                "confidence_score",
                "confidence_stars",
                "quality_score",
                "quality_stars",
                "custom_score",
                "drawdown",
                "expected_payoff",
                "input_LongStopLossPercent",
                "input_ShortStopLossPercent",
                "result",
                "deposit",
                "bt_net_profit",
                "bt_profit_pct",
                "recovery_factor",
            ]
        ].rename(
            columns={
                "predicted_profit": "Predicted Profit",
                "confidence_score": "Confidence",
                "confidence_stars": "⭐",
                "quality_score": "Evaluation",
                "quality_stars": "📊",
                "custom_score": "Custom Score",
                "drawdown": "Drawdown",
                "expected_payoff": "Expected Payoff",
                "input_LongStopLossPercent": "Long SL %",
                "input_ShortStopLossPercent": "Short SL %",
                "result": "BT Result",
                "deposit": "BT Deposit",
                "bt_net_profit": "BT Net Profit",
                "bt_profit_pct": "BT ROI %",
                "recovery_factor": "Recovery Factor",
            }
        ),
        use_container_width=True,
    )

    st.download_button(
        label="📥 Download Symbol Predictions",
        data=predictions_df.to_csv(index=False),
        file_name=f"{selected_symbol}_{selected_month}_predictions.csv",
        mime="text/csv",
    )

    st.markdown("---")
    st.subheader("📊 Visual Insights")

    st.markdown(
        "**Confidence vs Custom Score** — Higher confidence should ideally correlate with higher backtest custom score."
    )
    st.altair_chart(
        alt.Chart(predictions_df)
        .mark_circle(size=60)
        .encode(
            x="confidence_score:Q",
            y="custom_score:Q",
            tooltip=["confidence_score", "custom_score", "predicted_profit"],
        )
        .interactive()
        .properties(height=400),
        use_container_width=True,
    )

    if "bt_net_profit" in predictions_df.columns and pd.api.types.is_numeric_dtype(
        predictions_df["bt_net_profit"]
    ):
        st.markdown(
            "**Predicted Profit vs BT Net Profit** — Helps assess predictive accuracy using training-era backtest results."
        )
        st.altair_chart(
            alt.Chart(predictions_df)
            .mark_circle(size=60)
            .encode(
                x="predicted_profit:Q",
                y="bt_net_profit:Q",
                tooltip=["predicted_profit", "bt_net_profit"],
            )
            .interactive()
            .properties(height=400),
            use_container_width=True,
        )

    st.markdown(
        "**Custom Score by Long Stop Loss %** — Reveals how stop loss values influence strategy strength in backtests."
    )
    st.altair_chart(
        alt.Chart(predictions_df)
        .mark_boxplot(extent="min-max")
        .encode(x="input_LongStopLossPercent:O", y="custom_score:Q")
        .properties(height=400),
        use_container_width=True,
    )


if __name__ == "__main__":
    main()
