# File: src/optiview/ui/pages/04_Metrics.py

import streamlit as st
import pandas as pd
from optiview.engine.metrics import metrics_engine
from optiview.ui.utils import data_loader

st.set_page_config(page_title="Metrics View", layout="wide")
st.title("\U0001f4ca Metrics View – Alpha Performance")

st.markdown(
    "This page displays **Information Coefficient (IC)**, **Information Ratio (IR)**, and **Breadth** for a symbol across multiple models."
)

# Load prediction + evaluation data
full_df = data_loader.load_predictions_and_evaluations(strict_model_match=False)

# Derive available months and symbols from actual data
months = sorted(full_df["month"].unique(), reverse=True)
symbols = sorted(full_df["symbol"].unique())

# Select filters with defaults
month: str = st.selectbox("Select Month", months, index=0)
symbol: str = st.selectbox("Select Symbol", symbols, index=0)

# Debug panel
with st.expander("\U0001f50d Debug: Columns and Sample Rows"):
    st.write("Columns:", full_df.columns.tolist())
    st.dataframe(full_df.head())

# Dynamically detect which actual column exists
actual_col = (
    "actual_result_eval" if "actual_result_eval" in full_df.columns else "actual_result"
)

# Filter data
cross_model_df = full_df[(full_df["symbol"] == symbol) & (full_df["month"] == month)]
valid_rows = cross_model_df.dropna(subset=["predicted_profit_pred", actual_col])

# Show non-null count
st.write("Non-null count:")
st.write(valid_rows[["predicted_profit_pred", actual_col]].notnull().sum())

if not valid_rows.empty:
    predicted = valid_rows["predicted_profit_pred"]
    actual = valid_rows[actual_col]
    active_returns = actual - actual.mean()

    with st.expander("🔬 Input Check – IC Calculation"):
        st.write("Predicted Profit (first 10):", predicted.head(10).tolist())
        st.write("Actual Result (first 10):", actual.head(10).tolist())
        st.write("Predicted unique values:", predicted.nunique())
        st.write("Actual unique values:", actual.nunique())


    ic = (
        metrics_engine.calculate_ic(predicted, actual)
        if len(valid_rows) >= 2
        else float("nan")
    )
    ir = (
        metrics_engine.calculate_ir(active_returns)
        if len(valid_rows) >= 2
        else float("nan")
    )
    br = metrics_engine.calculate_breadth(valid_rows)

    # Display metrics
    st.metric(
        "📈 Information Coefficient (IC)",
        f"{ic:.3f}",
        help="Correlation between predicted and actual returns across models.",
    )
    st.metric(
        "💡 Information Ratio (IR)",
        f"{ir:.3f}",
        help="Risk-adjusted return vs mean benchmark across models.",
    )
    st.metric(
        "📊 Breadth",
        f"{br}",
        help="Number of models contributing for this symbol/month.",
    )

    # Optional: trend over time
    chart_data = []
    for m in sorted(full_df["month"].unique()):
        month_df = full_df[(full_df["symbol"] == symbol) & (full_df["month"] == m)]
        month_df = month_df.dropna(subset=["predicted_profit_pred", actual_col])

        if len(month_df) >= 2:
            ic_val = metrics_engine.calculate_ic(
                month_df["predicted_profit_pred"], month_df[actual_col]
            )
            ir_val = metrics_engine.calculate_ir(
                month_df[actual_col] - month_df[actual_col].mean()
            )
            chart_data.append({"month": m, "IC": ic_val, "IR": ir_val})

    if chart_data:
        chart_df = pd.DataFrame(chart_data).set_index("month")
        st.markdown("---")
        st.subheader("Model Performance Over Time")
        st.line_chart(chart_df)
else:
    st.warning("No valid predictions or evaluations available for this selection.")
