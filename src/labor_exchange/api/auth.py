from fastapi import APIRouter, Depends, HTTPException, status

from ..models.auth import TokenModel, LoginModel
from ..services.users import UserService
from ..config.security import verity_password, create_access_token
from .depends import get_user_service

router = APIRouter()


@router.post("/login", response_model=TokenModel)
async def login(login: LoginModel, user_service: UserService = Depends(get_user_service)):
    """
    ## Авторизация
    """
    user = await user_service.get_user_by_email(email=login.email)
    if user is None or not verity_password(login.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password"
        )
    return TokenModel(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
