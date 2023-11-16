from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.params import Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from app import models, schemas
from app.db.base import get_db
from app.db.crud import CRUDBase
from app.services.oauth2 import get_current_user, get_current_user_authorization
from app.utils.invitation import generate_invitation_token, confirm_invitation_token
from app.services.mail import send_email_background
from core.config import settings
from app.models import User
from core.logger import logger
from app.worker.celery import send_email_task


invitation_router = APIRouter(prefix='/invitation', tags=['Invitation'])
invitation_crud = CRUDBase(model=models.Invitation)


@invitation_router.get('')
def get_invitations(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_authorization)
) -> List[schemas.Invitation]:
    db_invitations = db.query(models.Invitation)
    return db_invitations


@invitation_router.post('/invite')
def invite(
    background_tasks: BackgroundTasks,
    invitation_data: schemas.InvitationCreateRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_authorization)
):
    unique_token = generate_invitation_token(data=invitation_data)
    created_by = db.query(User).filter(User.email == current_user.email).first()

    new_invitation = schemas.InvitationCreate(
        full_name=invitation_data.full_name,
        email=invitation_data.email,
        organization=invitation_data.organization,
        organizational_role=invitation_data.organizational_role,
        role=invitation_data.role,
        unique_token=unique_token,
        created_by_id=created_by.id
    )

    new_invitation.model_dump()
    _ = invitation_crud.create(db=db, obj_in=new_invitation)
