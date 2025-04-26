import streamlit as st
import pandas as pd
from sqlalchemy.engine import Engine
from optiview.ui.queries import load_predictions, get_prediction_filter_options
from optiview.ui.ui_components import format_month


def confidence_stars(score: float | None) -> str:
    if score is None:
        return "—"
    thresholds = [0.2, 0.4, 0.6, 0.8]
    count = sum(score >= t for t in thresholds) + 1
    return "★" * count + "☆" * (5 - count)


def count_stars(star_string: str) -> int:
    """
    Count the number of filled stars (★) in a star string.
    """
    return star_string.count("★")


def show(engine: Engine) -> None:
    st.header("📋 View Predictions")

    # Load options from database
    options = get_prediction_filter_options()

    if not options["strategies"] or not options["symbols"] or not options["months"]:
        st.warning("No predictions available yet.")
        return

    # Sidebar Filters
    selected_strategy = st.sidebar.selectbox(
        "Select Strategy", options=options["strategies"]
    )
    selected_symbol = st.sidebar.selectbox("Select Symbol", options=options["symbols"])
    selected_month = st.sidebar.selectbox(
        "Select Month",
        options=options["months"],
        format_func=format_month,
        index=0,
    )

    # Star-Based Filters
    min_conf_stars = st.sidebar.slider("Min Confidence Stars", 0, 5, 0, 1)
    min_quality_stars = st.sidebar.slider("Min Quality Stars", 0, 5, 0, 1)

    st.markdown(f"### Strategy: `{selected_strategy}`")

    # Load Data
    df = load_predictions(selected_symbol, selected_month, selected_strategy)

    if df.empty:
        st.info("No predictions found for the selected filters.")
        return

    # Compute confidence and quality stars
    df["confidence"] = df["confidence_score"].apply(confidence_stars)
    df["quality"] = df["quality_score"].apply(
        lambda x: confidence_stars(x) if x is not None else "—"
    )

    # Apply Filters
    df = df[df["confidence"].apply(count_stars) >= min_conf_stars]
    df = df[df["quality"].apply(count_stars) >= min_quality_stars]

    if df.empty:
        st.info("No predictions match the selected confidence/quality filters.")
        return

    df["recommended"] = df["rank"].apply(lambda r: "✅" if r == 1 else "")

    # Display
    display_df = df[
        ["recommended", "model", "predicted_profit", "confidence", "quality", "inputs"]
    ].rename(
        columns={
            "recommended": "",
            "model": "Model",
            "predicted_profit": "Predicted $",
            "confidence": "Confidence",
            "quality": "Quality",
            "inputs": "Parameters",
        }
    )

    st.dataframe(display_df, use_container_width=True)
