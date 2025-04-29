# scripts/init_db.py

import sys
from pathlib import Path

# Add the project src/ folder to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from sqlalchemy import create_engine
from optiview.database.db_paths import get_optiview_db_path
from optiview.database.models import Base


def init_db():
    db_path = get_optiview_db_path()
    engine = create_engine(f"sqlite:///{db_path}", future=True)
    Base.metadata.create_all(engine)
    print(f"✅ Initialized OptiView DB at {db_path}")


if __name__ == "__main__":
    init_db()
