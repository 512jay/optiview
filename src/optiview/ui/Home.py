# File: src/optiview/ui/pages/00_Home.py

"""
Home page for the OptiView dashboard.
Provides an overview of features and highlights.
"""

import streamlit as st
from optiview.ui.utils.data_loader import get_available_prediction_months

# Page setup
st.set_page_config(
    page_title="Home – OptiView",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.title("🏠 OptiView Dashboard")
st.markdown("Explore. Predict. Optimize.")

# About
st.markdown(
    """
Welcome to **OptiView**, your AI-assisted engine for analyzing backtested trading strategies.

With OptiView, you can:
- 📊 **Visualize and compare predictions** from multiple models
- 🧠 **Evaluate prediction accuracy** against actual outcomes
- 🧪 **Identify top-performing configurations** from your optimization runs
- 📉 **Spot outliers and weaknesses** using diagnostic plots

Everything is designed to work seamlessly with your existing OptiBatch results.
"""
)

# Latest insight
months = get_available_prediction_months()
if months:
    st.success(f"📅 Latest available prediction data: **{months[0]}**")
else:
    st.info("No prediction data found. Please ingest results using OptiBatch.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and OptiBatch.")
