from news_test.CommonLibrary.Android.Automation import click,input_content
from news_test.Testing.ProductLibrary.Android.Data.UIElement import get_selectors
def input_username(username):
    input_content(username,get_selectors('txt_username'))

def input_password(password):
    input_content(password,get_selectors('txt_password'))

def click_login_btn():
    click(get_selectors('btn_login'))


def open_news_client():
    click(get_selectors('btn_open'))

def close_news_client():
    click(get_selectors('btn_close'))