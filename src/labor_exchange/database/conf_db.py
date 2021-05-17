# ---
# подключение к базе данных
# ---
from databases import Database
from sqlalchemy import create_engine#, MetaData
from sqlalchemy.ext.declarative import declarative_base

from ..config.settings import DATABASE_URL

# подключение
database = Database(DATABASE_URL)


engine = create_engine(    # только для синхронных запросов к базе
    DATABASE_URL,
)

# --- 1ый способ
Base = declarative_base()

# --- 2ой способ
# metadata = MetaData()
