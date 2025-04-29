# Architecture Overview

## Overview

OptiView integrates with OptiBatch to provide advanced exploratory analysis and predictive modeling for backtest data.

## Key Components

- **OptiBatch**: Automates MT5 strategy tester runs and ingestion into `optibatch.db`.
- **OptiView**: Predicts future performance using historical optimization data (`optiview.db`).
- **Database Layer**: Two separate SQLite databases (`optibatch.db`, `optiview.db`).
- **Maintenance Scripts**: E.g., `sync_jobs.py` for syncing job metadata.
- **Streamlit UI**: Allows users to explore predictions interactively.

## Data Flow

MT5 ➔ OptiBatch ➔ OptiBatch DB ➔ OptiView ➔ Machine Learning ➔ Predictions

---
_More technical diagrams coming soon._
