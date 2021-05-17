from datetime import datetime, timedelta

from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from jose import jwt

from .settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def password_hashed(password: str) -> str:
    """хеширование пароля"""
    return password_context.hash(password)


def verity_password(password: str, hash: str) -> bool:
    """проверка хешированного пароля"""
    return password_context.verify(password, hash)


# работа с токеном (JWT)
def create_access_token(data: dict) -> str:
    """создать токен"""
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})    # добавление даты окончания действия токена
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    """чтение токена"""
    try:
        encoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.JWSError:
        return None
    return encoded_jwt


class JWTBearer(HTTPBearer):
    """защита доступа endpoints"""
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """логика проверки"""
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        exc = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid auth Token")
        if credentials:
            token = decode_access_token(credentials.credentials)
            if token is None:
                raise exc
            return credentials.credentials
        raise exc
