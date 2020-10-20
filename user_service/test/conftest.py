import pytest

from user_service.user import UserServiceFactory

factory = UserServiceFactory.create_factory({})


@pytest.fixture(scope="session")
def user_service():
    return factory.create_service()
