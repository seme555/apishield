# import logging
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app import schemas
from app.services.auth import validate_client_credentials
from app.services.oauth_client import (
    OAuth2ClientCredentialsRequestForm,
    create_client_access_token,
)

token_router = APIRouter(tags=["Token"])


@token_router.post("/token", response_model=schemas.ClientTokenResponse)
