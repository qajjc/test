from upload_test.CommonLibrary.Android.ExternalApiWrapper import external_api_wrapper as api
from upload_test.CommonLibrary.Android.AdbCmd import adb_disable_wifi, adb_enable_wifi


def android_launch_app(app_path):
    api.launch_sut_app(app_path)


def android_quit_app():
    api.quit_sut_app()


def click(selector):
    api.click(selector)


def input_content(content, selector):
    api.input_content(content, selector)


def android_open_wifi():
    adb_enable_wifi()


def android_close_wifi():
    adb_disable_wifi()


def click_back():
    api.click_key('back')


def click_home():
    api.click_key('home')


def open_notifications():
    api.open_notifications()


def wait_element_exist(selector, timeout):
    return api.wait_element_exist(timeout, selector)




