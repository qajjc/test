#coding=utf-8
import os

class Product(object):
    def __init__(self):
        self.name
        self.skuid
        self.price
        self.amount


products={
    '鸭梨脸':{'skuid':23202,'amount':1},
    '大饼脸':{'skuid':23203,'amount':1},
    '锥子脸':{'skuid':23204,'amount':1},
    '鞋拔子脸':{'skuid':23205,'amount':1},
    '猪腰子脸':{'skuid':23206,'amount':1},
    '透明':{'skuid':43757,'amount':1},
    '蓝莓':{'skuid':95539,'amount':1},
}

def get_product_info():
    path=os.path.dirname(__file__)#获取当前文件所在的路径
    filename='product_info.txt'
    f=file(path+os.sep+filename)
    line=f.readline()
    if len(line)==0:
        print 'the product info is null'
    else:
        product_info=eval(line)#需要将str转成字典

        return product_info

# print products['大饼脸']['skuid']
# print products.items()
# print products.keys()[1].decode('utf-8')

if  __name__=='__main__':
    product_info=get_product_info()
    print len(product_info.keys())
    print product_info[40969]['name']