from src.api.abstract_state import AbstractState
from src.api.abstract_state_machine import AbstractStateMachine
from src.api.abstract_transition import AbstractTransition


class StateMachineBuilder:

    @staticmethod
    def create_factory() -> "StateMachineBuilder":
        return StateMachineBuilder()

    def create_state(self, name: str) -> AbstractState:
        pass

    def create_transition(self, start_state: AbstractState, end_state: AbstractState, event: str) -> AbstractTransition:
        pass

    def set_initial_state(self, initial_state: AbstractState) -> None:
        pass

    def build(self) -> AbstractStateMachine:
        pass
