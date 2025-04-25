To transition OptiView from reading Parquet files to querying a SQLite database, you’ll need to:

---

### ✅ 1. **Update Data Source Logic**
Replace the Parquet file loading logic with SQL queries using `sqlite3` or `SQLAlchemy`.

**Before (Parquet):**
```python
import pandas as pd

df = pd.read_parquet("generated/predictions/2025-03/EURUSD/xgb/predicted_configs.parquet")
```

**After (SQLite):**
```python
import sqlite3
import pandas as pd
import os

db_path = os.getenv("OPTIVIEW_DB_PATH", "optibatch.sqlite")
conn = sqlite3.connect(db_path)

query = """
SELECT * FROM predicted_configs
WHERE symbol = 'EURUSD' AND model = 'xgb' AND month = '2025-03'
"""
df = pd.read_sql_query(query, conn)
conn.close()
```

---

### ✅ 2. **Adjust Streamlit Selectors**
Replace the logic behind dropdown population to reflect distinct values from the database instead of reading directory paths.

```python
symbols = pd.read_sql_query("SELECT DISTINCT symbol FROM predicted_configs", conn)["symbol"].tolist()
months = pd.read_sql_query(f"SELECT DISTINCT month FROM predicted_configs WHERE symbol = ?", conn, params=(selected_symbol,))["month"].tolist()
```

---

### ✅ 3. **Replace Parquet Output Pipeline**
Update any script that writes to Parquet so it now inserts into SQLite.

**Before:**
```python
df.to_parquet("predicted_configs.parquet")
```

**After:**
```python
df.to_sql("predicted_configs", conn, if_exists="append", index=False)
```

Make sure your DataFrame columns exactly match the schema defined in the database.

---

### ✅ 4. **Ensure Alembic Migration is Ready**
You’ll want to support future schema evolution. If not already set up:

- Create an `alembic/` folder and base version.
- Track changes to tables like `predicted_configs`, `quality_scores`, etc.

---

### ✅ 5. **Verify Data Consistency**
Write a migration script to:
- Read existing `.parquet` files
- Insert them into `predicted_configs` or related tables

Optional tool:
```bash
python scripts/migrate_parquet_to_db.py
```

---

### ✅ 6. **Update `.streamlit/secrets.toml` or `.env`**
Use `OPTIVIEW_DB_PATH` to reference the SQLite file instead of hardcoding it.

---

### ✅ 7. **Document the Migration**
Add a note in `dev_notes.md`:

```markdown
✅ April 2025 — Switched from Parquet to SQLite
- All prediction, confidence, and quality data now queried from SQLite
- UI now fully dynamic, database-driven
```

---

Would you like me to draft the initial schema, update loader functions, or create the migration script from `.parquet` to `.db`?