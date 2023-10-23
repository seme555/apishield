from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


class LoginRequest(BaseModel):
    email: EmailStr = None
    password: str

    class Config:
        extra = 'forbid'


class LoginResponse(BaseModel):
    message: str


class Token(BaseModel):
    model_config = ConfigDict(from_attributes=True)
