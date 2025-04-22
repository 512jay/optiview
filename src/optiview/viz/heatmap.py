# File: src/optiview/viz/heatmap.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def heatmap_of_two_params(
    df: pd.DataFrame, x_param: str, y_param: str, value_col: str
) -> None:
    # 🔍 Debug help
    if x_param not in df.columns:
        st.error(f"X param '{x_param}' not in DataFrame")
        return
    if y_param not in df.columns:
        st.error(f"Y param '{y_param}' not in DataFrame")
        return

    try:
        pivot = df.pivot_table(
            index=y_param, columns=x_param, values=value_col, aggfunc="mean"
        )
    except Exception as e:
        st.error(f"Failed to generate heatmap: {e}")
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(pivot, annot=False, cmap="coolwarm", ax=ax)
    ax.set_title(f"{value_col} Heatmap ({y_param} vs {x_param})")
    st.pyplot(fig)
