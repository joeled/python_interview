from abc import ABC, abstractmethod
from dataclasses import dataclass

__all__ = ["User", "UserListener", "UserService"]


@dataclass(frozen=True)
class User:
    id_: int
    first_name: str
    last_name: str


class UserListener(ABC):

    @abstractmethod
    def user_created(self, user: User) -> None:
        pass

    @abstractmethod
    def user_removed(self, user: User) -> None:
        pass


class UserService(ABC):

    @abstractmethod
    def create_user(self, id_: int, first_name: str, last_name: str) -> User:
        pass

    @abstractmethod
    def remove_user(self, id_: int) -> User:
        pass

    @abstractmethod
    def get_user(self, id_: int) -> User:
        pass

    @abstractmethod
    def add_user_listener(self, listener: UserListener) -> None:
        pass

