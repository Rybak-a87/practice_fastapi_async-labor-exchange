# ---
# для работы с переменными окружения
# ---
# --- 1ый способ
# from pydantic import BaseSettings
#
#
# class Settings(BaseSettings):
#     SERVER_HOST: str = "127.0.0.1"
#     SERVER_PORT: int = 8000
#     DATABASE_URL: str = "postgresql://user:password@localhost:80/name_db"

#     ACCESS_TOKEN_EXPIRE_MINUTES = 60
#     ALGORITHM = "HS256"
#     SECRET_KEY = "5STetuomLYYJWJeQ4GI3Wcb_O26zBSBPHaeZ-f_pMYk"
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
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="5STetuomLYYJWJeQ4GI3Wcb_O26zBSBPHaeZ-f_pMYk")
# --- 2ой способ
