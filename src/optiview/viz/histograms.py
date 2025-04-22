# File: src/optiview/viz/histograms.py

import streamlit as st
import pandas as pd
import plotly.express as px
from typing import Optional


def plot_histogram(
    df: pd.DataFrame,
    column: str,
    bins: Optional[int] = 30,
    title: Optional[str] = None,
) -> None:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    data = df[column].dropna()

    if data.nunique() < 2:
        st.info(f"Only one unique value: {data.unique()[0]}")
        return

    fig = px.histogram(
        data,
        x=column,
        nbins=bins,
        title=title or f"Histogram of {column}",
        opacity=0.75,
    )
    fig.update_layout(bargap=0.05)

    st.plotly_chart(fig, use_container_width=True)
