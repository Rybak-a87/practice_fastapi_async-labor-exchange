# --- 1ый способ
# from .users import UserDB
# from .jobs import JobDB
# from .conf_db import Base, engine
#
#
# Base.metadata.create_all(bind=engine)
# --- 1ый способ

# --- 2ой способ
from .users import user
from .jobs import job
from .conf_db import metadata, engine


metadata.create_all(bind=engine)
# --- 2ой способ
