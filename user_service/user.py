from abc import ABC, abstractmethod
from typing import Mapping, Any

from user_service.abstract_user import User, UserListener, UserService


class UserServiceFactory(ABC):

    @staticmethod
    def create_factory(config: Mapping[str, Any]) -> "UserServiceFactory":
        factory: "UserServiceFactory" = MyUserServiceFactory()
        factory.configure(config)
        return factory

    @abstractmethod
    def configure(self, config: Mapping) -> None:
        pass

    @abstractmethod
    def create_service(self) -> UserService:
        pass


class MyUserServiceFactory(UserServiceFactory):

    def configure(self, config: Mapping) -> None:
        pass

    def create_service(self) -> UserService:
        return


class MyUserService(UserService):
    pass
