#coding=utf-8
import random,time,logging,logging.config
from add_product import add_product_by_http_request
from ystore.BrowserOperation import Browser
from ystore.UIElement import get_selectors
from ystore.DDBOperation import count_sku_products
from Product import get_product_info


global Browser

logger=logging.getLogger('crud')

class Cart():
    def __init__(self):
        self.bo = Browser
        self.bo.click(get_selectors('link_login'))
        self.bo.input(get_selectors('txt_username'), 'qajjc01')
        self.bo.input(get_selectors('txt_password'), 'qa1234')
        time.sleep(1)#由于自动输入用户名密码的速度太快了，导致登录按钮还处于不可点击的状态，所以这边等待1s
        self.bo.click(get_selectors('btn_login'))
        self.bo.click(get_selectors('btn_shopping_cart'))




    def count_products(self):
        total_amount = self.bo.count_elements(get_selectors('list_product'))
        return total_amount

    def add_product_to_cart(self):
        #用http接口增加一个产品
        add_product_by_http_request()
        #增加后重新加载购物车页面
        self.bo.browser.refresh()

    def add_amount(self, index):
        if index > 0:
            self.bo.browser.refresh()
            try:
                self.bo.wait_element_exist(get_selectors('product_add', index))
                self.bo.click(get_selectors('product_add', index))
                logger.info('本次第%d个产品的数量增加1' % index)

                # time.sleep(1)
            except Exception:
                raise '增加按钮未出现'
                logger.error('增加按钮未出现')
        else:
            logger.info( 'index:%d'% index)
            logger.info( '购物车无产品，无法增加数量')


    def reduce_amount(self, index):
        if index > 0:
            self.bo.browser.refresh()
            try:
                self.bo.wait_element_exist(get_selectors('product_reduce', index))
                self.bo.click(get_selectors('product_reduce', index))

                # time.sleep(1)
            except Exception:
                logger.error('减少按钮未出现')
                raise '减少按钮未出现'

        else:
            logger.info( '购物车无产品，无法减少数量')


    def delete_product(self, index):
        if index > 0:
            self.bo.browser.refresh()
            skuid=self.get_product_skuid(index)
            logger.info('产品的skuid是%d'% skuid)
            try:
                self.bo.wait_element_exist(get_selectors('product_delete', index))
                self.bo.click(get_selectors('product_delete', index))
                self.bo.click(get_selectors('btn_confirm'))

                # time.sleep(1)
            except Exception:
                logger.error('删除按钮未出现')
                raise '删除按钮未出现'

        else:
            logger.info ('购物车无产品，无法进行删除')

    def get_product_name(self, index):
        name = self.bo.get_text(get_selectors('product_name', index))
        return name


    def get_product_category(self, index):
        category = self.bo.get_text(get_selectors('product_category', index))
        return category

    def get_product_skuid(self, index):
        '''
        获取购物车中产品对应的skuid
        '''
        category = self.bo.get_text(get_selectors('product_category', index))
        name = self.bo.get_text(get_selectors('product_name', index))
        products_info = get_product_info()
        skuid = 0
        length=len(products_info.keys())
        for i in range(0,length):
            if name == products_info[i]['name']:
                if products_info[i]['desc'] in category:
                    skuid = products_info[i]['skuid']
        return skuid

    def get_product_amount(self, index):
        skuid = self.get_product_skuid(index)
        logger.info('产品的skuid是%d'% skuid)
        amount = 0
        for items in count_sku_products().keys():
            if items == skuid:
                amount = count_sku_products()[items]
        return int(amount)

    def close_browser(self):
        self.bo.browser.close()


if __name__ == '__main__':
    cart = Cart()
    print cart.get_product_name(4)
    print cart.get_product_category(4)
    print cart.get_product_skuid(2)