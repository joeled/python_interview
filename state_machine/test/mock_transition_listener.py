
class MockListener:

    request_list = []

    def on_transition(self, event: str) -> None:
        self.request_list.append(event)

