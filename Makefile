# 🛠️ Makefile for OptiView
# Shortcuts to run common development tasks

.PHONY: evaluate predict view reset bulk init run-ui sync-jobs health-check

# Dynamically get the database path
OPTIVIEW_DB_PATH := $(shell poetry run python scripts/database/get_db_path.py)

# Automatically export it to every command
export OPTIVIEW_DB_PATH

# Show what database is being used whenever make runs
$(info Using OptiView database at $(OPTIVIEW_DB_PATH))

# --- Database Management ---
init:
	poetry run python scripts/database/init_db.py

reset:
	@if [ -f $(OPTIVIEW_DB_PATH) ]; then rm $(OPTIVIEW_DB_PATH); fi
	alembic upgrade head
	make sync-jobs
	make bulk
	make evaluate

# --- Prediction / Evaluation ---
bulk:
	poetry run python src/optiview/engine/walk_forward/bulk_predict.py --full-history

predict:
	poetry run python src/optiview/engine/walk_forward/bulk_predict.py

evaluate:
	poetry run python src/optiview/engine/walk_forward/evaluate_predictions.py

# --- User Interface ---
view:
	streamlit run src/optiview/ui/Optiview.py

run-ui:
	set PYTHONPATH=src && poetry run streamlit run src/optiview/ui/app.py --server.headless true --server.runOnSave true

# --- Maintenance Tasks ---
sync-jobs:
	poetry run python scripts/maintenance/sync_jobs.py

health-check:
	poetry run python scripts/maintenance/health_check_optibatch.py