from typing import Optional
import datetime
from typing import List

from . import BaseService
from ..config import security
from ..database.users import UserDB
from ..models.users import UserInModel, UserModel


class UserService(BaseService):
    user_db = UserDB.__table__    # для работы декларативных таблиц с модулем databases (вместо сессий - query)

    async def get_users_all(
            self,
            limit: int = 100,    # максимальное количество пользователей которое можно получить
            skip: int = 0    # сколько пользователей пропустить для реализации пагинации
    ) -> List[UserModel]:
        """Получение списка пользователей"""
        query = self.user_db.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_user_by_id(self, id: int) -> UserModel:
        """Вывод пользователя по id"""
        query = self.user_db.select().where(self.user_db.c.id == id)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return UserModel.parse_obj(user)

    async def get_user_by_email(self, email: str) -> UserModel:
        """Получение пользователя по email"""
        query = self.user_db.select().where(self.user_db.c.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return UserModel.parse_obj(user)

    async def create_user(self, user: UserInModel) -> UserModel:
        """Создание пользователя"""
        new_user = UserModel(
            name=user.name,
            email=user.email,
            password_hash=security.password_hashed(user.password_1),
            is_company=user.is_company,
            create_at=datetime.datetime.utcnow(),
            update_at=datetime.datetime.utcnow()
        )
        values = {**new_user.dict()}
        values.pop("id", None)

        query = self.user_db.insert().values(**values)
        new_user.id = await self.database.execute(query=query)
        return new_user

    async def update_user(self, id: int, user: UserInModel) -> UserModel:
        """Обновление данных пользователя"""
        update_user = UserModel(
            id=id,
            name=user.name,
            email=user.email,
            password_hash=security.password_hashed(user.password_1),
            is_company=user.is_company,
            create_at=datetime.datetime.utcnow(),
            update_at=datetime.datetime.utcnow()
        )
        values = {**update_user.dict()}
        values.pop("create_at", None)
        values.pop("id", None)
        for k, v in values.items():
            print(k, v)
        query = self.user_db.update().where(self.user_db.c.id == id).values(**values)
        await self.database.execute(query)
        return update_user
