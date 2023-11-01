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

