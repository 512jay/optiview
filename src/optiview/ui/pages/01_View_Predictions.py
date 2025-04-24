import streamlit as st
import pandas as pd
from pathlib import Path


def get_available_symbols(pred_root: Path) -> list[str]:
    """Return a sorted list of symbols available in the prediction folder."""
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
    """Return a reverse-sorted list of months that contain predictions for a symbol."""
    return sorted(
        {p.name for p in pred_root.iterdir() if (p / symbol).exists()}, reverse=True
    )


def stars_to_score(stars: str) -> int:
    """Convert star string (e.g., '★★☆☆☆') to integer score."""
    return stars.count("★") if isinstance(stars, str) else 0


def tag_best_recommendation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'recommended' column that flags the config with the highest predicted profit
    among those with the most confidence stars.
    """
    df["confidence_numeric"] = df["confidence_stars"].apply(stars_to_score)
    max_stars = df["confidence_numeric"].max()
    top_confidence = df[df["confidence_numeric"] == max_stars]

    if not top_confidence.empty:
        max_profit = top_confidence["predicted_profit"].max()
        df["recommended"] = (df["confidence_numeric"] == max_stars) & (
            df["predicted_profit"] == max_profit
        )
    else:
        df["recommended"] = False

    df["recommended"] = df["recommended"].apply(lambda x: "✅" if x else "")
    return df


def load_prediction_summary(pred_root: Path, symbol: str, month: str) -> pd.DataFrame:
    """
    Load prediction and annotation data for a given symbol/month, and annotate best config.
    """
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
                df_annot[["rank", "actual_profit", "quality_score", "quality_stars"]],
                on="rank",
                how="left",
            )

        df = df.loc[:, ~df.columns.duplicated()]
        rows.append(df)

    if not rows:
        return pd.DataFrame()

    df_all = pd.concat(rows, ignore_index=True)
    df_all["confidence_score"] = df_all["confidence_score"].round(3)
    df_all["quality_score"] = df_all["quality_score"].round(3)
    df_all = tag_best_recommendation(df_all)

    # Reorder so recommended appears first
    df_all = df_all.sort_values(
        by=["recommended", "confidence_score", "predicted_profit"],
        ascending=[False, False, False],
    )

    df_all.rename(
        columns={
            "recommended": "✔️",
            "model": "mod",
            "rank": "rnk",
            "predicted_profit": "prof",
            "confidence_score": "conf",
            "confidence_stars": "★",
            "actual_profit": "actp",
            "quality_score": "qual",
            "quality_stars": "☆",
        },
        inplace=True,
    )

    base_cols = ["✔️", "mod", "prof", "conf", "★", "actp", "qual", "☆", "rnk"]
    input_cols = sorted([c for c in df_all.columns if c.startswith("input_")])
    selected = [c for c in base_cols if c in df_all.columns] + input_cols
    return df_all[selected]


def render_predictions_view() -> None:
    """Streamlit entry point for the predictions view UI."""
    st.title("\U0001f4ca View Predictions")
    pred_root = Path("generated/predictions")

    if not pred_root.exists():
        st.warning("\u26a0\ufe0f predictions folder not found.")
        return

    symbols = get_available_symbols(pred_root)
    if not symbols:
        st.warning("\u26a0\ufe0f No symbols found.")
        return

    symbol = st.selectbox("Select Symbol", options=symbols)
    months = get_available_months(pred_root, symbol)
    if not months:
        st.warning("\u26a0\ufe0f No months available for selected symbol.")
        return

    month = st.selectbox("Select Month", options=months)
    df = load_prediction_summary(pred_root, symbol, month)

    if df.empty:
        st.warning("\u26a0\ufe0f No predictions found for this selection.")
    else:
        st.data_editor(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "✔️": st.column_config.TextColumn(
                    label="✔️", help="Best config based on predicted profit + confidence"
                ),
                "mod": st.column_config.TextColumn(
                    label="mod", help="Model used for prediction (e.g., xgb, cat)"
                ),
                "prof": st.column_config.NumberColumn(
                    label="prof", help="Expected profit for this configuration"
                ),
                "conf": st.column_config.NumberColumn(
                    label="conf",
                    help="Estimated confidence based on historical prediction accuracy",
                ),
                "★": st.column_config.TextColumn(
                    label="★", help="1–5 star rating of prediction confidence"
                ),
                "actp": st.column_config.NumberColumn(
                    label="actp", help="Realized profit from backtest (if available)"
                ),
                "qual": st.column_config.NumberColumn(
                    label="qual", help="How well this model predicted in past months"
                ),
                "☆": st.column_config.TextColumn(
                    label="☆", help="1–5 star rating of past prediction performance"
                ),
                "rnk": st.column_config.NumberColumn(
                    label="rnk", help="Rank within this model group (1 = top pick)"
                ),
            },
            disabled=True,
        )


if __name__ == "__main__":
    render_predictions_view()
