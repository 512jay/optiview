# 🛠️ Makefile for OptiView
# Shortcuts to run common development tasks

.PHONY: predict annotate view reset test

predict:
	poetry run python src/optiview/engine/walk_forward/bulk_predict.py

annotate:
	poetry run python src/optiview/engine/walk_forward/annotate_predictions.py

view:
	streamlit run src/optiview/ui/Optiview.py

reset:
	rm -rf generated

predict-single:
	poetry run python src/optiview/engine/walk_forward/predict.py \
	  --month 2025-03 \
	  --symbol EURUSD \
	  --model xgb

quality:
	poetry run python src/optiview/engine/walk_forward/annotate_quality_scores.py
