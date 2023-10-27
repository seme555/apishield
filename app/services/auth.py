from jose import jwt
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends, Cookie
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from typing import Optional,Union, Any

from app.db.base import get_db
from app.db.crud import CRUDBase
from app import models
from core.config import settings
from core.logger import logger
from app.schemas.auth import TokenPayload
from app.services.oauth_client import OAuth2ClientCredentials

from app.utils.security import verify_password


