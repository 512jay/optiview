import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

from optiview.data.loader import load_runs
from optiview.engine.walk_forward.predict import predict_optimal_config
from typing import Literal, cast

st.set_page_config(page_title="🔮 Run Predictions", layout="wide")
st.title("🔮 Walk-Forward Prediction Engine")

# --- Load available symbols and months dynamically ---
df = load_runs(Path("optibatch.db"))
symbols = sorted(df["symbol"].dropna().unique())

selected_symbol = st.selectbox("Select Symbol", symbols)

# Filter months with data for the selected symbol
months_for_symbol = (
    df[df["symbol"] == selected_symbol]["run_month"]
    .dropna()
    .drop_duplicates()
    .sort_values(ascending=False)
)

month_options = [pd.to_datetime(d).strftime("%Y-%m") for d in months_for_symbol]

selected_month = st.selectbox("Select Month", month_options)

from typing import Literal, cast

# Choose target metric (Literal cast for mypy compliance)
target = cast(
    Literal["profit", "custom_score"],
    st.selectbox("Select Target Metric", ["profit", "custom_score"]),
)

# Run prediction button
if st.button("Run Prediction Now"):
    with st.spinner("Running prediction..."):
        predict_month = pd.to_datetime(selected_month + "-01")
        results = predict_optimal_config(
            df,
            symbol=selected_symbol,
            predict_month=predict_month,
            target=target,
        )

        st.success(
            f"✅ Prediction for {selected_symbol} in {selected_month} completed.\n\n"
            "Click on the **'streamlit app'** in the sidebar to view results."
        )

        st.dataframe(
            results[
                ["rank", "run_month", "symbol", "predicted_score"]
                + [c for c in results.columns if c.startswith("input_")]
            ]
        )
