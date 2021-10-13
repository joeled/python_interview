from abc import ABC, abstractmethod


class AbstractTransition(ABC):

    @abstractmethod
    def add_transition_listener(self, listener: "TransitionListener") -> None:
        pass
