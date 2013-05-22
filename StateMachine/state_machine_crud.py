#coding=utf-8

class State(object):
    def __init__(self, name):
        self.name = name
        self.execution_callback = None
        self.execution_callback_paras = None
        self.verification_callback = None
        self.verification_callback.paras = None
        self.nextState = None

    def register_execution_callback(self, execution_callback, *para):
        self.execution_callback = execution_callback
        self.execution_callback_paras = para

    def register_verification_callback(self, verification_callback, *para):
        self.verification_callback = verification_callback
        self.verification_callback_paras = para

    def register_next_states(self, *next_states):
        self.next_states = next_states

    def run(self):
        self.execution_callback(*self.execution_callback_paras)
        if self.verification_callback != None:
            self.verification_callback(*self.verification_callback_paras)


class StateMachine(object):
    def __init__(self):
        self.state_records = []
        self.current_state = None
        self.last_state = None
