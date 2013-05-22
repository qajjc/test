#coding=utf-8
import unittest,random
from upload_test.Testing.ProductLibrary.Android.MetaAction.System import launch_app, quit_app,wait_message_exist,open_notifications
from upload_test.Testing.ProductLibrary.Android.MetaAction.Account import click_http,click_https,select_file,wait_state_code
import time


class test(unittest.TestCase):
    def setUp(self):
        launch_app()

    def tearDown(self):
        quit_app()

    def test_http_upload(self):
        """
        使用http方式正常上传
        """
        file_name='file'+str(random.choice(xrange(5)))
        print file_name
        click_http()
        select_file(file_name)
        assert wait_state_code("upload is over result code:",200)
        assert wait_state_code("upload is over result code:200",5)





    def test_https_upload(self):
        '''
        使用https方式正常上传
        '''
        file_name='file'+str(random.choice(xrange(5)))
        click_https()
        select_file(file_name)
        time.sleep(1)
        assert wait_state_code("upload is over result code:",200)
        assert wait_state_code("upload is over result code:200",3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner(verbosity=2).run(suite)