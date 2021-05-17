import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, validator, constr


class UserModel(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    password_hash: str    # не нужно раскрывать эти данные
    is_company: bool
    create_at: datetime.datetime
    update_at: datetime.datetime

    # class Config:
    #     orm_mode = True


class UserInModel(BaseModel):
    name: str
    email: EmailStr
    password_1: constr(min_length=4)    # минимальная длинна пароля
    password_2: str
    is_company: bool = False

    # кастомный валидатор (соответствие первого и второго переданного пароля)
    @validator("password_2")
    def password_match(cls, pass2, values, **kwargs):
        if "password_1" in values and pass2 != values["password_1"]:
            raise ValueError("Password don't match")
        return pass2
