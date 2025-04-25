# File: scripts/init_db.py

from sqlalchemy import create_engine
from optiview.data.db_path import get_optiview_db_path
from optiview.data.models import Base


def init_db():
    db_path = get_optiview_db_path()
    engine = create_engine(f"sqlite:///{db_path}", future=True)
    Base.metadata.create_all(engine)
    print(f"✅ Initialized OptiView DB at {db_path}")


if __name__ == "__main__":
    init_db()
