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


@user_router.post("", response_model=schemas.UserDetails)
def create_user(data: schemas.UserCreateRequest, db: Session = Depends(get_db)):
    token_data = confirm_invitation_token(token=data.token)
    invitation = db.query(models.Invitation).filter_by(unique_token=data.token).first()

    if data.password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Password did not match")

    if not token_data or not invitation or invitation.expires_at < datetime.now():
        raise HTTPException(
            status_code=400, detail="Invalid information or expired invitation link"
        )

    existing_user = (
        db.query(models.User).filter(models.User.email == invitation.email).first()
    )
    if existing_user:
        raise HTTPException(
