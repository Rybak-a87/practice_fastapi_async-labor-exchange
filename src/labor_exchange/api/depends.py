# ---
# зависимости
# ---
from fastapi import Depends, HTTPException, status

from ..config.security import JWTBearer, decode_access_token
from ..database.conf_db import database
from ..services.users import UserService
from ..models.users import UserModel


def get_user_service() -> UserService:
    """возвращает сервис"""
    return UserService(database=database)


async def get_current_user(
        user_service: UserService = Depends(get_user_service),
        token: str = Depends(JWTBearer())
) -> UserModel:
    """возвращает пользователя"""
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid"),
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await user_service.get_user_by_email(email=email)
    if user is None:
        raise cred_exception
    return user
