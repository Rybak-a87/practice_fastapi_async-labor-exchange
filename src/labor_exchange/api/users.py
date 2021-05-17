from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from .depends import get_user_service, get_current_user
from ..models.users import UserModel, UserInModel
from ..services.users import UserService


router = APIRouter()


@router.get("/get-users-list", response_model=List[UserModel])
async def get_users_list(
        limit: int = 100,
        skip: int = 0,
        user_service: UserService = Depends(get_user_service)
):
    """
    ## Получение списка пользователей
    \f
    :param limit:
    :param skip:
    :param user_service:
    :return:
    """
    return await user_service.get_users_all(limit=limit, skip=skip)


@router.post("/create-user", response_model=UserModel)
async def create_user(
        user: UserInModel,
        user_service: UserService = Depends(get_user_service)
):
    """
    ## Создание пользователя
    """
    return await user_service.create_user(user=user)


@router.put("/update-user", response_model=UserModel)
async def update_user(
        id: int,
        user: UserInModel,
        user_service: UserService = Depends(get_user_service),
        current_user: UserModel = Depends(get_current_user)
):
    """
    ## Обновление данных пользователя
    """
    # если пользователь пытается изменить нек себя
    print("1")
    old_user = await user_service.get_user_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await user_service.update_user(id=id, user=user)
