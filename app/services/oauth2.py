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
    data: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    ret = token.verify_token(data, credentials_exception, db)
    return ret


def get_current_user_authorization(
    req: Request,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(get_current_user),
):
    # enforcer = casbin.Enforcer("core/model.conf", adapter)
