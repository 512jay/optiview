# File: src/optiview/ui/OptiView.py

import streamlit as st
from optiview.ui.queries import (
    load_latest_top_prediction,
    load_predictions,
    update_tags_notes,
)
import pandas as pd

st.set_page_config(page_title="OptiView", layout="wide")

def render_confidence_stars(score: float | None) -> str:
    if score is None:
        return "—"
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)

def show_top_recommendation():
    st.header("🔮 Most Recommended Trade (Latest Month)")
    latest = load_latest_top_prediction()
    if latest is None:
        st.info("No recommendations available yet.")
        return

    st.subheader(f"Symbol: {latest['symbol']} | Model: {latest['model']}")
    st.metric("Predicted Profit", f"${latest['predicted_profit']:.2f}")
    st.write(f"Confidence: {render_confidence_stars(latest['confidence_score'])}")

    qs = latest.get("quality_score")
    st.write(f"Quality Score: {qs:.2f}" if qs is not None else "Quality Score: —")

    st.markdown("**Recommended Settings:**")
    st.json(latest["inputs"] or {})

    st.button("📋 Explore More Predictions")  # Non-functional, no tab switch

def explore_predictions_ui():
    st.header("📋 Explore Predictions")

    symbol = st.selectbox("Symbol", options=["EURUSD", "GBPUSD"])
    model = st.selectbox("Model", options=["xgb", "rf", "gbr", "histgb", "lgbm", "cat"])
    month = st.text_input("Month (YYYY-MM)", value="2025-03")

    if st.button("Load Predictions"):
        df = load_predictions(symbol=symbol, model=model, month=month)
        if df.empty:
            st.warning("No predictions found.")
        else:
            st.dataframe(df)

# Static tabs
tab1, tab2 = st.tabs(["🏠 Top Recommendation", "📋 Explore Predictions"])

with tab1:
    show_top_recommendation()

with tab2:
    explore_predictions_ui()
