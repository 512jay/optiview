# File: src/optiview/ui/pages/01_View_Predictions.py

import streamlit as st
import pandas as pd
from pathlib import Path


def get_available_symbols(pred_root: Path) -> list[str]:
    return sorted(
        {
            p.name
            for m in pred_root.iterdir()
            if m.is_dir()
            for p in m.iterdir()
            if p.is_dir()
        }
    )


def get_available_months(pred_root: Path, symbol: str) -> list[str]:
    return sorted(
        {p.name for p in pred_root.iterdir() if (p / symbol).exists()}, reverse=True
    )


def load_prediction_summary(pred_root: Path, symbol: str, month: str) -> pd.DataFrame:
    rows = []
    base_path = pred_root / month / symbol

    for model_dir in base_path.iterdir():
        if not model_dir.is_dir():
            continue

        pred_path = model_dir / "prediction_summary.parquet"
        annot_path = model_dir / "annotations.parquet"
        model_name = model_dir.name

        if not pred_path.exists():
            continue

        df = pd.read_parquet(pred_path)
        df["model"] = model_name

        if annot_path.exists():
            df_annot = pd.read_parquet(annot_path)
            df_annot["model"] = model_name
            df = pd.merge(
                df,
                df_annot[
                    ["rank", "actual_profit", "quality_score", "quality_stars"]
                ],
                on="rank",
                how="left",
            )

        df = df.loc[:, ~df.columns.duplicated()]
        rows.append(df)

    if not rows:
        return pd.DataFrame()

    df_all = pd.concat(rows, ignore_index=True)

    # Trim to useful columns
    base_cols = [
        "model",
        "rank",
        "predicted_profit",
        "actual_profit",
        "confidence_stars",
        "quality_score",
        "quality_stars",
    ]

    input_cols = sorted([c for c in df_all.columns if c.startswith("input_")])
    selected = [c for c in base_cols if c in df_all.columns] + input_cols

    return df_all[selected]


def render_predictions_view() -> None:
    st.title("📊 View Predictions")
    pred_root = Path("generated/predictions")

    if not pred_root.exists():
        st.warning("⚠️ predictions folder not found.")
        return

    symbols = get_available_symbols(pred_root)
    if not symbols:
        st.warning("⚠️ No symbols found.")
        return

    symbol = st.selectbox("Select Symbol", options=symbols)
    months = get_available_months(pred_root, symbol)
    if not months:
        st.warning("⚠️ No months available for selected symbol.")
        return

    month = st.selectbox("Select Month", options=months)
    df = load_prediction_summary(pred_root, symbol, month)

    if df.empty:
        st.warning("⚠️ No predictions found for this selection.")
    else:
        st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    render_predictions_view()
