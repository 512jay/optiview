#Project Structure

```
Optiview/
│   ├── .streamlit
│   │   ├── config.toml
│   ├── README.md
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
│   ├── generated
│   │   ├── predictions
│   │   │   ├── 2020-05
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-06
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-07
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-08
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-09
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-10
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-11
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2020-12
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-01
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-02
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-03
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-04
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-05
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-06
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-07
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-08
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-09
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-10
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-11
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2021-12
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-01
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-02
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-03
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-04
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-05
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-06
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-07
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-08
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-09
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-10
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-11
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2022-12
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-01
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-02
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-03
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-04
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-05
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-06
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-07
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-08
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-09
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-10
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-11
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2023-12
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-01
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-02
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-03
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-04
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-05
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-06
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-07
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-08
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-09
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-10
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-11
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2024-12
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2025-01
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2025-02
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   ├── 2025-03
│   │   │   │   ├── EURUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   ├── GBPUSD
│   │   │   │   │   ├── cat
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── gbr
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── histgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── lgbm
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── rf
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   │   │   │   │   ├── xgb
│   │   │   │   │   │   ├── annotations.csv
│   │   │   │   │   │   ├── predicted_config_rank_1.ini
│   │   │   │   │   │   ├── predicted_config_rank_2.ini
│   │   │   │   │   │   ├── predicted_config_rank_3.ini
│   │   │   │   │   │   ├── prediction_summary.csv
│   ├── mypy.ini
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── sanitize_predictions.py
│   ├── src
│   │   ├── optiview
│   │   │   ├── __init__.py
│   │   │   ├── app.py
│   │   │   ├── data
│   │   │   │   ├── loader.py
│   │   │   ├── engine
│   │   │   │   ├── walk_forward
│   │   │   │   │   ├── annotate_from_database.py
│   │   │   │   │   ├── bulk_predict.py
│   │   │   │   │   ├── export_ini.py
│   │   │   │   │   ├── predict.py
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
│   │   │   ├── viz
│   │   │   │   ├── boxplot.py
│   │   │   │   ├── heatmap.py
│   │   │   │   ├── histograms.py
│   │   │   │   ├── scatter.py
│   ├── tests
│   │   ├── __init__.py
```
