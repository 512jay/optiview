# File: src/optiview/test_loader.py

from pathlib import Path
from optiview.data.loader import load_runs


def main() -> None:
    db_path = Path("db/optibatch.db")
    df = load_runs(db_path)

    print("Loaded runs:", len(df))
    print(df.head())


if __name__ == "__main__":
    main()
