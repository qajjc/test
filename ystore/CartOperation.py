#coding=utf-8
import random
from add_product import add_product_by_http_request
from ystore.BrowserOperation import Browser
from ystore.UIElement import get_selectors
from ystore.Product import products
from ystore.DDBOperation import count_sku_products
global Browser
import time

class Cart():
    def __init__(self):
        self.bo = Browser
        self.bo.click(get_selectors('link_login'))
        self.bo.input(get_selectors('txt_username'), 'qajjc01')
        self.bo.input(get_selectors('txt_password'), 'qa1234')
        time.sleep(1)#由于自动输入用户名密码的速度太快了，导致登录按钮还处于不可点击的状态，所以这边等待1s
        self.bo.click(get_selectors('btn_login'))
        self.bo.click(get_selectors('btn_shopping_cart'))

    def select_product(self):
        i = random.choice([1, 2, 3])
        if i == 1:
            return 1 #选择操作第一个产品
        elif i == 2:
            num = random.choice(list(xrange(self.count_products())))
            return num #随机选择操作一个产品
        elif i == 3:
            return self.count_products()#选择操作最后一个产品


    def count_products(self):
        total_amount = self.bo.count_elements(get_selectors('list_product'))
        return total_amount

    def add_product_to_cart(self):
        #用http接口增加一个产品
        add_product_by_http_request()
        #增加后重新加载购物车页面
        self.bo.browser.refresh()

    def add_amount(self,index):
        #增加购物车产品的数量，实际操作为点一下购物车中的“+”
        self.bo.browser.refresh()
        try:
            self.bo.wait_element_exist(get_selectors('product_add',index))
            self.bo.click(get_selectors('product_add',index))
            time.sleep(1)
        except :
            raise '增加按钮未出现'


    def reduce_amount(self,index):
        #减少购物车产品的数量，实际操作为点一下购物车中的“-”
        self.bo.browser.refresh()
        try:
            self.bo.wait_element_exist(get_selectors('product_reduce',index))
            self.bo.click(get_selectors('product_reduce',index))
            time.sleep(1)
        except :
            raise '减少按钮未出现'


    def delete_product(self,index):

        self.bo.browser.refresh()
        try:
            self.bo.wait_element_exist(get_selectors('product_delete',index))
            self.bo.click(get_selectors('product_delete', index))
            self.bo.click(get_selectors('btn_confirm'))
            time.sleep(1)
        except :
            raise '删除按钮未出现'

    def get_product_name(self,index):
        name = self.bo.get_text(get_selectors('product_name', index))
        return name


    def get_product_category(self,index):
        category = self.bo.get_text(get_selectors('product_category', index))
        return category

    def get_product_skuid(self,index):
        '''
        获取购物车中产品对应的skuid
        '''
        category = self.bo.get_text(get_selectors('product_category',index))
        skuid = 0
        for keys in products.keys():
            if category == keys.decode('utf-8'):
                skuid = products[keys]['skuid']
        return skuid

    def get_product_amount(self,skuid):
        amount=0
        for items in count_sku_products().keys():
            if items==skuid:
                amount=count_sku_products()[items]
        return int(amount)

    def close_browser(self):
        self.bo.browser.close()


if __name__ == '__main__':
    cart = Cart()
    print cart.get_product_name(1)
    print cart.get_product_category(1)