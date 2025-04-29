# File: src/optiview/ui/pages/03_Admin_Tools.py

import streamlit as st
import time
import sys
import os
import pandas as pd

# Allow relative imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from optiview.engine.walk_forward.bulk_predict import bulk_predict as bulk_predict_main


def get_next_month() -> list[str]:
    """Return next month as a list [YYYY-MM] to predict."""
    now = pd.Timestamp.now()
    next_month = (now + pd.DateOffset(months=1)).strftime("%Y-%m")
    return [next_month]


def main() -> None:
    """Admin Tools Page."""
    st.title("🛠️ Admin Tools")

    st.header("Bulk Prediction Settings")

    months_back = st.slider(
        "Months to train back:",
        min_value=1,
        max_value=12,
        value=3,
        help="Typically 3 months. 1 month back is allowed. 0 is not allowed.",
    )

    available_models = ["xgb", "rf", "cat", "lgbm", "gbr", "histgb"]
    selected_models = st.multiselect(
        "Models to predict (future feature — not active yet):",
        options=available_models,
        default=available_models,
        help="Future feature: select which models to run. Currently all models are predicted.",
    )

    st.divider()

    st.header("Monthly Prediction (Upcoming Month Only)")
    if st.button("🚀 Run Monthly Bulk Prediction"):
        start_time = time.time()
        with st.spinner("Running monthly prediction..."):
            bulk_predict_main(full_history=False, months_back=months_back)
        elapsed = time.time() - start_time
        st.success(
            f"✅ Monthly bulk prediction complete! Elapsed time: {elapsed:.1f} seconds."
        )

    st.divider()

    st.header("Full Historical Prediction (Rebuild Entire Database)")
    confirm_full_history = st.checkbox(
        "⚠️ I confirm I want to run a full history rebuild (this may take a long time)"
    )

    if st.button("🧹 Run Full Historical Bulk Prediction"):
        if not confirm_full_history:
            st.warning(
                "⚠️ Please confirm you want to run a full rebuild by checking the box above."
            )
        else:
            start_time = time.time()
            with st.spinner("Running full historical prediction..."):
                bulk_predict_main(full_history=True, months_back=months_back)
            elapsed = time.time() - start_time
            st.success(
                f"✅ Full historical prediction complete! Elapsed time: {elapsed:.1f} seconds."
            )


if __name__ == "__main__":
    main()
