from fastapi import APIRouter

from .users import router as users_router
from .auth import router as auth_router

router = APIRouter()


router.include_router(users_router, prefix="/user", tags=["Пользователи"])
router.include_router(auth_router, prefix="/auth", tags=["Авторизация - Регистрация"])
