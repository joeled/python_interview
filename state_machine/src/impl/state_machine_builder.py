from src.api.abstract_state import AbstractState
from src.api.abstract_state_machine import AbstractStateMachine
from src.api.abstract_transition import AbstractTransition


class StateMachineBuilder:

    @staticmethod
    def create_factory() -> "StateMachineBuilder":
        return StateMachineBuilder()

    def create_state(self, name: str) -> AbstractState:
        raise Exception("you need to implement")

    def create_transition(self, start_state: AbstractState, end_state: AbstractState, event: str) -> AbstractTransition:
        raise Exception("you need to implement")

    def set_initial_state(self, initial_state: AbstractState) -> None:
        raise Exception("you need to implement")

    def build(self) -> AbstractStateMachine:
        raise Exception("you need to implement")
