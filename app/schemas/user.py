from pydantic import BaseModel, EmailStr, UUID4
from typing import Optional

from app.schemas.base import AppBaseModel


class UserBasic(BaseModel):
    email: EmailStr
    full_name: str
    organization_name: str = None
    organizational_role: str = None

    class Config:
        from_attributes = True


class UserId(BaseModel):
    id: UUID4
