# File: src/optiview/app.py

import streamlit as st
import pandas as pd
from pathlib import Path
from optiview.data.loader import load_runs
from optiview.viz.boxplot import boxplot_by_param
from optiview.viz.heatmap import heatmap_of_two_params
from optiview.viz.scatter import scatter_with_trendline

st.set_page_config(layout="wide")
st.title("📊 OptiView – MT5 Optimization Run Explorer")

# --- File Selection ---
st.sidebar.header("📁 Select Database")

uploaded_file = st.sidebar.file_uploader("Upload a SQLite .db file", type=["db"])
default_db = Path("db/optibatch.db")

if uploaded_file is not None:
    db_path = Path(uploaded_file.name)
    with open(db_path, "wb") as f:
        f.write(uploaded_file.read())
    st.sidebar.success(f"Using uploaded file: {uploaded_file.name}")
elif default_db.exists():
    db_path = default_db
    st.sidebar.info(f"Using default symlinked DB: {default_db}")
else:
    st.sidebar.error("No database file selected or found.")
    st.stop()

# --- Load Data ---
try:
    df = load_runs(db_path)
    st.success(f"Loaded {len(df):,} runs from database ✅")
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# --- Preview Data ---
# st.subheader("🔍 Data Preview")
# st.write(f"Shape: `{df.shape[0]:,} rows × {df.shape[1]} columns`")
# st.dataframe(df.head(100), use_container_width=True)


st.markdown("## 📊 Performance Visualizations")

param_col = st.selectbox(
    "Select input parameter", [col for col in df.columns if col.startswith("input_")]
)
score_col = st.selectbox(
    "Select score column", ["profit", "custom_score", "sharpe_ratio"]
)

boxplot_by_param(df, param_col, score_col)
scatter_with_trendline(df, param_col, score_col)

# Optionally allow picking two input params for heatmap
numeric_inputs = [
    col
    for col in df.columns
    if col.startswith("input_") and pd.api.types.is_numeric_dtype(df[col])
]

x_param = st.selectbox("X Axis Param", numeric_inputs, key="heatmap_x")
y_param = st.selectbox("Y Axis Param", numeric_inputs, key="heatmap_y")

heatmap_of_two_params(df, x_param, y_param, score_col)
st.write(f"x_param type: {type(x_param)}, y_param type: {type(y_param)}")
