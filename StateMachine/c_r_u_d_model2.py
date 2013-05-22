#coding=utf-8
import random
import string
from StateMachine.bubble_sort import bubbleSort

class CRUD_Operation(object):
    def __init__(self):
        self.my_list = ['hzomu', 'mdqto', 'qljen', 'qurfaq', 'yrtkj']



    def gen_str(self):
        selector = [random.choice(string.ascii_lowercase) for i in xrange(5)]
        genStr = ''.join([i for i in selector])
        return genStr

    def getRandomNO(self):
        i = random.randint(0, len(self.my_list))#获取随机值的个数
        num = [random.choice(list(range(i))) for a in range(i)]#
        print num
        return num

    def generate_operate_position(self):
        i = random.choice([1,2,3])
        if i == 1:
            print '本次操作位于第一个位置'
            num=[0]
            return num
        elif i == 2 :
            print '本次操作的位于最后一个位置'
            num=[-1]
            return num
        elif i == 3:
            k = random.randint(0, len(self.my_list))#获取随机值的个数
            print '本次将随机操作%d个位置' % k
            num = [random.choice(list(range(k))) for a in range(k)]#
            print'具体的序号如下：'
            print num
            return num

    def create_operation(self):
        self.create_NO = random.randint(1, 8)
        print'这次新增了%d元素' % self.create_NO
        for i in range(self.create_NO):
            self.my_list.append(self.gen_str())
            self.my_list = bubbleSort(self.my_list)
        print '一共%d个元素' % (len(self.my_list))
        return self.my_list

    def read_operation(self):
        print'='*4+'读取的元素'+'='*4
        for i in self.generate_operate_position():
            print self.my_list[i]

    def update_operation(self):
        print'='*4+'更新的元素'+'='*4
        for i in self.generate_operate_position():
            update_list=self.my_list[i]
            self.my_list.pop(i)
            new_list=update_list+self.gen_str()
            self.my_list.append(new_list)
            self.my_list = bubbleSort(self.my_list)
        return self.my_list


    def delete_operation(self):
        print'='*4+'删除的元素'+'='*4
        for i in self.generate_operate_position():
            if i < len(self.my_list):
                print self.my_list[i]
                self.my_list.pop(i)
        return self.my_list

class CRUD_Manger(object):
    pass



if __name__ == '__main__':
    c = CRUD_Operation()
    print c.create_operation()
    c.read_operation()
    print c.update_operation()
    print c.delete_operation()



