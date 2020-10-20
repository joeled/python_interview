
from user_service.user import UserServiceFactory
from user_service.test import MockUserListener

FACTORY = UserServiceFactory.create_factory({})
USER_SERVICE = FACTORY.create_service()

ID_1 = 4
ID_2 = 5
NAME_1 = "spam"
MOCK_USER_LISTENER = MockUserListener()
USER_SERVICE.add_user_listener(MOCK_USER_LISTENER)


def add_user():
    name2 = "Yun"

    employee = USER_SERVICE.create_user(ID_1, NAME_1, "ham")

    assert len(MOCK_USER_LISTENER.users_created) == 1

    USER_SERVICE.create_user(ID_2, name2, "eggs")

    assert len(MOCK_USER_LISTENER.users_created) == 2

    employee_res = USER_SERVICE.get_user(ID_1)
    assert ID_1 == employee_res.id_
    assert NAME_1 == employee_res.first_name

    employee_res_2 = USER_SERVICE.get_user(ID_2)
    assert ID_2 == employee_res_2.id_
    assert name2 == employee_res_2.first_name


def test_add_user():
    add_user()
