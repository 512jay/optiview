# File: src/optiview/viz/scatter.py

import streamlit as st
import plotly.express as px
import pandas as pd


def scatter_with_trendline(df: pd.DataFrame, x_param: str, y_metric: str) -> None:
    fig = px.scatter(
        df,
        x=x_param,
        y=y_metric,
        title=f"{y_metric} vs {x_param}",
        trendline="lowess",
        opacity=0.6,
    )
    st.plotly_chart(fig, use_container_width=True)
