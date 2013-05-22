from upload_test.CommonLibrary.Android.Automation import android_launch_app, android_quit_app, open_notifications, click, click_back, wait_element_exist, \
    android_open_wifi, android_close_wifi
from upload_test.Testing.ProductLibrary.Android.Data.BusinessData import business_data
from upload_test.Testing.ProductLibrary.Android.Data.UIElement import get_selectors


def launch_app():
    android_launch_app(business_data['app_path'])


def quit_app():
    android_quit_app()


def open_wifi():
    android_open_wifi()


def close_wifi():
    android_close_wifi()


def clear_notification():
    open_notifications()
    click(get_selectors('btn_clear_notification'))
    # click_back()



def wait_message_exist(message):
    open_notifications()
    selector = 'new UiSelector().textContains("%s")' % message
    exist = wait_element_exist(selector, timeout=10)
    print exist, selector
    if not exist:
        click_back()
        raise RuntimeError("the message %s don't occur, timeout" % message)
    else:
        clear_notification()


def wait_message_not_exist(message):
    open_notifications()
    selector = 'new UiSelector().textContains("%s")' % message
    exist = wait_element_exist(selector, timeout=10)
    print exist, selector
    if exist:
        # click_back()
        raise RuntimeError("the message %s occur" % message)
    else:
        clear_notification()
