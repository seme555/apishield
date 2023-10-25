from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional
from datetime import datetime
from app.schemas import UserBasic


class InvitationCreateRequest(BaseModel):
    full_name: str
    email: EmailStr
    organization: str
    organizational_role: str
    role: str

    class Config:
        from_attributes = True
        validate_assignment = True


