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

