from state_machine.state_machine import StateMachineBuilder

BUILDER = StateMachineBuilder.create_factory()


def test_phone():

    incoming_call = "incomingCall"
    answer_call = "answerCall"
    hang_up = "hangUp"

    idle = BUILDER.create_state("IDLE")
    ringing = BUILDER.create_state("RINGING")
    on_call = BUILDER.create_state("ON-CALL")

    BUILDER.create_transition(idle, ringing, incoming_call)
    BUILDER.create_transition(ringing, on_call, answer_call)
    BUILDER.create_transition(on_call, idle, hang_up)

    BUILDER.set_initial_state(idle)
    state_machine = BUILDER.build()

    assert idle == state_machine.get_current_state()

    state_machine.fire_event(incoming_call)
    assert ringing == state_machine.get_current_state()

    state_machine.fire_event(answer_call)
    assert on_call == state_machine.get_current_state()

    state_machine.fire_event(hang_up)
    assert idle == state_machine.get_current_state()
    