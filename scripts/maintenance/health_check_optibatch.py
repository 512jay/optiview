"""
health_check_optibatch.py
Location: scripts/maintenance/

Verifies that all params_json fields are properly populated for all symbols and months.
Outputs both console results and a CSV report.
"""
import sys
from pathlib import Path

# Add the project src/ folder to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

import sqlite3
import json
import csv
import os
from typing import Any

from optiview.database.db_paths import get_optibatch_db_path

def health_check_optibatch_db(db_path: str, output_csv: str) -> None:
    """Check all symbols/months for params_json validity and save report."""

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT symbol, run_month
        FROM runs
        ORDER BY symbol, run_month
        """
    )
    symbol_months = cursor.fetchall()

    print(f"🔎 Found {len(symbol_months)} symbol/month combinations to check.")

    rows_for_csv: list[dict[str, Any]] = []
    problems_found = False

    for symbol, run_month in symbol_months:
        cursor.execute(
            """
            SELECT params_json
            FROM runs
            WHERE symbol = ?
              AND run_month = ?
            """,
            (symbol, run_month),
        )
        rows = cursor.fetchall()

        missing = 0
        bad_rows = 0

        for (params_json_str,) in rows:
            if params_json_str is None:
                missing += 1
                continue

            try:
                params = json.loads(params_json_str)
            except Exception:
                bad_rows += 1
                continue

            if not isinstance(params, dict):
                bad_rows += 1
                continue

            if (
                "input_LongStopLossPercent" not in params
                or "input_ShortStopLossPercent" not in params
            ):
                bad_rows += 1
                continue

            if (
                params["input_LongStopLossPercent"] is None
                or params["input_ShortStopLossPercent"] is None
            ):
                bad_rows += 1
                continue

        total = len(rows)
        status = "OK" if missing == 0 and bad_rows == 0 else "Problem"
        if status == "Problem":
            problems_found = True
            print(
                f"⚠️  {symbol} {run_month}: {missing} missing params_json, {bad_rows} bad params out of {total} runs."
            )
        else:
            print(f"✅ {symbol} {run_month}: OK ({total} runs)")

        rows_for_csv.append(
            {
                "symbol": symbol,
                "run_month": run_month,
                "total_runs": total,
                "missing_params_json": missing,
                "bad_params_json": bad_rows,
                "status": status,
            }
        )

    conn.close()

    # Write CSV report
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "symbol",
                "run_month",
                "total_runs",
                "missing_params_json",
                "bad_params_json",
                "status",
            ],
        )
        writer.writeheader()
        writer.writerows(rows_for_csv)

    print(f"\n📄 Health check results saved to: {output_csv}")

    if not problems_found:
        print("\n✅ All symbol/month runs passed health check.")
    else:
        print("\n⚠️ Problems found — review needed.")


if __name__ == "__main__":
    # Adjust paths as needed
    optibatch_db_path = get_optibatch_db_path()
    output_csv_path = "generated/health_check/optibatch_health_report.csv"

    health_check_optibatch_db(optibatch_db_path, output_csv_path)
