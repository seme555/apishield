import pytest

from app.tests.factories import UserFactory, CasbinRuleFactory

from core.logger import logger


def test_login_logout_successful(client, test_db):
    # Setup 1: Create a test user
    test_user = UserFactory(session=test_db)

    # Setup 2: Define role permission for the user
    _ = CasbinRuleFactory(
        v0=test_user.email,
        v1=test_user.role,
        v2=test_user.organization_name
    )

