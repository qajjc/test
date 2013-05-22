#coding=utf-8
import MySQLdb

def execute_sql(sql):
    connection = MySQLdb.connect(host='jipiao1.photo.163.org', user='mysql', passwd='mysql', db='ystore-test',
                                          port=4332,charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


if __name__ == '__main__':

    result = execute_sql('SELECT COUNT(id) FROM TB_Ystore_CartItem WHERE Userid=78244;')
    for r in result:
        print r[0]


