# File: src/optiview/database/loader.py

"""Loader utilities for OptiBatch and OptiView databases."""

from __future__ import annotations
import os
from typing import Any, Optional

import pandas as pd
import sqlite3

from optiview.database.session import get_optiview_session
from optiview.database.models import PredictedSetting, EvaluatedSetting
from optiview.database.db_paths import get_optibatch_db_path
from optiview.database.db_paths import get_optibatch_db_path


def get_all_symbols() -> list[str]:
    """Fetch distinct symbols from the OptiBatch runs table."""
    conn = sqlite3.connect(get_optibatch_db_path())
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT symbol FROM runs WHERE symbol IS NOT NULL")
    rows = cursor.fetchall()

    conn.close()

    return sorted(row[0] for row in rows if row[0])


def load_symbol_months_runs(symbol: str, months: list[str]) -> pd.DataFrame:
    """Load runs for a given symbol and specific months. If months empty, load all runs."""
    conn = sqlite3.connect(get_optibatch_db_path())
    cursor = conn.cursor()

    if months:
        query = f"""
        SELECT * FROM runs
        WHERE symbol = ?
          AND run_month IN ({','.join(['?'] * len(months))})
        """
        params = [symbol] + months
    else:
        query = "SELECT * FROM runs WHERE symbol = ?"
        params = [symbol]

    cursor.execute(query, params)
    rows = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]

    conn.close()

    if not rows:
        return pd.DataFrame()

    return pd.DataFrame([dict(zip(cols, row)) for row in rows])


def load_all_runs(symbol: Optional[str] = None) -> list[dict[str, Any]]:
    """Load all runs, fully populated, optionally filtered by symbol."""
    conn = sqlite3.connect(get_optibatch_db_path())
    cursor = conn.cursor()

    rows = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]

    conn.close()

    return [dict(zip(cols, row)) for row in rows]


def load_all_predictions() -> list[dict[str, Any]]:
    """Load all predicted settings from the OptiView database.

    Returns:
        list[dict]: List of prediction dictionaries.
    """
    session = get_optiview_session()
    results = session.query(PredictedSetting).all()
    return [{c.name: getattr(p, c.name) for c in p.__table__.columns} for p in results]


def load_all_evaluations() -> list[dict[str, Any]]:
    """Load all evaluated settings from the OptiView database.

    Returns:
        list[dict]: List of evaluation dictionaries.
    """
    session = get_optiview_session()
    results = session.query(EvaluatedSetting).all()
    return [{c.name: getattr(e, c.name) for c in e.__table__.columns} for e in results]


def load_symbol_runs(symbol: str) -> pd.DataFrame:
    """Load all historical runs for a given symbol.

    Args:
        symbol (str): Trading symbol.

    Returns:
        pd.DataFrame: DataFrame of runs for the symbol.
    """
    runs = load_all_runs(symbol=symbol)
    return pd.DataFrame(runs)
