# File: src/optiview/data/join_tools.py

import sqlite3
import json
import pandas as pd
from optiview.data.db_path import get_optiview_db_path, get_optibatch_db_path
from typing import Optional


def get_metadata_for_run(run_id: int) -> Optional[dict]:
    """
    Fetch full metadata for a given run_id from OptiBatch.
    Joins `runs` and `jobs` to return all fields needed for .ini generation.
    """
    conn = sqlite3.connect(get_optiview_db_path())
    conn.execute(f"ATTACH DATABASE '{get_optibatch_db_path()}' AS optibatch")

    query = """
    SELECT 
        r.id AS run_id,
        r.symbol,
        r.start_date,
        r.end_date,
        r.run_month,
        r.pass_number,
        r.params_json,
        j.expert_name,
        j.expert_path,
        j.period,
        j.deposit,
        j.currency,
        j.leverage,
        j.model AS optimization_model,
        j.optimization_criterion
    FROM optibatch.runs r
    JOIN optibatch.jobs j ON r.job_id = j.id
    WHERE r.id = ?
    """

    try:
        row = pd.read_sql_query(query, conn, params=(run_id,)).to_dict(orient="records")
        return row[0] if row else None
    finally:
        conn.close()


def get_expert_name_for_run(run_id: int) -> Optional[str]:
    """Quickly fetch just the expert_name for a given run_id."""
    metadata = get_metadata_for_run(run_id)
    return metadata.get("expert_name") if metadata else None


def get_ini_data_for_run(run_id: int) -> Optional[dict]:
    """
    Prepare structured dict of .ini-compatible fields for a given run.
    Includes [Tester] and [TesterInputs] keys.
    """
    meta = get_metadata_for_run(run_id)
    if not meta:
        return None

    # Parse JSON params into input format
    try:
        inputs = (
            json.loads(meta["params_json"])
            if isinstance(meta["params_json"], str)
            else meta["params_json"]
        )
    except Exception:
        inputs = {}

    return {
        "Tester": {
            "Expert": meta["expert_path"],
            "Symbol": meta["symbol"],
            "Period": meta["period"],
            "Optimization": 1,
            "Model": meta.get("optimization_model", 1),
            "FromDate": meta["start_date"],
            "ToDate": meta["end_date"],
            "ForwardMode": 0,
            "Deposit": meta["deposit"],
            "Currency": meta["currency"],
            "ProfitInPips": 0,
            "Leverage": meta["leverage"],
            "ExecutionMode": 0,
            "OptimizationCriterion": meta.get("optimization_criterion", 0),
        },
        "TesterInputs": inputs,
    }


def render_ini_string(ini_data: dict) -> str:
    """
    Converts structured .ini-compatible dictionary into an INI file string.
    """
    if not ini_data:
        return ""

    lines = []

    # Section: [Tester]
    lines.append("[Tester]")
    for key, value in ini_data.get("Tester", {}).items():
        lines.append(f"{key}={value}")
    lines.append("")

    # Section: [TesterInputs]
    lines.append("[TesterInputs]")
    for key, val in ini_data.get("TesterInputs", {}).items():
        lines.append(f"{key}={val}")

    return "\n".join(lines)


# Prediction insert helpers
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from optiview.data.models import Base, PredictedConfig, ModelType
from optiview.data.db_path import get_optiview_db_path


def get_db_session() -> Session:
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}")
    Base.metadata.create_all(engine)
    return Session(bind=engine)


def insert_predictions(predictions: list[dict]) -> None:
    """
    Upsert prediction rows into optiview.db using SQLAlchemy.
    Uses session.merge() to overwrite existing rows based on composite PK.
    """
    session = get_db_session()
    try:
        for row in predictions:
            session.merge(PredictedConfig(**row))
        session.commit()
    finally:
        session.close()


def convert_to_prediction_dict(
    row: pd.Series,
    symbol: str,
    model_name: str,
    month: str,
    expert_name: Optional[str] = None,
    confidence_score: Optional[float] = None,
    confidence_stars: Optional[str] = None,
    predicted_profit: Optional[float] = None,
) -> dict:
    inputs_dict = {k: row[k] for k in row.index if k.startswith("input_")}
    return {
        "month": month,
        "symbol": symbol,
        "model": model_name,
        "rank": row.get("rank", 1),
        "predicted_profit": predicted_profit,  # ✅ Use real predicted profit
        "confidence_score": confidence_score,
        "confidence_stars": confidence_stars,
        "actual_profit": None,
        "quality_score": None,
        "quality_stars": None,
        "expert_name": expert_name,
        "inputs": json.dumps(inputs_dict),
        "run_id": row.get("run_id"),
        "tags": "[]",
        "notes": None,
    }


def save_prediction_outputs(
    df: pd.DataFrame,
    symbol: str,
    model_name: str,
    predict_month: pd.Timestamp,
    **kwargs,
) -> None:
    """
    Convert and store predictions into the optiview database.
    """
    month = predict_month.strftime("%Y-%m")
    predictions = [
        convert_to_prediction_dict(row, symbol, model_name, month)
        for _, row in df.iterrows()
    ]
    insert_predictions(predictions)
    print(
        f"✅ Saved {len(predictions)} predictions for {symbol} ({model_name}) into database."
    )


def extract_input_matrix(df: pd.DataFrame, input_keys: list[str]) -> pd.DataFrame:
    """
    Expand params_json into a dataframe of input columns.

    Args:
        df: DataFrame containing params_json field
        input_keys: List of expected input keys

    Returns:
        A DataFrame with input columns.
    """
    parsed_rows = []

    for val in df["params_json"].dropna():
        try:
            parsed = val if isinstance(val, dict) else json.loads(val)
            if not isinstance(parsed, dict):
                parsed = {}
        except Exception:
            parsed = {}

        row = {k: parsed.get(k, None) for k in input_keys}
        parsed_rows.append(row)

    return pd.DataFrame(parsed_rows, index=df.index)


def get_training_features(df: pd.DataFrame) -> list[str]:
    """
    Extract list of input keys from the first non-null params_json in the dataframe.
    Assumes params_json is a JSON string or a dict.
    """
    for val in df["params_json"].dropna():
        try:
            parsed = val if isinstance(val, dict) else json.loads(val)
            if isinstance(parsed, dict):
                return list(parsed.keys())
        except Exception:
            continue
    raise ValueError("No valid params_json found in training dataframe.")
