import factory
from faker import Faker
from app.models import User

from app.tests.conftest import TestingSessionLocal
from app.utils.security import get_password_hash

fake = Faker()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session_persistence = "commit"

    full_name = factory.Faker('name')
    email = factory.LazyAttribute(lambda _: fake.email())
    organization_name = factory.Faker('company')
