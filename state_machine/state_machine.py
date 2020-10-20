from state_machine.abstract_state_machine import State, StateMachine


class StateMachineBuilder:

    @staticmethod
    def create_factory() -> "StateMachineBuilder":
        return StateMachineBuilder()

    def create_state(self, name: str) -> State:
        pass

    def create_transition(self, start_state: State, end_state: State, event: str) -> "Transition":
        pass

    def set_initial_state(self, initial_state: State) -> None:
        pass

    def build(self) -> StateMachine:
        pass
