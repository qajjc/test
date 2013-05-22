#coding=utf-8
from ystore.MysqlConnect import execute_sql


def count_sku_NO():
    '''
    计算购物车中有多少个sku
    '''
    sql = 'SELECT COUNT(id) FROM TB_Ystore_CartItem WHERE Userid=78244;'
    result = execute_sql(sql)
    for r in result:
        amount = r[0]
    return amount


def count_all_products():
    '''
     计算购物车中所有产品的数量
    '''
    sql = 'SELECT SUM(Count) FROM TB_Ystore_CartItem WHERE UserId = 78244;'
    result = execute_sql(sql)

    for r in result:
        total = r[0]
    return total


def count_sku_products():
    '''
    检查购物车中，每个对应skuid所包含的产品个数。
    '''
    sql = 'SELECT skuid,COUNT FROM TB_Ystore_CartItem,TB_Ystore_SkuCartItem WHERE TB_Ystore_SkuCartItem.userid=78244 AND TB_Ystore_CartItem.Id =TB_Ystore_SkuCartItem.CartItemId'
    result = execute_sql(sql)
    count = []
    skuid = []
    for r in result:
        skuid.append(r[0])
        count.append(r[1])
        # print skuid,count
    dict = {}
    for i in range(0, len(count)):
        dict[skuid[i]] = count[i]
        # print dict
    return dict


def get_the_list_of_skuid():
    '''
    获取库存大于0 的skuid
    '''
    sql = 'SELECT id FROM TB_Ystore_Sku WHERE SellVolume >5 AND Valid=1;'
    result = execute_sql(sql)
    skuid_list = []
    for r in result:
        skuid_list.append(r[0])
    return skuid_list




def get_the_name_and_description_of_skuid():
    '''
    获取skuid对应的产品名以及产品描述,返回的格式是{skuid:{'name':'','desc':''}}
    '''
    sql = 'SELECT TB_Ystore_ProductSkuSpecMap.SkuId,TB_Ystore_Product.NAME,TB_Ystore_SkuSpecOptionValue.OpDesc FROM TB_Ystore_SkuSpec,TB_Ystore_SkuSpecOptionValue,TB_Ystore_ProductSkuSpecMap,TB_Ystore_Product,TB_Ystore_Sku WHERE TB_Ystore_SkuSpec.Id =TB_Ystore_SkuSpecOptionValue.SkuSpecId AND TB_Ystore_ProductSkuSpecMap.SkuSpecId=TB_Ystore_SkuSpecOptionValue.SkuSpecId AND TB_Ystore_ProductSkuSpecMap.SkuSpecOptionValueId=TB_Ystore_SkuSpecOptionValue.Id AND TB_Ystore_Product.Id=TB_Ystore_Sku.ProductId AND TB_Ystore_Sku.Id=TB_Ystore_ProductSkuSpecMap.SkuId'
    result = execute_sql(sql)
    skuid = []
    name = []
    desc = []
    dict = {
    }
    for r in result:
        skuid.append(r[0])
        name.append(r[1])
        desc.append(r[2])
    for i in range(0, len(skuid)):
        dict[i]={'skuid':'','name': '', 'desc': ''}
        dict[i]['skuid']= skuid[i]
        dict[i]['name'] = name[i]
        dict[i]['desc'] = desc[i]
    # return dict
    f=open('product_info.txt','w')
    f.write(str(dict))
    f.close()



if __name__ == '__main__':
    # print count_sku_NO()
    # print count_all_products()
    # print count_sku_products()
    # print get_the_list_of_skuid()
    get_the_name_and_description_of_skuid()
