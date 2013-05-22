import unittest
import time
from state_machine import State, StateMachine
from news_test.Testing.ProductLibrary.Android.MetaAction.System import launch_app, quit_app, open_wifi, close_wifi,\
    wait_message_exist,wait_message_not_exist
from news_test.Testing.ProductLibrary.Android.MetaAction.Account import open_news_client, close_news_client
from news_test.Testing.ProductLibrary.Server.PostMessage import post_broadcast


class Test(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine()
        self.wifi_open = True
        self.news_open = True
        self.message = 'qajjc' + str(time.time())
        launch_app()

    def tearDown(self):
        print "==================="
        print time.strftime("%Y-%m-%d %X", time.localtime())
        print self.sm.state_records
        open_wifi()
        quit_app()


    def state_open_wifi(self):
        self.wifi_open = True
        print "[state] open_wifi"
        open_wifi()
        self.post_message()


    def state_close_wifi(self):
        self.wifi_open = False
        print "[state] close_wifi"
        close_wifi()
        self.post_message()


    def state_open_news_clint(self):
        self.news_open = True
        print "[state] open_news_clint"
        open_news_client()
        self.post_message()

    def state_close_news_clint(self):
        self.news_open = False
        print "[state] close_news_clint"
        close_news_client()
        self.post_message()

    def post_message(self):
        time.sleep(2)
        post_broadcast('title', self.message, 'summary', 'test.news.163.com', 'android')


    def check(self):
        if self.news_open and self.wifi_open :
            wait_message_exist(self.message)
        else:
            pass



    def test(self):
        state_open_wifi = State("state_open_wifi")
        state_close_wifi = State("state_close_wifi")
        state_open_news_client = State("state_open_news_client")
        state_close_news_client = State("state_close_news_client")

        state_open_wifi.register_execution_callback(self.state_open_wifi)
        state_open_wifi.register_verification_callback(self.check)
        state_close_wifi.register_execution_callback(self.state_close_wifi)
        state_close_wifi.register_verification_callback(self.check)
        state_open_news_client.register_execution_callback(self.state_open_news_clint)
        state_open_news_client.register_verification_callback(self.check)
        state_close_news_client.register_execution_callback(self.state_close_news_clint)
        state_close_news_client.register_verification_callback(self.check)

        state_open_wifi.next_states = [state_close_wifi, state_close_news_client, state_close_news_client]
        state_close_wifi.next_states = [state_open_news_client, state_close_news_client, state_open_wifi]
        state_open_news_client.next_states = [state_close_wifi, state_open_news_client, state_close_news_client, ]
        state_close_news_client.next_states = [state_open_wifi, state_close_wifi, state_open_news_client, ]

        self.sm.execution_times = 20
        self.sm.register_start_state(state_open_wifi)
        self.sm.run()


if __name__ == "__main__":
    unittest.main()
#

