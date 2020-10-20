from state_machine.state_machine import StateMachineBuilder
from state_machine.test.mock_transition_listener import MockListener

BUILDER = StateMachineBuilder.create_factory()


def test_on_off():
    on_event = "flipOn"
    off_event = "flipOff"

    on = BUILDER.create_state("on")
    off = BUILDER.create_state("off")

    transition1 = BUILDER.create_transition(on, off, off_event)
    transition2 = BUILDER.create_transition(off, on, on_event)

    # setup listener
    mock = MockListener()
    transition1.add_transition_listener(mock)

    # initialize
    BUILDER.set_initial_state(on)
    state_machine = BUILDER.build()

    # initial state
    assert on == state_machine.get_current_state()
    state_machine.fire_event(on_event)  # Should do nothing because we are already on

    # first event
    assert on == state_machine.get_current_state()
    state_machine.fire_event(off_event);

    # second event
    assert off == state_machine.get_current_state()
    assert 1 == len(mock.request_list)
    assert off_event == mock.request_list[0]
