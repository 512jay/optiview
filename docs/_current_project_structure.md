#Project Structure

```
Optiview/
│   ├── .streamlit
│   │   ├── config.toml
│   ├── Makefile
│   ├── README.md
│   ├── alembic
│   │   ├── README
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   ├── versions
│   │   │   ├── bec65ff74ae3_initial_composite_schema.py
│   ├── alembic.ini
│   ├── catboost_info
│   │   ├── catboost_training.json
│   │   ├── learn
│   │   │   ├── events.out.tfevents
│   │   ├── learn_error.tsv
│   │   ├── time_left.tsv
│   │   ├── tmp
│   ├── db
│   ├── docs
│   │   ├── _current_project_structure.md
│   │   ├── bulk_predict.md
│   │   ├── transition_to_sqlite.md
│   │   ├── walk_forward_eda.md
│   ├── mypy.ini
│   ├── poetry.lock
│   ├── project_state.yaml
│   ├── pyproject.toml
│   ├── sanitize_predictions.py
│   ├── scripts
│   │   ├── init_db.py
│   ├── src
│   │   ├── optiview
│   │   │   ├── __init__.py
│   │   │   ├── app.py
│   │   │   ├── data
│   │   │   │   ├── db_path.py
│   │   │   │   ├── join_tools.py
│   │   │   │   ├── loader.py
│   │   │   │   ├── models.py
│   │   │   ├── engine
│   │   │   │   ├── walk_forward
│   │   │   │   │   ├── annotate_predictions.py
│   │   │   │   │   ├── bulk_predict.py
│   │   │   │   │   ├── export_ini.py
│   │   │   │   │   ├── predict.py
│   │   │   │   │   ├── scoring.py
│   │   │   │   │   ├── train.py
│   │   │   ├── maintenance
│   │   │   │   ├── missing_months_report.py
│   │   │   ├── ml
│   │   │   │   ├── baseline_model.py
│   │   │   │   ├── model_comparison.py
│   │   │   │   ├── predict_next_month.py
│   │   │   │   ├── walk_forward_model.py
│   │   │   ├── test_loader.py
│   │   │   ├── ui
│   │   │   │   ├── OptiView.py
│   │   │   │   ├── pages
│   │   │   │   │   ├── 01_View_Predictions.py
│   │   │   │   │   ├── 02_Run_Predictions.py
│   │   │   │   ├── queries.py
│   │   │   │   ├── tabs
│   │   │   │   │   ├── home_tab.py
│   │   │   │   │   ├── run_predictions_tab.py
│   │   │   │   │   ├── view_predictions_tab.py
│   │   │   │   ├── ui_components.py
│   │   │   ├── viz
│   │   │   │   ├── boxplot.py
│   │   │   │   ├── heatmap.py
│   │   │   │   ├── histograms.py
│   │   │   │   ├── scatter.py
│   ├── tests
│   │   ├── __init__.py
│   ├── theory_and_setup.md
```
