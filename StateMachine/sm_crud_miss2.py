#coding=utf-8
__author__ = 'thinkpad'
import unittest
import logging
import logging.config
from ystore.BrowserOperation import Browser
from StateMachine.copy_file import copy_log_to_logfile
from StateMachine.crud_shoppingcart import ShoppingCartCRUDModel
from state_machine import State, StateMachine
from ystore.CartOperation2 import Cart
global Browser




logger = logging.getLogger('crud')

class MissCartTest(unittest.TestCase):
    def setUp(self):

        self.sccm = ShoppingCartCRUDModel()
        self.sccm.register_cart(Cart())
        self.sm = StateMachine()

    def tearDown(self):
        logger.info(self.sm.state_records)
        copy_log_to_logfile()
        bo=Browser
        bo.browser.close()
        # self.crud.close_cart_browser()

    def state_create(self):
        self.sccm.create_operation()

    def state_read(self):
        self.sccm.read_operation()

    def state_update(self):
        self.sccm.update_operation()

    def state_delete(self):
        self.sccm.delete_operation()

    def test_crud(self):
        state_create = State('state_create')
        state_read = State('state_read')
        state_update = State('state_update')
        state_delete = State('state_delete')

        state_create.register_execution_callback(self.state_create)
        state_read.register_execution_callback(self.state_read)
        state_update.register_execution_callback(self.state_update)
        state_delete.register_execution_callback(self.state_delete)

        for state in [state_create, state_read, state_update, state_delete]:
            state.next_states = (state_create, state_delete, state_update, state_read)

        self.sm.execution_times = 20
        self.sm.register_start_state(state_create)
        self.sm.register_important_state(state_delete)
        self.sm.run()


if __name__ == "__main__":
    unittest.main()
