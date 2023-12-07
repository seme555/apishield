import os
import json

from app.db.crud import CRUDBase
from app.models import User
from app.schemas.user import UserCreatewithID
from app.utils.security import get_password_hash

from core.logger import logger

userCrud = CRUDBase(model=User)


def push_user_data(db, db_data):
    users = db_data['users']
    for user in users:
        user_in_create = UserCreatewithID(
            id=user['id'],
