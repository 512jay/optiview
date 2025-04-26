# File: src/optiview/maintenance/missing_months_report.py

import pandas as pd
from sqlalchemy import select, distinct
from sqlalchemy.orm import Session
from optiview.data.db_path import get_optiview_db_path
from optiview.data.models import PredictedConfig
from sqlalchemy import create_engine
from datetime import datetime
from typing import Optional

def generate_missing_months_report(lookback_months: int = 12) -> pd.DataFrame:
    """
    Scans predicted_configs and reports missing months per (symbol, expert_name).
    
    Args:
        lookback_months: How many months back from today to check.

    Returns:
        DataFrame with missing months per (symbol, expert_name).
    """
    engine = create_engine(f"sqlite:///{get_optiview_db_path()}", future=True)

    with Session(engine) as session:
        stmt = (
            select(
                PredictedConfig.symbol,
                PredictedConfig.expert_name,
                PredictedConfig.month,
            )
            .where(PredictedConfig.month.is_not(None))
        )
        result = session.execute(stmt).all()

    df = pd.DataFrame(result, columns=["symbol", "expert_name", "month"])
    if df.empty:
        return pd.DataFrame()

    # Prepare lookup
    df["month"] = pd.to_datetime(df["month"])
    now = datetime.utcnow()
    cutoff = now.replace(day=1) - pd.DateOffset(months=lookback_months)
    df = df[df["month"] >= cutoff]

    expected_months = pd.date_range(
        start=cutoff, end=now, freq="MS"
    ).strftime("%Y-%m").tolist()

    # Build missing report
    report = []
    for (symbol, expert_name), group in df.groupby(["symbol", "expert_name"]):
        actual_months = group["month"].dt.strftime("%Y-%m").tolist()
        missing = sorted(set(expected_months) - set(actual_months))
        if missing:
            report.append({
                "symbol": symbol,
                "expert_name": expert_name,
                "missing_months": ", ".join(missing),
            })

    return pd.DataFrame(report)

if __name__ == "__main__":
    report = generate_missing_months_report(lookback_months=12)
    if report.empty:
        print("✅ No missing months detected.")
    else:
        print("⚠️ Missing months detected:")
        print(report.to_string(index=False))
