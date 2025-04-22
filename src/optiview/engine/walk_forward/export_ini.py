# 📁 File: src/optiview/engine/walk_forward/export_ini.py

from pathlib import Path
import pandas as pd


def export_ini_file(df: pd.DataFrame, folder: Path) -> None:
    for idx, (_, row) in enumerate(df.iterrows(), 1):
        filename = folder / f"predicted_config_rank_{idx}.ini"
        with filename.open("w", encoding="utf-16") as f:
            f.write("[TesterInputs]\n")
            for col in row.index:
                if col.startswith("input_"):
                    f.write(f"{col}={row[col]}\n")
