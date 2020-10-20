
from user_service.test.test_b_user_service import USER_SERVICE


def test_basic():
    id_1 = 4
    name_1 = "spam"

    employee = USER_SERVICE.create_user(id_1, name_1, "ham")

    employee.id_ = 5
    employee.first_name = "xxx"

    employee2 = USER_SERVICE.get_user(id_1)
    assert id_1 == employee2.id_
    assert name_1 == employee2.first_name
