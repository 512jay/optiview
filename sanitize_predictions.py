from pathlib import Path
import pandas as pd

base_dir = Path("generated/predictions")


def sanitize_csv(file_path: Path) -> None:
    try:
        df = pd.read_csv(file_path)
        df = df.loc[:, ~df.columns.duplicated()]
        eval_cols = [
            "predicted_profit",
            "actual_profit",
            "quality_score",
            "quality_stars",
            "confidence_stars",
        ]
        front = [col for col in eval_cols if col in df.columns]
        rest = [col for col in df.columns if col not in front]
        df = df[front + rest]
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"⚠️ Error processing {file_path}: {e}")


for month_dir in base_dir.iterdir():
    if not month_dir.is_dir():
        continue
    for symbol_dir in month_dir.iterdir():
        if not symbol_dir.is_dir():
            continue
        for model_dir in symbol_dir.iterdir():
            if not model_dir.is_dir():
                continue
            for fname in ["prediction_summary.csv", "annotations.csv"]:
                fpath = model_dir / fname
                if fpath.exists():
                    sanitize_csv(fpath)

print("✅ Sanitization complete.")
