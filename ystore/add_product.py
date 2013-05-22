import random,logging
import requests
from ystore.DDBOperation import get_the_list_of_skuid

# logger=logging.getLogger(__name__)
logger=logging.getLogger('crud')

def add_product_by_http_request():
    skuid_list = get_the_list_of_skuid()
    skuId = random.choice(skuid_list)
    num = random.randint(1, 2)
    url = 'http://miss.163.com/cart/addToCart.json?skuId=' + str(skuId) + '&num=' + str(num)
    logger.info(url)
    cookies = get_cookies()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Connection": "Keep-Alive", "Referer": "http://miss.163.com/prod?productId=23201",
        "Cookie": cookies,
    }

    r = requests.get(url, headers=headers)
    if r.text.endswith('true}'):
        logger.info('add product success')
    else:
        # print'add product fail'
        logger.error('add product fail')


def get_cookies():
    url = 'https://reg.163.com/logins.jsp?product=lede&domains=lede.com&url=http%3A%2F%2Fmiss.163.com%2F'
    post_data = {
        'username': 'qajjc01@163.com',
        'password': 'qa1234'
    }
    r = requests.post(url, post_data)
    return r.headers['set-cookie']
    # print "=============="
    # print r.headers['set-cookie']
    # print "=============="
    # for i in r.text.split('var url = "'):
    #     if i.startswith('http://reg.lede.com'):
    #         temp = i
    #
    # url_miss163 = temp.split('var ')[0].split('"')[0].encode('utf-8')
    # print url_miss163
    # strinfo = re.compile('crossdomain')
    # url_miss163 = strinfo.sub('next',url_miss163)
    # print url_miss163
    # req = requests.get(url_miss163)
    #
    # print req.text


if __name__ == '__main__':
    # print get_cookies()
    add_product_by_http_request()