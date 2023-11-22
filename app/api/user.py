from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.db.base import get_db
from app.db.crud import CRUDBase
from app.services.oauth2 import add_new_role_in_org
from app.utils.invitation import confirm_invitation_token
from app.utils.security import get_password_hash

user_router = APIRouter(prefix="/user", tags=["User"])
user_crud = CRUDBase(model=models.User)


