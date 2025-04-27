# 🛠️ Makefile for OptiView
# Shortcuts to run common development tasks

.PHONY: evaluate predict evaluate view reset bulk init

bulk:
	poetry run python src/optiview/engine/walk_forward/bulk_predict.py --full-history

predict:
	poetry run python src/optiview/engine/walk_forward/bulk_predict.py

evaluate:
	poetry run python src/optiview/engine/walk_forward/evaluate_predictions.py

view:
	streamlit run src/optiview/ui/Optiview.py

reset:
	rm src/optiview/data/optiview.db
	poetry run python scripts/init_db.py
	make bulk
	make evaluate

init:
	poetry run python scripts/init_db.py
