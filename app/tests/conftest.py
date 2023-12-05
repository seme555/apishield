import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base
from app.db.base import get_db
from core.config import settings
from main import app
from app import schemas
from app.tests.utils.utils import push_data_into_test_db
from app.services.oauth2 import get_current_user_authorization


engine = create_engine(settings.TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
Base.metadata.create_all(bind=engine, checkfirst=True)

db = TestingSessionLocal()


def get_current_user_authorization_override():
    mock_user = schemas.TokenData(
        email='testuser@example.com',
        full_name='test user full name',
        organization_name='test',
        role='admin'
    )
    return mock_user


@pytest.fixture
def test_db():
