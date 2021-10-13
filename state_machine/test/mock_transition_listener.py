from src.api.abstract_transition_listener import AbstractTransitionListener


class MockListener(AbstractTransitionListener):

    request_list = []

    def on_transition(self, event: str) -> None:
        self.request_list.append(event)

