# scripts/database/get_db_path.py

import sys
from pathlib import Path

# Add the project src/ folder to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))


"""Return the absolute OptiView database path."""

from optiview.database.db_paths import get_optiview_db_path

if __name__ == "__main__":
    print(get_optiview_db_path().resolve())
