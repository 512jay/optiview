## OptiView Database Schema

This document describes the current **database tables** managed by OptiView.

---

## Tables

### 1. `predicted_settings`

Stores machine learning predictions of top settings.

| Column              | Type         | Description                                |
|---------------------|--------------|--------------------------------------------|
| `version`           | `String`     | Version tag of prediction engine (nullable) |
| `month`             | `String`     | Month predicted (e.g., '2025-03') **[PK]** |
| `symbol`            | `String`     | Symbol (e.g., 'EURUSD') **[PK]** |
| `model`             | `Enum(ModelType)` | ML model used (e.g., 'xgb') **[PK]** |
| `rank`              | `Integer`    | Rank of prediction within month **[PK]** |
| `predicted_profit`  | `Float`      | Predicted profit for setting |
| `confidence_score`  | `Float` (nullable) | Confidence level (0.0 - 1.0) |
| `confidence_stars`  | `String` (nullable) | Human-readable stars (e.g., '★★★☆☆') |
| `inputs`            | `JSON`       | Input parameters predicted |
| `run_id`            | `Integer` (nullable) | Link to original OptiBatch run |
| `tags`              | `JSON`       | User tags (default empty list) |
| `notes`             | `Text` (nullable) | User notes |
| `created_at`        | `DateTime`   | Record creation timestamp |
| `updated_at`        | `DateTime`   | Record last update timestamp |
| `params_json`       | `JSON` (nullable) | Copy of original training parameters |

🔹 **Primary Key**: (`month`, `symbol`, `model`, `rank`)

---

### 2. `evaluated_settings`

Stores the evaluation results of previously predicted settings.

| Column                  | Type         | Description                                  |
|---------------------------|--------------|----------------------------------------------|
| `id`                     | `Integer`    | Primary key (auto-increment) |
| `month`                  | `String`     | Prediction month evaluated |
| `symbol`                 | `String`     | Symbol |
| `model`                  | `Enum(ModelType)` | Model name |
| `rank`                   | `Integer`    | Rank associated |
| `evaluator_version`      | `String`     | Evaluation engine version |
| `quality_score`          | `Float` (nullable) | Evaluation score |
| `quality_stars`          | `String` (nullable) | Human-readable star rating |
| `confidence_score`       | `Float` (nullable) | ML predicted confidence at eval time |
| `confidence_stars`       | `String` (nullable) | Human-readable confidence stars |
| `notes`                  | `Text` (nullable) | Human notes |
| `metrics_json`           | `JSON` (nullable) | Additional evaluation metrics |
| `evaluated_at`           | `DateTime`   | Timestamp when evaluated |

🔹 **Primary Key**: (`id`)

---

### 3. `synced_jobs`

Stores lightweight copies of job metadata from the original OptiBatch `jobs` table.

| Column                  | Type         | Description                                  |
|---------------------------|--------------|----------------------------------------------|
| `id`                     | `String`     | Job ID **[PK]** |
| `expert_name`            | `String`     | Name of expert advisor (e.g., 'IndyTSL_v2') |
| `expert_path`            | `String`     | Path to expert file (e.g., 'Shared Projects/IndyTSL/IndyTSL_v2_0.ex5') |
| `period`                 | `String`     | MT5 timeframe (e.g., 'H1') |
| `deposit`                | `Float`      | Deposit amount (e.g., 1000.0) |
| `currency`               | `String`     | Deposit currency (e.g., 'USD') |
| `leverage`               | `String`     | Leverage ratio (e.g., '100') |
| `model`                  | `String` (nullable) | Strategy testing model |
| `optimization_mode`      | `String` (nullable) | Optimization mode |
| `optimization_criterion` | `String` (nullable) | Optimization criterion |
| `tester_inputs`          | `JSON`       | Tester inputs (full .ini file params) |
| `created_at`             | `DateTime`   | Timestamp when synced into OptiView |

🔹 **Primary Key**: (`id`)

---

## Notes

- `params_json` in `predicted_settings` captures **the exact training input parameters** used.
- `inputs` in `predicted_settings` captures **only the optimized inputs** chosen by the ML model.
- `synced_jobs` is **synced separately** from the live OptiBatch database.
- **Enum `ModelType`** includes:
  - `xgb` (XGBoost)
  - `rf` (Random Forest)
  - `gbr` (Gradient Boosting)
  - `histgb` (Histogram Gradient Boosting)
  - `lgbm` (LightGBM)
  - `cat` (CatBoost)

---

