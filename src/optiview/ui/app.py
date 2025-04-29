"""File: src/optiview/ui/app.py
Main entry point for OptiView Streamlit app.
"""

import streamlit as st
from optiview.ui.components.header import render_header

# App setup
st.set_page_config(
    page_title="OptiView",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main() -> None:
    """Main function for Streamlit app."""
    render_header()

    st.write("Welcome to **OptiView**! 📊")
    st.write("Please use the sidebar to navigate between features.")


if __name__ == "__main__":
    main()
