#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import *
from ystore.UIElement import get_selectors

class BrowserOperation(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://miss.163.com/')

    def _set_selector(self, selector):

        if selector.startswith('id_'):
            exec ('self.element=self.browser.find_element_by_id(%s)' % selector)
        elif selector.startswith("name"):
            exec ("self.element = self.browser.find_element_by_name(%s)" % selector)
        elif selector.startswith('xpath'):
            exec ("self.element = self.browser.find_element_by_xpath(%s)" % selector)

    def click(self, selector):
        self._set_selector(selector)
        self.element.click()


    def input(self, selector, content):
        self._set_selector(selector)
        self.element.send_keys(content)

    def wait_element_exist(self,selector,timeout=30):
        for second in range(0, timeout):
            try:
                self._set_selector(selector)
                return True
            except:
                time.sleep(1)
                continue
        return False

    def count_elements(self,selector):
        '''
        计算包含该属性元素的个数
        '''
        time.sleep(2)
        exec ("self.element = self.browser.find_elements_by_xpath(%s)" % selector)
        element_list=self.element
        return len(element_list)

    def get_text(self,selector):
        '''
        获取该元素对应的文本内容
        '''
        self._set_selector(selector)
        text=self.element.text #注意这个后面不能加（）否则会报错
        return text

    def close_browser(self):
        self.browser.close()



global Browser
Browser = BrowserOperation()

if __name__ == '__main__':
    username = 'qajjc@163.com'
    password = 'qa1234'
    bo = Browser
    # bo.count_elements("//div[@id='cart-items']/div")
    print bo.get_text(get_selectors('link_login'))
    # bo.click(get_selectors('link_login'))
    # bo.input(get_selectors('txt_username'),username)
    # bo.input(get_selectors('txt_password'),password)





