from upload_test.CommonLibrary.Android.Automation import click,input_content,wait_element_exist
from upload_test.Testing.ProductLibrary.Android.Data.UIElement import get_selectors
import time
def click_http():
    click(get_selectors("http"))

def click_https():
    click(get_selectors("https"))

def select_file(file_name):
    # click(get_selectors("file_manager"))

    click(get_selectors(file_name))
    time.sleep(1)
    # click(get_selectors("Button_confirm"))

def wait_state_code(code,timeout):
    selector = 'new UiSelector().textContains("%s")' % code
    return wait_element_exist(selector,timeout)