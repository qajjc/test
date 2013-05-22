#coding=utf-8
__author__ = 'thinkpad'
import unittest
from StateMachine.c_r_u_d_miss import CRUD_MISS
from state_machine import State,StateMachine

class CRUD (unittest.TestCase):
    def setUp(self):
        self.crud=CRUD_MISS()
        self.sm = StateMachine()

    def tearDown(self):
        print self.sm.state_records
        # self.crud.close_cart_browser()

    def state_create(self):
        self.crud.create_operation()

    def state_read(self):
        self.crud.read_operation()

    def state_update(self):
        self.crud.update_operation()

    def state_delete(self):
        self.crud.delete_operation()

    def test_crud(self):
        state_create=State('state_create')
        state_read=State('state_read')
        state_update=State('state_update')
        state_delete=State('state_delete')

        state_create.register_execution_callback(self.state_create)
        state_read.register_execution_callback(self.state_read)
        state_update.register_execution_callback(self.state_update)
        state_delete.register_execution_callback(self.state_delete)

        for state in [state_create,state_read,state_update,state_delete]:
            state.next_states=(state_create,state_delete,state_update,state_read)
            state.register_verification_callback(self.crud.check_operation)

        self.sm.execution_times = 30
        self.sm.register_start_state(state_create)
        self.sm.run()


if __name__ == "__main__":
    unittest.main()