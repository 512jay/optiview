# scripts/maintenance/sync_jobs.py

"""Synchronize jobs from OptiBatch into OptiView's synced_jobs table.

This script connects to the external OptiBatch database,
retrieves all jobs, and inserts or updates them into
OptiView's local synced_jobs table.

Intended to be run manually or automatically before bulk predictions.

Usage:
    poetry run python src/optiview/maintenance/sync_jobs.py
"""


import sys
from pathlib import Path

# Add the project src/ folder to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))
import sqlite3
from typing import Any
from pathlib import Path
from optiview.database.db_paths import get_optibatch_db_path
from optiview.database.session import get_optiview_session
from optiview.database.models import SyncedJob


def get_optibatch_connection() -> sqlite3.Connection:
    """Create a read-only connection to the OptiBatch database.

    Returns:
        sqlite3.Connection: Connection object to OptiBatch.

    Raises:
        FileNotFoundError: If the OptiBatch database file does not exist.
    """
    batch_db_path = get_optibatch_db_path()
    if not batch_db_path.exists():
        raise FileNotFoundError(f"OptiBatch database not found at {batch_db_path}")
    return sqlite3.connect(batch_db_path)


def fetch_all_jobs(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    """Fetch all jobs from the OptiBatch database.

    Args:
        conn (sqlite3.Connection): Connection to OptiBatch database.

    Returns:
        list[dict[str, Any]]: List of job dictionaries.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, expert_name, expert_path, period, deposit, currency, leverage,
               model, optimization_mode, optimization_criterion, tester_inputs
        FROM jobs
        """
    )
    columns = [desc[0] for desc in cursor.description]
    jobs = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return jobs


def sync_jobs() -> None:
    """Synchronize jobs from OptiBatch into OptiView."""
    try:
        conn = get_optibatch_connection()
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    jobs = fetch_all_jobs(conn)
    local_session = get_optiview_session()

    inserted = 0
    updated = 0

    for job in jobs:
        existing = local_session.query(SyncedJob).filter_by(id=job["id"]).first()
        if existing:
            existing.expert_name = job["expert_name"]
            existing.expert_path = job["expert_path"]
            existing.period = job["period"]
            existing.deposit = job["deposit"]
            existing.currency = job["currency"]
            existing.leverage = job["leverage"]
            existing.model = job["model"]
            existing.optimization_mode = job["optimization_mode"]
            existing.optimization_criterion = job["optimization_criterion"]
            existing.tester_inputs = job["tester_inputs"]
            updated += 1
        else:
            new_job = SyncedJob(
                id=job["id"],
                expert_name=job["expert_name"],
                expert_path=job["expert_path"],
                period=job["period"],
                deposit=job["deposit"],
                currency=job["currency"],
                leverage=job["leverage"],
                model=job["model"],
                optimization_mode=job["optimization_mode"],
                optimization_criterion=job["optimization_criterion"],
                tester_inputs=job["tester_inputs"],
            )
            local_session.add(new_job)
            inserted += 1

    local_session.commit()

    print(f"\n✅ Synced jobs into OptiView:")
    print(f"- Inserted: {inserted} new jobs")
    print(f"- Updated: {updated} existing jobs")
    print("🔄 Synchronization complete!")
    print("You can now run bulk predictions with the latest job data.")
    print("Make sure to run this script periodically to keep job data up-to-date.")
    print("Happy trading! 🚀")
    print("For more details, check the OptiView documentation.")


if __name__ == "__main__":
    sync_jobs()
