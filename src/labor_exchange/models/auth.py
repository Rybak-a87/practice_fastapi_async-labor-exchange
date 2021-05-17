from pydantic import BaseModel, EmailStr


class TokenModel(BaseModel):
    access_token: str
    token_type: str


class LoginModel(BaseModel):
    email: EmailStr
    password: str
