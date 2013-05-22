import random

class State():
    def __init__(self,name):
        self.name=name
        self.execution_callback=None
        self.execution_callback_paras=None
        self.verification_callback=None
        self.verification_callback_paras=None
        self.next_states=None
        
    def register_execution_callback(self,execution_callback,*para):
        self.execution_callback=execution_callback
        self.execution_callback_paras=para
        
    def register_verification_callback(self,verification_callback,*para):
        self.verification_callback=verification_callback
        self.verification_callback_paras=para
        
    def register_next_states(self,*next_states):
        self.next_states=next_states
        
    def run(self):
        self.execution_callback(*self.execution_callback_paras)
        if self.verification_callback != None:
            self.verification_callback(*self.verification_callback_paras)

class StateMachine():
    def __init__(self):
        self.state_records=[]
        self.current_state=None
        self.last_state=None
        self.execution_times=10
        self.without_impor_exce_times = 5
        self.expect_impot_state_exec_imm = False
        self.assist_operation = None
        self.assit_circle_times = 0
    
    def register_start_state(self,state):
        self.current_state=state
        
    def register_end_state(self, state):
        self.end_state = state
    
    def register_important_state(self,state):
        self.important_state = state
    
    def register_assist_operation(self, operation):
        self.assist_operation = operation
        
    def run(self):
        times=0
        while True:
            if times==self.execution_times:
                break
            self.state_records.append(self.current_state.name)
            self.current_state.run()
            self.assit_circle_times += 1
            if self.assit_circle_times%6 == 0:
                self.assist_operation()
            if len(self.state_records)%self.without_impor_exce_times==0:
                print self.state_records[-5:]
                if self.important_state in self.state_records[-5:]:
                    self.expect_impot_state_exec_imm = False
                else:
                    self.expect_impot_state_exec_imm = True
                    
            self.__generate_next_state()
            times+=1
            
    def __generate_next_state(self):
        next_states=self.current_state.next_states
        
          
        if self.expect_impot_state_exec_imm:
            if self.important_state in next_states:
                next_state = self.important_state
                self.expect_impot_state_exec_imm = False
            else:
                next_state_index=random.randint(0,len(next_states)-1)
                next_state=next_states[next_state_index]
                    
        else:
            next_state_index=random.randint(0,len(next_states)-1)
            next_state=next_states[next_state_index]
                        
        if next_state==self.current_state:
            self.__generate_next_state()
        else:
            self.current_state=next_state
    
if __name__=="__main__":
    pass
    