
from user_service.test.test_b_user_service import add_user, USER_SERVICE, ID_1, NAME_1, MOCK_USER_LISTENER


def test_remove():
    MOCK_USER_LISTENER.users_created = []
    MOCK_USER_LISTENER.users_removed = []

    add_user()

    employee = USER_SERVICE.remove_user(ID_1)
    assert ID_1 == employee.id_
    assert NAME_1 == employee.first_name

    assert len(MOCK_USER_LISTENER.users_removed) == 1
    removed_employee = MOCK_USER_LISTENER.users_removed[0]
    assert ID_1 == removed_employee.id_
    assert NAME_1 == removed_employee.first_name
