#coding=utf-8
import unittest,time
from StateMachine.state_machine import StateMachine, State

#创建-读取-更新-删除-状态机模型
class C_r_u_d_model(unittest.TestCase):
    def setUp(self):
        self.i = 0  #作为计数器，当>=1的时候可以删除，读取，以及更新，其他时候只能创建
        self.sm = StateMachine()

    def tearDown(self):
        print "==================="
        print time.strftime("%Y-%m-%d %X", time.localtime())
        print self.sm.state_records

    def create_operation(self):
        print '创建一条记录'
        self.i += 1
        print'目前有%d条记录' % self.i


    def read_operation(self):
        if self.i > 0:
            print'读取一条记录'
        else:
            print'无记录，未执行读取操作'

    def update_operation(self):
        if self.i > 0:
            print'更新一条记录'
        else:
            print'无记录，未执行更新操作'

    def delete_operation(self):
        if self.i > 0:
            print '删除一条记录'
            self.i -= 1
            print '删除一条记录后还有%d条记录' % self.i

    def check_operation(self):
        print'check'


    def test_c_r_u_d_model(self):
        state_create = State('create_operation')
        state_read = State('read_operation')
        state_update = State('update_operation')
        state_delete = State('delete_operation')

        state_create.register_execution_callback(self.create_operation)
        state_read.register_execution_callback(self.read_operation)
        state_update.register_execution_callback(self.update_operation)
        state_delete.register_execution_callback(self.delete_operation)

        for state in [state_create, state_read, state_update, state_delete]:
            state.register_verification_callback(self.check_operation)
            state.next_states = (state_create, state_read, state_update, state_delete)


        self.sm.execution_times = 50
        self.sm.register_start_state(state_create)
        self.sm.run()


if __name__ == "__main__":
    unittest.main()
