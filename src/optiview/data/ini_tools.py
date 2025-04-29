# File: src/optiview/data/ini_tools.py

"""Utilities for generating and rendering INI files from optimization runs and predictions."""

from __future__ import annotations

from typing import Optional, Any
import sqlite3
import json
from datetime import datetime


OPTIBATCH_DB_PATH = "src/optibatch/data/optibatch.db"  # Adjust path if needed


# --- Database Helper (Current CLI Uses This) ---


def get_metadata_for_job(job_id: int) -> Optional[dict[str, Any]]:
    """Fetch INI metadata for a specific optimization job from the OptiBatch database.

    Args:
        job_id (int): ID of the optimization job.

    Returns:
        Optional[dict[str, Any]]: Dictionary of INI metadata if found, otherwise None.
    """
    conn = sqlite3.connect(OPTIBATCH_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT 
                expert_name,
                expert_path,
                period,
                optimization_mode,
                optimization_criterion,
                model,
                deposit,
                currency,
                leverage,
                tester_inputs,
                created_at
            FROM jobs
            WHERE id = ?
            """,
            (job_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        (
            expert_name,
            expert_path,
            period,
            optimization_mode,
            optimization_criterion,
            model,
            deposit,
            currency,
            leverage,
            tester_inputs_raw,
            created_at,
        ) = row

        tester_inputs = json.loads(tester_inputs_raw) if tester_inputs_raw else {}

        metadata = {
            "expert_name": expert_name,
            "expert_path": expert_path,
            "period": period,
            "optimization_mode": optimization_mode,
            "optimization_criterion": optimization_criterion,
            "model": model,
            "deposit": deposit,
            "currency": currency,
            "leverage": leverage,
            "inputs": tester_inputs,
            "created_at": created_at,
        }

        return metadata

    finally:
        conn.close()


# --- INI Section Builders ---


def render_tester_section(metadata: dict[str, Any], symbol: str) -> str:
    """Render the [Tester] section of the INI file.

    Args:
        metadata (dict[str, Any]): Metadata for the optimization job.
        symbol (str): Trading symbol.

    Returns:
        str: Formatted [Tester] section string.
    """
    created_at = metadata.get("created_at", datetime.utcnow())
    from_date = "2020.01.01"  # Placeholder; can be dynamic later
    to_date = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S").strftime("%Y.%m.%d")

    tester_fields = {
        "Expert": metadata["expert_path"],
        "Symbol": symbol,
        "Period": metadata["period"],
        "Optimization": 1,
        "Model": metadata["model"],
        "FromDate": from_date,
        "ToDate": to_date,
        "ForwardMode": 0,
        "Deposit": int(metadata["deposit"]),
        "Currency": metadata["currency"],
        "ProfitInPips": 0,
        "Leverage": int(metadata["leverage"]),
        "ExecutionMode": 0,
        "OptimizationCriterion": metadata["optimization_criterion"],
    }

    lines = ["[Tester]"]
    for key, value in tester_fields.items():
        lines.append(f"{key}={value}")

    return "\n".join(lines)


def render_tester_inputs_section(inputs: dict[str, Any]) -> str:
    """Render the [TesterInputs] section of the INI file.

    Args:
        inputs (dict[str, Any]): INI input parameters.

    Returns:
        str: Formatted [TesterInputs] section string.
    """
    lines = ["[TesterInputs]"]
    for key, value in sorted(inputs.items()):
        lines.append(f"{key}={value}")
    return "\n".join(lines)


# --- CLI Generator (Based on Job Metadata) ---


def generate_full_ini(job_id: int, symbol: str) -> Optional[str]:
    """Generate the full INI file content for a given optimization job.

    Args:
        job_id (int): ID of the optimization job.
        symbol (str): Trading symbol.

    Returns:
        Optional[str]: Full INI content string if successful, otherwise None.
    """
    metadata = get_metadata_for_job(job_id)
    if metadata is None:
        return None

    tester_section = render_tester_section(metadata, symbol)
    tester_inputs_section = render_tester_inputs_section(metadata["inputs"])

    return f"{tester_section}\n\n{tester_inputs_section}"


# --- Streamlit / Interactive Generator (From Prediction) ---


def generate_ini_from_prediction(prediction: dict[str, Any]) -> str:
    """Generate a full MT5 INI file string from a selected prediction.

    Args:
        prediction (dict[str, Any]): Selected prediction dictionary.

    Returns:
        str: Full MT5 INI file content as a string.
    """
    symbol = prediction.get("symbol", "EURUSD")
    expert_name = prediction.get("expert_name", "UnknownExpert.ex5")
    period = prediction.get("period", "H1")
    deposit = prediction.get("deposit", 1000)
    currency = prediction.get("currency", "USD")
    leverage = prediction.get("leverage", 100)
    optimization_criterion = prediction.get("optimization_criterion", 0)
    model = prediction.get("model", 1)
    params_json = prediction.get("params_json", {})

    # Later we will trace prediction -> run -> job for perfect data
    from_date = "2020.01.01"
    to_date = "2025.12.31"

    tester_fields = {
        "Expert": expert_name,
        "Symbol": symbol,
        "Period": period,
        "Optimization": 1,
        "Model": model,
        "FromDate": from_date,
        "ToDate": to_date,
        "ForwardMode": 0,
        "Deposit": deposit,
        "Currency": currency,
        "ProfitInPips": 0,
        "Leverage": leverage,
        "ExecutionMode": 0,
        "OptimizationCriterion": optimization_criterion,
    }

    tester_lines = ["[Tester]"]
    for k, v in tester_fields.items():
        tester_lines.append(f"{k}={v}")

    inputs_lines = ["[TesterInputs]"]
    for k, v in sorted(params_json.items()):
        inputs_lines.append(f"{k}={v}")

    return "\n\n".join(
        [
            "\n".join(tester_lines),
            "\n".join(inputs_lines),
        ]
    )


# --- CLI Entry Point (for testing) ---

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate INI file from OptiBatch job metadata."
    )
    parser.add_argument(
        "--job-id", type=int, required=True, help="ID of the optimization job"
    )
    parser.add_argument(
        "--symbol", type=str, required=True, help="Trading symbol (e.g., EURUSD)"
    )
    parser.add_argument(
        "--output-path", type=str, default="output.ini", help="Output INI file path"
    )

    args = parser.parse_args()

    ini_content = generate_full_ini(job_id=args.job_id, symbol=args.symbol)
    if ini_content is None:
        print(f"❌ No metadata found for job ID {args.job_id}.")
    else:
        with open(args.output_path, "w", encoding="utf-16") as f:
            f.write(ini_content)
        print(f"✅ INI file saved to {args.output_path} (UTF-16 LE encoding).")
