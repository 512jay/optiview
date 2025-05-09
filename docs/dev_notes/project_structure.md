<!-- AUTO-GENERATED FILE - DO NOT EDIT -->
# 🗂️ OptiView Project Structure

_Generated on 2025-04-29 02:32:00_

- 📂 .streamlit/
  - 📄 config.toml
- 📄 Makefile
- 📄 README.md
- 📂 alembic/
  - 📄 README
  - 📄 env.py
  - 📄 script.py.mako
  - 📂 versions/
    - 📄 17e405df967f_add_synced_jobs_table.py
    - 📄 30dd7ec0b96a_initial_database_schema.py
    - 📄 c14cd3dbed5f_remove_expert_advisor_from_.py
    - 📄 c601aadfc9d1_add_params_json_to_predicted_settings.py
- 📄 alembic.ini
- 📂 catboost_info/
  - 📄 catboost_training.json
  - 📂 learn/
    - 📄 events.out.tfevents
  - 📄 learn_error.tsv
  - 📄 time_left.tsv
  - 📂 tmp/
- 📂 db/
- 📂 docs/
  - 📂 dev_notes/
    - 📄 [architecture_overview.md](../dev_notes/architecture_overview.md)
    - 📄 [optiview_schema.md](../dev_notes/optiview_schema.md)
    - 📄 [project_structure.md](../dev_notes/project_structure.md)
  - 📄 [index.md](../index.md)
  - 📂 user_guide/
    - 📄 [bulk_predict.md](../user_guide/bulk_predict.md)
    - 📄 [maintenance.md](../user_guide/maintenance.md)
    - 📄 [theory_and_setup.md](../user_guide/theory_and_setup.md)
- 📂 generated/
  - 📂 health_check/
    - 📄 optibatch_health_report.csv
- 📄 mkdocs.yml
- 📄 mypy.ini
- 📄 poetry.lock
- 📄 project_state.yaml
- 📄 pyproject.toml
- 📂 scripts/
  - 📂 database/
    - 📄 get_db_path.py
    - 📄 init_db.py
  - 📂 maintenance/
    - 📄 health_check_optibatch.py
    - 📄 sync_jobs.py
- 📂 src/
  - 📂 optiview/
    - 📂 data/
      - 📄 ini_tools.py
      - 📄 join_tools.py
    - 📂 database/
      - 📄 db_paths.py
      - 📄 loader.py
      - 📄 models.py
      - 📄 query.py
      - 📄 session.py
    - 📂 engine/
      - 📂 walk_forward/
        - 📄 bulk_predict.py
        - 📄 evaluate_predictions.py
        - 📄 model_configs.py
        - 📄 predict.py
        - 📄 scoring_helpers.py
        - 📄 time_utils.py
        - 📄 train_model.py
    - 📂 maintenance/
      - 📄 missing_months_report.py
    - 📂 ml/
      - 📄 baseline_model.py
      - 📄 model_comparison.py
      - 📄 predict_next_month.py
      - 📄 walk_forward_model.py
    - 📂 ui/
      - 📄 app.py
      - 📂 components/
        - 📄 header.py
      - 📂 pages/
        - 📄 01_View_Predictions.py
        - 📄 03_Admin_Tools.py
      - 📂 utils/
        - 📄 data_loader.py
    - 📂 viz/
      - 📄 boxplot.py
      - 📄 heatmap.py
      - 📄 histograms.py
      - 📄 scatter.py
- 📂 tests/
  - 📄 __init__.py
  - 📂 engine/
    - 📂 walk_forward/
      - 📄 test_predict.py


> ℹ️ **Note:** Files inside `/docs/` are clickable links.
