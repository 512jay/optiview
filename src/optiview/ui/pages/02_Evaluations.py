# File: src/optiview/ui/pages/02_Evaluations.py

"""
Streamlit page for exploring model evaluations.

Allows filtering by month, symbol, and one or more models.
Displays predicted vs actual profit, quality and confidence metrics,
and derived evaluation scores. Built on top of SQLAlchemy models.
"""

import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from optiview.database.models import EvaluatedSetting
from optiview.database.db_paths import get_optiview_db_path
from io import StringIO


@st.cache_data
def load_evaluations() -> pd.DataFrame:
    """Load evaluated predictions from the database.

    Returns:
        DataFrame with all fields from EvaluatedSetting.
    """
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)
    with Session(engine) as session:
        rows = session.execute(select(EvaluatedSetting)).scalars().all()
        data = [r.__dict__ for r in rows]
        df = pd.DataFrame(data)
        df.drop(columns=["_sa_instance_state"], errors="ignore", inplace=True)
        return df


def main() -> None:
    """Render the Streamlit UI for viewing evaluated predictions."""
    st.set_page_config(layout="wide")
    st.title("📈 Evaluation Results")

    df = load_evaluations()
    if df.empty:
        st.warning("No evaluation data available.")
        return

    # Filters
    months = sorted(df["month"].dropna().unique(), reverse=True)
    symbols = sorted(df["symbol"].dropna().unique())
    models = sorted(df["model"].dropna().unique())

    selected_month: str = st.selectbox("Month", months)
    selected_symbol: str = st.selectbox("Symbol", symbols)
    selected_models: list[str] = st.multiselect("Models", models, default=models)

    filtered = df[
        (df["month"] == selected_month)
        & (df["symbol"] == selected_symbol)
        & (df["model"].isin(selected_models))
    ].copy()

    # Derived columns
    filtered["result_delta"] = pd.to_numeric(
        filtered["actual_result"], errors="coerce"
    ) - pd.to_numeric(filtered["predicted_profit"], errors="coerce")

    st.dataframe(
        filtered[
            [
                "month",
                "symbol",
                "model",
                "rank",
                "evaluator_version",
                "predicted_profit",
                "actual_result",
                "result_delta",
                "quality_score",
                "quality_stars",
                "confidence_score",
                "confidence_stars",
                "matched_run_id",
                "matched_job_id",
                "evaluated_at",
            ]
        ].sort_values("rank"),
        use_container_width=True,
    )

    # Export Button
    csv = filtered.to_csv(index=False)
    st.download_button(
        "📥 Download Evaluations (CSV)",
        data=csv,
        file_name="evaluated_predictions.csv",
        mime="text/csv",
    )

    # Summary Statistics
    st.markdown("---")
    st.subheader("📊 Evaluation Summary")

    st.metric("Average Result Delta", f"{filtered['result_delta'].mean():.2f}")
    st.metric("Average Quality Score", f"{filtered['quality_score'].mean():.3f}")
    st.metric("Average Confidence Score", f"{filtered['confidence_score'].mean():.3f}")

    st.markdown("---")
    st.subheader("📊 Evaluation Metrics")

    st.markdown("**Actual vs Predicted Profit**")
    st.altair_chart(
        alt.Chart(filtered)
        .mark_circle(size=60)
        .encode(
            x="predicted_profit:Q",
            y="actual_result:Q",
            color="model:N",
            tooltip=[
                "rank",
                "model",
                "predicted_profit",
                "actual_result",
                "result_delta",
            ],
        )
        .interactive()
        .properties(height=300),
        use_container_width=True,
    )

    st.markdown("**Confidence vs Quality Score**")
    st.altair_chart(
        alt.Chart(filtered)
        .mark_circle(size=60)
        .encode(
            x="confidence_score:Q",
            y="quality_score:Q",
            color="model:N",
            tooltip=["model", "confidence_score", "quality_score", "result_delta"],
        )
        .interactive()
        .properties(height=300),
        use_container_width=True,
    )

    st.markdown("**📊 Model Comparison: Average Metrics**")
    model_avg = (
        filtered.groupby("model")[["quality_score", "confidence_score", "result_delta"]]
        .mean(numeric_only=True)
        .reset_index()
        .sort_values("result_delta", ascending=False)
    )
    model_avg = model_avg.melt(id_vars="model", var_name="metric", value_name="value")

    chart = (
        alt.Chart(model_avg)
        .mark_bar()
        .encode(
            x=alt.X("model:N", title="Model"),
            y=alt.Y("value:Q", title="Metric Value"),
            color="metric:N",
            tooltip=["model", "metric", "value"],
        )
        .facet(column=alt.Column("metric:N", title=None))
        .resolve_scale(y="independent")
    )
    st.altair_chart(chart, use_container_width=True)

    st.download_button(
        "📥 Export Model Averages",
        model_avg.to_csv(index=False),
        file_name="model_comparison.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    main()
