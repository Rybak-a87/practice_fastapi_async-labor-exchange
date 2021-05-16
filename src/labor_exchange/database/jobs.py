# --- 1ый способ
# import datetime
#
# from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
#
# from .conf_db import Base
#
#
# class JobDB(Base):
#     __tablename__ = "job"
#     id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
#     title = Column(String)
#     description = Column(String)
#     salary_from = Column(Integer)
#     salary_to = Column(Integer)
#     is_active = Column(Boolean, default=False)
#     create_at = Column(DateTime, default=datetime.datetime.utcnow())
#     update_at = Column(DateTime, default=datetime.datetime.utcnow())
#
#     def __repr__(self):
#         return f"Job ID: {self.id}"
# --- 1ый способ


# --- 2ой способ
import sqlalchemy
from .conf_db import metadata
import datetime

job = sqlalchemy.Table(
    "job",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("salary_from", sqlalchemy.Integer),
    sqlalchemy.Column("salary_to", sqlalchemy.Integer),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
# --- 2ой способ
