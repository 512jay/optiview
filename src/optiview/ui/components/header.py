"""File: src/optiview/ui/components/header.py
Reusable header component.
"""

import streamlit as st


def render_header() -> None:
    """Renders the app header."""
    st.title("📈 OptiView Dashboard")
    st.caption("Explore. Predict. Optimize.")
