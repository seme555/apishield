from fastapi import HTTPException, Request, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.services import token
from app import schemas
from app.db.base import engine
from app.db.base import get_db

# import casbin
# import casbin_sqlalchemy_adapter


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/oauth-login")
# adapter = casbin_sqlalchemy_adapter.Adapter(engine)


def get_current_user(
