#coding=utf-8
import random
from ystore.DDBOperation import count_sku_NO
from ystore.CartOperation import Cart

cart = Cart()


class CRUD_MISS(object):
    def __init__(self):
        pass

    def get_the_length_of_list(self):
        return int(count_sku_NO())

    def repeat_times(self):
        i = random.randint(1, 3)
        print "以下这个动作会重复%d次" % i
        return i

    def select_which_object_to_operate(self):
        length = self.get_the_length_of_list()
        i = random.choice([1, 2, 3])
        if i == 1 and length > 0:
            print'本次将操作第一个产品'
            return [1]#选择操作第一个产品

        elif i == 2 and length > 0:
            num = []
            k = random.randint(1, length)
            l = [random.choice(list(xrange(k))) for a in xrange(k)]
            for j in l:
                num.append(j + 1)
            print '本次将操作%d个产品，分别是' % k
            print num
            return num #随机选择操作几个产品

        elif i == 3 and length > 0:
            print'本次将对最后一个产品进行操作'
            return [self.get_the_length_of_list()]#选择操作最后一个产品
        else:
            #如果购物车列表为空的话，直接返回0
            return [0]

    def create_operation(self):
        print '=' * 5 + '创建操作' + '=' * 5
        i = self.repeat_times()
        while i:
            cart.add_product_to_cart()
            i -= 1


    def read_operation(self):
        print '=' * 5 + '读取操作' + '=' * 5

        length = self.get_the_length_of_list()
        print '目前购物车中有%d 个不同商品' % length


    def update_add_operation(self):
        if self.get_the_length_of_list() >= 1:
            for i in self.select_which_object_to_operate():
                skuid = cart.get_product_skuid(i)
                before_add = cart.get_product_amount(skuid)
                cart.add_amount(i)
                after_add = cart.get_product_amount(skuid)
                if after_add - before_add == 1:
                    print '增加产品数量成功'
                    print 'after add  the skuid %d have %d' % (skuid, after_add)
                else:
                    print '增加前的数量：%d'% before_add
                    print '增加后的数量：%d'% after_add
        else:
            print '购物车中无产品，无法增加单个产品数量'


    def update_reduce_operation(self):
        if self.get_the_length_of_list() > 1:
            for i in self.select_which_object_to_operate():
                skuid = cart.get_product_skuid(i)
                before_reduce = cart.get_product_amount(skuid)
                if before_reduce > 1:
                    cart.reduce_amount(i)
                    after_reduce = cart.get_product_amount(skuid)
                    if before_reduce - after_reduce == 1:
                        print '减少产品数量成功！'
                        print 'after reduce  the skuid %d have %d' % (skuid, after_reduce)
                    else:
                        print '减少前的数量：%d'% before_reduce
                        print '减少后的数量：%d'% after_reduce

                elif before_reduce <= 1:
                    print '产品数量为1，无法再减少了'
        else:
            print '购物车中无产品，无法减少单个产品数量'

    def update_operation(self):
        print '=' * 5 + '更新操作' + '=' * 5
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
        print '=' * 5 + '删除操作' + '=' * 5
        times = self.repeat_times()
        while times:
            for i in self.select_which_object_to_operate():
                before_delete = self.get_the_length_of_list()
                print 'before_delete:%d' % before_delete
                print '目前操作的序号是%d' % i
                if before_delete >= 1 and i <= before_delete:
                    cart.delete_product(i)
                    after_delete = self.get_the_length_of_list()
                    if before_delete - after_delete == 1:
                        print '删除产品成功'
                else:
                    print '购物车中无产品或该序号的产品已经删除，无法进行删除操作'
            times -= 1

    def check_operation(self):

        if self.get_the_length_of_list() == 0:
            self.create_operation()

    def close_cart_browser(self):
        cart.close_browser()


if __name__ == '__main__':
    crud = CRUD_MISS()
    print crud.get_the_length_of_list()
    crud.create_operation()
    crud.update_add_operation()


