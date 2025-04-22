import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit import column_config


def load_prediction_data(base_path: Path) -> dict:
    prediction_data = {}
    for month_dir in sorted(base_path.iterdir()):
        for symbol_dir in month_dir.iterdir():
            csv_path = symbol_dir / "prediction_summary.csv"
            if csv_path.exists():
                key = (month_dir.name, symbol_dir.name)
                prediction_data[key] = pd.read_csv(csv_path)
    return prediction_data


def main():
    st.set_page_config(page_title="OptiView Predictions", layout="wide")
    st.sidebar.title("View Predictions")

    base_path = Path("generated/predictions")
    data = load_prediction_data(base_path)

    if not data:
        st.warning("No prediction data found in 'generated/predictions'")
        return

    month_options = sorted(set(k[0] for k in data), reverse=True)
    symbol_options = sorted(set(k[1] for k in data))

    selected_month = st.selectbox("Select Month", month_options, index=0)
    selected_symbol = st.selectbox("Select Symbol", symbol_options)

    key = (selected_month, selected_symbol)
    if key in data:
        df = data[key]
        # Rename score column for clarity
        if "predicted_score" in df.columns:
            df = df.rename(columns={"predicted_score": "predicted_profit"})


        # Simplify columns for display
        keep_cols = [
            "rank",
            "symbol",
            "run_month",
            "predicted_profit",
            "input_LongStopLossPercent",
            "input_ShortStopLossPercent",
        ]
        df = df[[c for c in keep_cols if c in df.columns]].copy()

        # After df = df[[...]].copy()
        if "quality_score" in df.columns:
            def quality_to_stars(q: float) -> str:
                if q >= 0.9:
                    return "⭐⭐⭐⭐⭐"
                elif q >= 0.7:
                    return "⭐⭐⭐⭐"
                elif q >= 0.5:
                    return "⭐⭐⭐"
                elif q >= 0.3:
                    return "⭐⭐"
                else:
                    return "⭐"

            df["expected_profit_confidence"] = df["quality_score"].apply(quality_to_stars)


        # Reorder columns
        cols = [
            "rank",
            "symbol",
            "run_month",
            "expected_profit_confidence",
            "predicted_profit",
            "input_LongStopLossPercent",
            "input_ShortStopLossPercent",
        ]
        df = df[[c for c in cols if c in df.columns]]

        # Display
        st.dataframe(df, use_container_width=True)

        # INI downloads
        ini_folder = base_path / selected_month / selected_symbol
        ini_files = list(ini_folder.glob("*.ini"))
        st.markdown("### 📦 Download INI Files")
        for ini_file in ini_files:
            with ini_file.open("r", encoding="utf-16") as f:
                st.download_button(
                    label=ini_file.name, data=f.read(), file_name=ini_file.name
                )
    else:
        st.info(f"No data found for {selected_symbol} in {selected_month}")


if __name__ == "__main__":
    main()
