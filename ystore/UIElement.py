#coding=utf-8


ui_element = {}

home_page = {
    'link_login': {'id_': 'ys-login'},
    'btn_shopping_cart': {'id_': 'mc-menu-hd'}
}

login_page = {
    'txt_username': {'name': 'username'},
    'txt_password': {'name': 'password'},
    'btn_login': {'xpath': "//a[@class='w-btn1 w-btn1-2 btn commit']"}


}



cart_page = {
    #需要传一个值给他，确定第几个元素
    'list_product': {'xpath': "//div[@id='cart-items']/div"},
    'product_delete': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[8]/a" },
    'btn_confirm': {'xpath': "//div[@class='zcnt']/div/div[2]/div[2]/a[1]" },
    'product_price': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[4]" },
    'product_discount': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[6]/select" },
    'product_add': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[5]/div/span[2]" },
    'product_reduce': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[5]/div/span[1]" },
    'product_amount': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[5]/div/input" },
    'product_name': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[3]/div/a" },
    'product_category': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[3]/div[2]" },
    'product_total_price': {'xpath': "//div[@id='cart-items']/div[*]/table/tbody/tr/td[7]/span"},
}
ui_element.update(home_page)
ui_element.update(login_page)
ui_element.update(cart_page)


def get_selectors(element_key,i=None):
    selector = ""
    if ui_element.has_key(element_key):
        for prop, value in ui_element[element_key].items():
            if prop == "child": continue
            if type(value) == str or type(value) == unicode:
                selector += '%s="%s",' % (prop, value)
            else:
                selector += '%s=%s,' % (prop, value)
        selector = selector[:-1] # remove the last comma
    else:
        pass
    if i :
        string=selector.split("*")
        selector=string[0]+str(i)+string[1]
        return selector
    else:
        return selector


if __name__ == '__main__':
    print get_selectors('product_delete',2)