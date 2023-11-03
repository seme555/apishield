import secrets
from itsdangerous import URLSafeTimedSerializer as Serializer

from core.config import settings


def generate_invitation_token(data) -> str:
    """
    Generates a secure token for email invitations.
    Args: email, full_name, organization, organizational_role, role
    Returns: str: A secure and unique token.
    """
    serializer = Serializer(
        settings.INVITATION_URL_SECRET_KEY,
        salt=settings.INVITATION_URL_SECURITY_PASSWORD_SALT
    )
    unique_id = str(secrets.token_urlsafe())
    token_data = data.__dict__
