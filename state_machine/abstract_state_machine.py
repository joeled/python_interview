from abc import ABC, abstractmethod

__all__ = ["State", "StateMachine", "Transition", "TransitionListener"]


class State:

    name: str


class StateMachine(ABC):

    @abstractmethod
    def get_current_state(self) -> State:
        pass

    @abstractmethod
    def fire_event(self, on_event: str) -> None:
        pass


class Transition(ABC):

    @abstractmethod
    def add_transition_listener(self, listener: "TransitionListener") -> None:
        pass


class TransitionListener(ABC):

    @abstractmethod
    def on_transition(self, event: str) -> None:
        pass

