# File: src/optiview/viz/boxplot.py

import streamlit as st
import plotly.express as px
import pandas as pd


def boxplot_by_param(df: pd.DataFrame, param_col: str, score_col: str) -> None:
    fig = px.box(
        df, x=param_col, y=score_col, title=f"{score_col} by {param_col}", points="all"
    )
    st.plotly_chart(fig, use_container_width=True)
