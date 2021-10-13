from abc import ABC, abstractmethod

from src.api.abstract_state import AbstractState


class AbstractStateMachine(ABC):

    @abstractmethod
    def get_current_state(self) -> AbstractState:
        pass

    @abstractmethod
    def fire_event(self, on_event: str) -> None:
        pass

