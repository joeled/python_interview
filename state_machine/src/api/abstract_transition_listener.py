from abc import ABC, abstractmethod


class AbstractTransitionListener(ABC):

    @abstractmethod
    def on_transition(self, event: str) -> None:
        pass
