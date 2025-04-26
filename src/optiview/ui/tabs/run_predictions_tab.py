# File: optiview/tabs/run_predictions_tab.py

import streamlit as st
import pandas as pd
from optiview.data.loader import load_runs
from optiview.engine.walk_forward.predict import predict_optimal_config
from sqlalchemy.engine import Engine
from datetime import datetime
from typing import Literal, cast

def show(engine: Engine) -> None:
    st.header("🔮 Walk-Forward Prediction Engine")

    df = load_runs()
    symbols = sorted(df["symbol"].dropna().unique())

    selected_symbol = st.selectbox("Select Symbol", symbols)
    months_for_symbol = (
        df[df["symbol"] == selected_symbol]["run_month"]
        .dropna()
        .drop_duplicates()
        .sort_values(ascending=False)
    )
    month_options = [pd.to_datetime(d).strftime("%Y-%m") for d in months_for_symbol]
    selected_month = st.selectbox("Select Month", options=month_options)

    target = cast(
        Literal["profit", "custom_score"],
        st.selectbox("Select Target Metric", ["profit", "custom_score"]),
    )

    if st.button("Run Prediction Now"):
        with st.spinner("Running prediction..."):
            predict_month = pd.to_datetime(selected_month + "-01")
            results = predict_optimal_config(
                df,
                symbol=selected_symbol,
                predict_month=predict_month,
                target=target,
            )
            st.success(f"✅ Prediction for {selected_symbol} in {selected_month} completed.")
            st.dataframe(results)