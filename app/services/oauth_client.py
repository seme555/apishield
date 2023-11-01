import warnings
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional

from fastapi import Header
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Form
from fastapi.security.oauth2 import OAuth2, OAuthFlowsModel
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

from core.config import settings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message="int_from_bytes is deprecated")
    from jose import JWTError, jwt


def create_client_access_token(
    data: dict,
    expires_delta: timedelta,
    secret_key: str,
    now: Optional[datetime] = None,
) -> str:
    to_encode = data.copy()
    expire = (now or datetime.now(timezone.utc)) + expires_delta
    to_encode["exp"] = expire
    encoded_jwt: str = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt


def get_subject_from_token(token: str =  Header(alias='Authorization')):#, secret_key: str='secret'):
    try:
        payload = jwt.decode(token, settings.OAUTH_CLIENT_SECRET, algorithms=["HS256"])
        sub = payload["sub"]
