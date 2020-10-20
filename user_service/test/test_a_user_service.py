
from user_service.user import UserServiceFactory

FACTORY = UserServiceFactory.create_factory({})
USER_SERVICE = FACTORY.create_service()

ID_1 = 4
ID_2 = 5
NAME_1 = "spam"


def test_add_user():
    name2 = "Yun"

    employee = USER_SERVICE.create_user(ID_1, NAME_1, "ham")
    assert ID_1 == employee.id_
    assert NAME_1 == employee.first_name

    USER_SERVICE.create_user(ID_2, name2, "eggs")

    employee_res = USER_SERVICE.get_user(ID_1)
    assert ID_1 == employee_res.id_
    assert NAME_1 == employee_res.first_name

    employee_res_2 = USER_SERVICE.get_user(ID_2)
    assert ID_2 == employee_res_2.id_
    assert name2 == employee_res_2.first_name


def test_remove_user():
    test_add_user()

    employee = USER_SERVICE.remove_user(ID_1)
    assert ID_1 == employee.id_
    assert NAME_1 == employee.first_name

    user = USER_SERVICE.get_user(ID_1)
    assert user is None
