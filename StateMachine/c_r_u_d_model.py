#coding=utf-8
import random
import string


class CRUD(object):
    def __init__(self):
        self.my_list = ['hzomu', 'mdqto', 'qljen', 'qurfaq', 'yrtkj']
        self.create_NO = 0
        self.read_NO = 0
        self.update_NO = 0
        self.del_NO = 0

    def gen_str(self):
        selector = [random.choice(string.ascii_lowercase) for i in range(5)]
        genStr = ''.join([i for i in selector])
        return genStr


    def create_operation(self):
        self.create_NO = random.randint(1, 6)
        print'这次新增了%d行' % self.create_NO

        for i in range(self.create_NO):
            self.my_list.append(self.gen_str())
            self.my_list = sorted(self.my_list)
        print '一共%d行' % (len(self.my_list))
        print self.my_list
        return self.my_list

    def read_operation(self):
        l = len(self.my_list)
        self.read_NO = random.randint(0, l - 1)
        print'本次读取的是第%d行' % (self.read_NO + 1)
        print self.my_list[self.read_NO]
        return self.my_list[self.read_NO]

    def update_operation(self):
        self.update_NO = random.randint(0, len(self.my_list) - 1)  #需要修改的行
        print '将要更新第%s行' % (self.update_NO + 1)
        li = self.my_list[self.update_NO]
        print'更新前的值是%s' % li
        self.my_list.pop(self.update_NO) #先将这行删除
        update_list = self.gen_str() + li
        print '更新后的值为%s' % update_list
        self.my_list.append(update_list)
        self.my_list = sorted(self.my_list)
        return self.my_list

    def delete_operation(self):

        # self.del_NO = random.randint(0, len(self.my_list) - 1)

        for i in self.getRandomNO():
            if i < len(self.my_list):
                print self.my_list[i]
                self.my_list.pop(i)
        return self.my_list

    def getRandomNO(self):
        i = random.randint(0, len(self.my_list) - 1)#获取随机值的个数
        num = [random.choice(list(range(i))) for a in range(0, i)]#
        return num


if __name__ == '__main__':
    c = CRUD()
    print c.create_operation()
    c.read_operation()
    print c.update_operation()
    print c.delete_operation()
    c.getRandomNO()
