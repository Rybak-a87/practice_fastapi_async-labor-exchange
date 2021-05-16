# --- 1ый способ
import datetime
#
# from sqlalchemy import Column, Integer, String, Boolean, DateTime


# from .conf_db import Base
#
#
# class UserDB(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     email = Column(String, primary_key=True, unique=True)
#     name = Column(String)
#     password_hash = Column(String)
#     is_company = Column(Boolean, default=False)
#     create_at = Column(DateTime, default=datetime.datetime.utcnow())
#     update_at = Column(DateTime, default=datetime.datetime.utcnow())
#
#     def __repr__(self):
#         return f"User ID: {self.id}"
# --- 1ый способ


# --- 2ой способ
import sqlalchemy
from .conf_db import metadata
import datetime

user = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("is_company", sqlalchemy.Boolean),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
# --- 2ой способ
