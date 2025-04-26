# File: optiview/tabs/home_tab.py

import streamlit as st
from sqlalchemy.engine import Engine
from optiview.ui.queries import load_latest_top_prediction
from optiview.ui.ui_components import format_month

def render_confidence_stars(score: float | None) -> str:
    if score is None:
        return "—"
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)

def show(engine: Engine) -> None:
    from optiview.ui.ui_components import format_month
    latest = load_latest_top_prediction()
    if latest is None:
        st.info("No recommendations available yet.")
        return
    
    st.header(f"🔮 Most Recommended Trade ({format_month(latest['month'])})")
    st.subheader(f"Symbol: {latest['symbol']} | Model: {latest['model']}")
    st.metric("Predicted Profit", f"${latest['predicted_profit']:.2f}")
    st.write(f"Confidence: {render_confidence_stars(latest['confidence_score'])}")

    qs = latest.get("quality_score")
    st.write(f"Quality Score: {qs:.2f}" if qs is not None else "Quality Score: —")

    st.markdown("**Recommended Settings:**")
    st.json(latest["inputs"] or {})
