# 🛠️ Makefile for OptiView
# Shortcuts to run common development tasks

.PHONY: annotations predictions view reset

predictions:
	poetry run python src/optiview/engine/walk_forward/bulk_predict.py

annotations:
	poetry run python src/optiview/engine/walk_forward/annotate_predictions.py

view:
	streamlit run src/optiview/ui/Optiview.py

reset:
	rm optiview.db
	poetry run python scripts/init_db.py
	make predictions
	make annotations

init:
	poetry run python scripts/init_db.py
