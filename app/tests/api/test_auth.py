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

    # Action: Make a request to the login endpoint
    response = client.post(
        "api/login",
        json={"email": test_user.email, 'password': 'password'}
    )

    # Assertions
    assert response.status_code == 200
    assert response.json()["message"] == "login successful"
    assert "authorization" in response.cookies

    logout_response = client.post("api/logout")

    # Assertions
    assert logout_response.status_code == 200
    assert logout_response.json()["message"] == "logout successful"
    assert "authorization" not in logout_response.cookies


def test_login_with_invalid_credentials_raises_error(client):
    # Action: Make a request to the login endpoint
    response = client.post(
        "api/login",
        json={'email': 'unknown@test.com', 'password': 'wrong_password'}
    )

    # Action & Assertion: Invalid password
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect email or password"
    assert "authorization" not in response.cookies


def test_oauth_login_successful(client, test_db):
    # Setup 1: Create a test user
    test_user = UserFactory(session=test_db)
    
