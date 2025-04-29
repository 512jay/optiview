# File: src/optiview/maintenance/missing_months_report.py

"""Generate reports for missing prediction months in OptiView database."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from optiview.database.loader import get_optiview_db_path
from optiview.database.models import PredictedSetting


def generate_missing_months_report(lookback_months: int = 12) -> pd.DataFrame:
    """Scan predicted_settings and report missing months per (symbol, expert_name).

    Args:
        lookback_months (int): How many months back from today to check.

    Returns:
        pd.DataFrame: DataFrame with missing months per (symbol, expert_name).
    """
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

    with Session(engine) as session:
        stmt = select(
            PredictedSetting.symbol,
            PredictedSetting.expert_name,
            PredictedSetting.month,
        ).where(PredictedSetting.month.is_not(None))
        result = session.execute(stmt).all()

    df = pd.DataFrame(result, columns=["symbol", "expert_name", "month"])
    if df.empty:
        return pd.DataFrame()

    # Prepare lookup
    df["month"] = pd.to_datetime(df["month"])
    now = datetime.utcnow()
    cutoff = now.replace(day=1) - pd.DateOffset(months=lookback_months)
    df = df[df["month"] >= cutoff]

    expected_months = (
        pd.date_range(start=cutoff, end=now, freq="MS").strftime("%Y-%m").tolist()
    )

    # Build missing report
    report = []
    for (symbol, expert_name), group in df.groupby(["symbol", "expert_name"]):
        actual_months = group["month"].dt.strftime("%Y-%m").tolist()
        missing = sorted(set(expected_months) - set(actual_months))
        if missing:
            report.append(
                {
                    "symbol": symbol,
                    "expert_name": expert_name,
                    "missing_months": ", ".join(missing),
                }
            )

    return pd.DataFrame(report)


if __name__ == "__main__":
    report = generate_missing_months_report(lookback_months=12)
    if report.empty:
        print("✅ No missing months detected.")
    else:
        print("⚠️ Missing months detected:")
        print(report.to_string(index=False))
