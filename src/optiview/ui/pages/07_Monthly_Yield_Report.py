# File: streamlit_app/07_Monthly_Yield_Report.py

import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from optiview.database.session import get_optiview_session
from optiview.database.models import EvaluatedSetting
from sqlalchemy import select
from collections import defaultdict

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(page_title="Monthly Yield Report", layout="wide")
st.title("📈 Monthly Yield Report (Based on $1,000 Deposit)")

# ------------------------------
# Database Access
# ------------------------------
session = get_optiview_session()

# ------------------------------
# Query Evaluated Settings (rank=1 only)
# ------------------------------
st.info(
    "This report selects the *rank 1* configuration with the **highest actual profit** per month."
)

stmt = select(EvaluatedSetting).where(EvaluatedSetting.rank == 1)
results = session.scalars(stmt).all()
session.close()

# Group by (month, symbol, model)
data_by_month = defaultdict(list)
for row in results:
    key = row.month
    data_by_month[key].append(row)

# Sort months descending
sorted_months = sorted(data_by_month.keys(), reverse=True)

# Extract all symbols
all_symbols = sorted({r.symbol for r in results})
selected_symbol = st.selectbox(
    "Filter by Symbol (optional):", options=["All"] + all_symbols
)

report_rows = []

for month in sorted_months:
    entries = data_by_month[month]

    if selected_symbol != "All":
        entries = [e for e in entries if e.symbol == selected_symbol]

    if not entries:
        report_rows.append({"Month": month, "Status": "Missing"})
        continue

    # Find config with highest actual_result
    best = max(
        entries,
        key=lambda x: x.actual_result if x.actual_result is not None else float("-inf"),
    )

    if best.actual_result is None:
        report_rows.append({"Month": month, "Status": "Missing"})
        continue

    yield_percent = (best.actual_result / 1000.0) * 100
    report_rows.append(
        {
            "Month": month,
            "Symbol": best.symbol,
            "Model": best.model,
            "Profit ($)": round(best.actual_result, 2),
            "Yield (%)": round(yield_percent, 2),
            "Status": "OK",
        }
    )

# Display report
report_df = pd.DataFrame(report_rows)
st.dataframe(report_df, use_container_width=True)

# Chart
chart_data = report_df[report_df["Status"] == "OK"]
if not chart_data.empty:
    st.line_chart(chart_data.set_index("Month")["Yield (%)"].sort_index())

# CSV Export
csv = report_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download CSV", csv, "monthly_yield_report.csv", "text/csv")
