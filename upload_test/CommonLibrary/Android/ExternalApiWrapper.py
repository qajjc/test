#coding=utf-8
import time
from appium import webdriver


class ExternalApiWrapper(object):
    def _set_selector(self, selector):
        if selector.startswith('id_'):
            exec ('self.element=self.device.find_element_by_id(%s)' % selector)
        elif selector.startswith("name"):
            exec ("self.element = self.device.find_element_by_name(%s)" % selector)
        elif selector.startswith('new'):
            exec ("self.element = self.device.find_element_by_android_uiautomator('%s')" % selector)


    def launch_sut_app(self, app_path):

        self.device = webdriver.Remote(command_executor='http://localhost:4723/wd/hub',
                                       desired_capabilities={
                                           'platformName': 'Android',
                                           'deviceName': 'Android Emulator',
                                           'platformVersion': '4.2',
                                           'app': app_path
                                       })

    def quit_sut_app(self):
        self.device.quit()

    def click(self, selector):
        self._set_selector(selector)
        self.element.click()

    def input_content(self, content, selector):
        self._set_selector(selector)
        self.element.send_keys(content)

    def open_notifications(self):
        self.device.open_notifications()



    def click_key(self,key):

        if key =='back':

            self.device.press_keycode(4)
        elif key =='home':
            #http://developer.android.com/reference/android/view/KeyEvent.html,需要去这个页面找key对应的值
            self.device.press_keycode('3')


    def wait_element_exist(self, timeout, selector):
        for second in range(0, timeout):
            try:
                self._set_selector(selector)
                print "the element %s exist" % selector
                return True
            except:
                time.sleep(1)
                continue
        print "the element %s not exist" % selector
        return False


external_api_wrapper = ExternalApiWrapper()

    
    
    
    