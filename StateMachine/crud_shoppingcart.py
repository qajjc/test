#coding=utf-8
import random
import logging
import logging.config


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('crud')


class ShoppingCartCRUDModel(object):
    def __init__(self):
        self.get_the_length_of_list_callback = None
        self.get_the_amount_of_product_callback = None
        self.get_the_amount_of_product_callback_para = None
        self.create_product_not_exist_in_shopping_cart_callback = None
        self.create_product_exist_in_shopping_cart_callback = None
        self.create_product_not_exist_in_database_callback = None
        self.read_product_callback = None
        self.update_product_add_amount_callback = None
        self.update_product_add_amount_callback_para = None
        self.update_product_reduce_amount_callback = None
        self.update_product_reduce_amount_callback_para = None
        self.delete_product_exist_in_shopping_cart_callback = None
        self.delete_product_exist_in_shopping_cart_callback_para = None
        self.delete_product_not_exist_in_shopping_cart_callback = None
        self.delete_product_not_exist_in_shopping_cart_callback_para = None


    def register_cart(self, cart):
        self.cart = cart
        self.register_get_the_length_of_list_callback(self.cart.count_products)
        self.register_get_the_amount_of_product_callback(self.cart.get_product_amount)
        self.register_create_product_not_exist_in_database_callback(self.cart.add_product_to_cart)
        self.register_update_product_add_amount_callback(self.cart.add_amount)
        self.register_update_product_reduce_amount_callback(self.cart.reduce_amount)
        self.register_delete_product_exist_in_shopping_cart_callback(self.cart.delete_product)
        # self.get_the_length_of_list_callback = self.cart.count_products
        # self.get_the_amount_of_product_callback = self.cart.get_product_amount
        # self.create_product_not_exist_in_shopping_cart_callback = self.cart.add_product_to_cart
        # self.update_product_add_amount_callback = self.cart.add_amount
        # self.update_product_reduce_amount_callback = self.cart.reduce_amount
        # self.delete_product_exist_in_shopping_cart_callback = self.cart.delete_product


    def register_get_the_length_of_list_callback(self, get_the_length_of_list_callback):
        self.get_the_length_of_list_callback = get_the_length_of_list_callback

    def register_get_the_amount_of_product_callback(self, get_the_amount_of_product_callback, ):
        self.get_the_amount_of_product_callback = get_the_amount_of_product_callback


    def register_create_product_not_exist_in_shopping_cart_callback(self,
                                                                    create_product_not_exist_in_shopping_cart_callback):
        self.create_product_not_exist_in_shopping_cart_callback = create_product_not_exist_in_shopping_cart_callback

    def register_create_product_exist_in_shopping_cart_callback(self, create_product_exist_in_shopping_cart_callback):
        self.create_product_exist_in_shopping_cart_callback = create_product_exist_in_shopping_cart_callback

    def register_create_product_not_exist_in_database_callback(self, create_product_not_exist_in_database_callback):
        self.create_product_not_exist_in_database_callback = create_product_not_exist_in_database_callback

    def register_read_product_callback(self, read_product_callback):
        self.read_product_callback = read_product_callback

    def register_update_product_add_amount_callback(self, update_product_add_amount_callback):
        self.update_product_add_amount_callback = update_product_add_amount_callback


    def register_update_product_reduce_amount_callback(self, update_product_reduce_amount_callback):
        self.update_product_reduce_amount_callback = update_product_reduce_amount_callback


    def register_delete_product_exist_in_shopping_cart_callback(self, delete_product_exist_in_shopping_cart_callback):
        self.delete_product_exist_in_shopping_cart_callback = delete_product_exist_in_shopping_cart_callback


    def register_delete_product_not_exist_in_shopping_cart_callback(self,
                                                                    delete_product_not_exist_in_shopping_cart_callback):
        self.delete_product_not_exist_in_shopping_cart_callback = delete_product_not_exist_in_shopping_cart_callback


    def get_the_amount_of_product_callback_run(self):
        index = self.select_which_object_to_operate()
        if index != 0:
            self.get_the_amount_of_product_callback_para = index
            return self.get_the_amount_of_product_callback(self.get_the_amount_of_product_callback_para)
        else:
            self.get_the_amount_of_product_callback_para = 0
            return 0

    def update_product_add_amount_callback_run(self):
        self.get_the_amount_of_product_callback_run()
        self.update_product_add_amount_callback_para = self.get_the_amount_of_product_callback_para
        # print '增加产品数量传参数%d' % self.update_product_add_amount_callback_para
        self.update_product_add_amount_callback(self.update_product_add_amount_callback_para)

    def update_product_reduce_amount_callback_run(self):
        self.get_the_amount_of_product_callback_run()
        self.update_product_reduce_amount_callback_para = self.get_the_amount_of_product_callback_para
        # print '减少产品数量传参数%d' % self.update_product_reduce_amount_callback_para
        self.update_product_reduce_amount_callback(self.update_product_reduce_amount_callback_para)

    def delete_product_exist_in_shopping_cart_callback_run(self):
        self.delete_product_exist_in_shopping_cart_callback_para = self.select_which_object_to_operate()
        # print 'delete传参数%d' % self.delete_product_exist_in_shopping_cart_callback_para
        self.delete_product_exist_in_shopping_cart_callback(self.delete_product_exist_in_shopping_cart_callback_para)

    def repeat_times(self):
        i = random.randint(1, 3)
        logger.info("以下这个动作会重复%d次" % i)
        return i

    def select_which_object_to_operate(self):
        length = self.get_the_length_of_list_callback()
        i = random.choice([1, 2, 3])
        if i == 1 and length > 0:
            logger.info('本次将操作第一个产品')
            return 1 #选择操作第一个产品

        elif i == 2 and length > 0:
            num = random.randint(1, length)
            logger.info('本次将操作的序号是%d' % num)
            return num #随机选择操作几个产品

        elif i == 3 and length > 0:
            logger.info('本次将对最后一个产品进行操作')
            return length #选择操作最后一个产品
        else:
            #如果购物车列表为空的话，直接返回0
            logger.info('购物车中无产品')
            return 0

    def create_operation(self):
        logger.info('=' * 5 + '创建操作' + '=' * 5)
        i = self.repeat_times()
        while i:
            self.create_product_not_exist_in_database_callback()
            i -= 1

    def read_operation(self):
        logger.info('=' * 5 + '读取操作' + '=' * 5)
        logger.info('目前购物车中有%d个产品' % self.get_the_length_of_list_callback())

    def update_add_operation(self):
        '''
        先去数据库取一次购物车产品的列表，如果不为空，那么执行一次
        '''
        length = self.get_the_length_of_list_callback()
        if length != 0:
            try:
                self.update_product_add_amount_callback_run()
                logger.info('增加产品成功')
            except:
                logger.error('增加产品时发生异常')
                raise Exception('增加产品时发生异常')

        else:
            logger.info('购物车列表为空，无法进行增加操作')

    def update_reduce_operation(self):
        length = self.get_the_length_of_list_callback()
        before_reduce = self.get_the_amount_of_product_callback_run()
        if length != 0:
            if before_reduce > 1:
                try:
                    self.update_product_reduce_amount_callback_run()
                    logger.info('减少产品成功')
                except:
                    logger.error('减少产品时出现异常，请检查')
                    raise Exception('减少产品时出现异常，请检查')


            elif before_reduce <= 1:
                logger.info('产品数量为1，无法再减少了')
        else:
            logger.info('购物车列表为空，无法进行减少操作')


    def update_operation(self):
        logger.info( '=' * 5 + '更新操作' + '=' * 5)
        times = self.repeat_times()
        i = random.choice([1, 2])
        if i == 1:
            while times:
                self.update_add_operation()
                times -= 1
        else:
            while times:
                self.update_reduce_operation()
                times -= 1

    def delete_operation(self):
        logger.info('=' * 5 + '删除操作' + '=' * 5)
        length = self.get_the_length_of_list_callback()
        if length != 0:
            times = self.repeat_times()
            while times:
                before_delete = self.get_the_length_of_list_callback()
                self.delete_product_exist_in_shopping_cart_callback_run()
                after_delete = self.get_the_length_of_list_callback()
                if before_delete - after_delete == 1:
                    logger.info('删除产品成功')
                times -= 1
        else:
            logger.info('需要删除的产品已被删除，无法进行减少操作')
