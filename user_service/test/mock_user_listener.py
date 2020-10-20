from typing import List

from user_service.src import UserListener, User


class MockUserListener(UserListener):

    users_created: List[User] = []
    users_removed: List[User] = []

    def user_created(self, user: User) -> None:
        self.users_created.append(user)

    def user_removed(self, user: User) -> None:
        self.users_removed.append(user)
