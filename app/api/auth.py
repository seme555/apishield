from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.schemas.auth import LoginResponse, LoginRequest
from app.utils.security import create_access_token
from app.services.auth import authenticate
from app import models
from app.services import token
from app.services.hash import Hash


auth_router = APIRouter(prefix='', tags=['Auth'])


