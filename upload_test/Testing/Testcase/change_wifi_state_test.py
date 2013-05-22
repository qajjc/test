#coding=utf-8
import unittest,random
from upload_test.Testing.ProductLibrary.Android.MetaAction.System import launch_app, quit_app,wait_message_exist,open_notifications
from upload_test.Testing.ProductLibrary.Android.MetaAction.Account import click_http,click_https,select_file,wait_state_code
from upload_test.CommonLibrary.Android.AdbCmd import adb_disable_wifi,adb_enable_wifi
import time


class test_wifi(unittest.TestCase):
    def setUp(self):
        launch_app()


    def tearDown(self):
        quit_app()

    def test_change_wifi_state(self):
        """
        切换wifi开关，测试上传
        """
        adb_disable_wifi() #关闭wifi
        file_name='file'+str(random.choice(xrange(5)))
        print file_name
        click_http()
        select_file(file_name)
        assert wait_state_code("upload is over result code:",300)#等待超时200s
        assert wait_state_code("upload is over result code:799",5)#验证返回的code，799表示网络问题

        adb_enable_wifi()#打开wifi
        click_http()
        select_file(file_name)
        #等待的分开写是因为如果你想等待上传成功返回200，但是因为网络或其他问题已经返回了799或是其他错误，如果写在一起的话需要300s等待完了，才知道出错了。
        #分开写的话如果有返回了就继续验证一下返回的是什么，不用一直在那边等
        assert wait_state_code("upload is over result code:",300)#等待超时300s
        assert wait_state_code("upload is over result code:200",5)#验证返回的code，200表示上传成功



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_wifi)
    unittest.TextTestRunner(verbosity=2).run(suite)
