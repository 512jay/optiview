# File: optiview/OptiView.py

import os
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from optiview.ui.tabs import home_tab, view_predictions_tab, run_predictions_tab


def main() -> None:
    # Configure Streamlit page
    st.set_page_config(page_title="OptiView", layout="wide")

    # Load database path from environment variable
    db_path = os.getenv("OPTIVIEW_DB_PATH")
    if not db_path:
        st.error(
            "❗ Database path not set. Please set the OPTIVIEW_DB_PATH environment variable."
        )
        st.stop()

    # Create database engine
    engine: Engine = create_engine(f"sqlite:///{db_path}")

    # Sidebar navigation
    tab = st.sidebar.radio(
        "Navigation",
        ("🏠 Top Recommendation", "📋 View Predictions", "🔮 Run Predictions"),
    )

    # Load the selected tab
    if tab == "🏠 Top Recommendation":
        home_tab.show(engine)
    elif tab == "📋 View Predictions":
        view_predictions_tab.show(engine)
    elif tab == "🔮 Run Predictions":
        run_predictions_tab.show(engine)


if __name__ == "__main__":
    main()
