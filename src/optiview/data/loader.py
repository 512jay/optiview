# File: src/optiview/data/loader.py

import sqlite3
import json
from pathlib import Path
import pandas as pd
from pandas import json_normalize
from typing import Any
from optiview.data.db_path import get_db_path


def load_runs() -> pd.DataFrame:
    db_path = get_db_path()

    """
    Loads optimization run results from the OptiBatch SQLite database.

    Returns:
        pd.DataFrame: DataFrame containing runs and extracted input params.
    """

    if not db_path.exists():
        raise FileNotFoundError(f"Database not found at: {db_path}")

    conn = sqlite3.connect(str(db_path))
    try:
        df = pd.read_sql("SELECT * FROM runs", conn)

        # Decode JSON if necessary
        if "params_json" in df.columns:
            params_raw = df["params_json"].apply(
                lambda val: json.loads(val) if isinstance(val, str) else val
            )
            param_df = json_normalize(params_raw.tolist())  # type: ignore[arg-type]
            df = pd.concat([df.drop(columns=["params_json"]), param_df], axis=1)

        return df
    finally:
        conn.close()
