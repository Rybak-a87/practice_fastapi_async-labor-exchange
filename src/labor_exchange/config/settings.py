# ---
# для работы с переменными окружения
# ---
# --- 1ый способ
# from pydantic import BaseSettings
#
#
# class Settings(BaseSettings):
#     server_host: str = "127.0.0.1"
#     server_port: int = 8000
#     database_url: str = "postgresql://user:password@localhost:80/name_db"
#
#
# settings = Settings(
#     _env_file=".env",
#     _env_file_encoding="utf-8"
# )
# --- 1ый способ


# --- 2ой способ
from starlette.config import Config

config = Config(".env")

DATABASE_URL = config(
    "EE_DATABASE_URL",    # имя переменной
    cast=str,    # преобразовывать переменные в строку
    default="postgresql://user:password@127.0.0.1:80/name_db"    # значение переменной по умолчанию
)
# --- 2ой способ
