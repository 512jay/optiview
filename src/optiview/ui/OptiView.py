# File: src/optiview/ui/OptiView.py

import os
import streamlit as st
from streamlit import runtime
from pathlib import Path

# 🧭 Register all page scripts
PAGES_DIR = Path(__file__).parent / "pages"

# Ensure all page scripts are discovered in order
st.set_page_config(page_title="OptiView Predictions", layout="wide")

# Streamlit auto-discovers files in pages/, so nothing else is needed here.
# This file acts as the launcher.

import shutil
import subprocess

st.title("🧠 OptiView System Overview")

st.markdown(
    """
Welcome to **OptiView** — your MT5 optimization analysis and prediction tool.

Here’s what you can do:
- 🗂 Explore past optimization results
- 🤖 Run walk-forward predictions
- ⭐ View prediction confidence using quality scores
- ⚙️ Re-initialize the system when new data is added
"""
)
st.subheader("Update and Append Data")
if st.button("Add New Data & Update"):
    st.info("📥 Processing new data and updating predictions...")

    # Run prediction generator
    subprocess.run(
        ["poetry", "run", "python", "src/optiview/engine/walk_forward/bulk_predict.py"]
    )

    # Recalculate quality scores
    subprocess.run(
        ["poetry", "run", "python", "src/optiview/analysis/evaluate_predictions.py"]
    )

    st.success("✅ Update complete! Visit the sidebar to view predictions.")


st.subheader("🔄 Rebuild System")

if st.button("Reset and Rebuild All"):
    st.info("⚙️ Rebuilding predictions and quality scores. Please wait...")

    # Delete old predictions and quality results
    shutil.rmtree("generated/predictions", ignore_errors=True)
    shutil.rmtree("generated/quality", ignore_errors=True)

    # Regenerate predictions
    subprocess.run(
        ["poetry", "run", "python", "src/optiview/engine/walk_forward/bulk_predict.py"]
    )

    # Recalculate quality scores
    subprocess.run(
        ["poetry", "run", "python", "src/optiview/analysis/evaluate_predictions.py"]
    )

    st.success("✅ Rebuild complete! Visit the sidebar to view predictions.")

if st.button("Check DB Path"):
    db_path = os.getenv("OPTIVIEW_DB_PATH")
    if db_path and Path(db_path).exists():
        st.success(f"✅ DB found at: {db_path}")
    else:
        st.error(f"❌ DB not found or env var not set: {db_path}")
