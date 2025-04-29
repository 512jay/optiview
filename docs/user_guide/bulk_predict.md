# Bulk Predict Module (`bulk_predict.py`) Overview

## Purpose
`bulk_predict.py` is responsible for automating model-based prediction of optimal configurations across historical data in OptiView.

## Modes

| Mode | Description |
|:-----|:------------|
| Default (no flags) | Predicts only for the month following the latest available historical month per symbol. |
| `--full-history` | Predicts for **every month** where there is sufficient historical data (rolling window) per symbol. |

## How It Works
1. **Load runs** from the database (OptiBatch results).
2. **Group by symbol**.
3. **Determine months** eligible for prediction:
   - Default: Only latest month + 1.
   - Full-history: After sufficient months have accumulated (`--months_back`).
4. **For each symbol and month:**
   - Train the model.
   - Predict the best configuration.
   - Save prediction to the database.

## CLI Options

| Argument | Description | Default |
|:---------|:-------------|:--------|
| `--months_back` | Minimum number of months of history needed before a prediction can be made. | `3` |
| `--target` | Target column to optimize for (e.g., `profit`). | `profit` |
| `--prediction_col` | Column name for storing predictions. | `predicted_profit` |
| `--prediction_error_penalty` | Penalty weight applied to prediction error in scoring. | `1.0` |
| `--full-history` | Predict across **all months** where enough history exists, not just latest month. | _Off by default_ |

## Example Commands

- Predict only latest month:

```bash
poetry run python src/optiview/engine/walk_forward/bulk_predict.py
```

- Predict across full history:

```bash
poetry run python src/optiview/engine/walk_forward/bulk_predict.py --full-history
```

## Important Notes
- No `Timestamp` or datetime objects are used.
- All months are treated as **strings** formatted as `YYYY-MM`.
- Missing prediction months are automatically checked after bulk prediction.

---

# Project Time Handling Standard (OptiBatch & OptiView)

## Guiding Rule
> **No datetime objects (e.g., pandas.Timestamp) are used in OptiBatch or OptiView.**
>
> **All months and dates must be stored and manipulated as plain strings.**

Example: `"2025-04"` not `Timestamp("2025-04-01")`.

## Reasoning
- Simplifies database structure.
- Avoids cross-library compatibility issues.
- Prevents subtle bugs when merging across systems.

## When to Consider Changing
In the future, if broader datetime manipulation (timezones, day-level granularity, multi-calendar support) becomes necessary, a **controlled migration plan** can be initiated to introduce datetime types systematically.

Until that time, **string months remain the enforced standard.**

## Development Reminder
Whenever adding new fields, query logic, or database models:
- If handling dates/months, **keep them as `str`**.
- Avoid `.strftime()`, `.to_period()`, or `.to_timestamp()` unless absolutely needed and carefully documented.

---

✅ Last updated: {{ 2025-04-25 }}

---

