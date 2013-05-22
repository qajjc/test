#coding=utf-8 
import requests
import os
            
def send_post_request(request_url_header, sub_request_url, data):
    try:
        request_url="%s%s"%(request_url_header,sub_request_url)
        r = requests.post(request_url, data=data)
        print "=============="
        print r.text
        print "=============="
        message = r.text
        if message.find("msgId") == -1:
            raise RuntimeError("Send Message Fail")
    except Exception,e:
        print e

def send_post_request_with_file(request_url_header, sub_request_url, data, files):
    for key, value in data.items():
        print "%s:%s" % (key,value)
    try:
        request_url="%s%s"%(request_url_header,sub_request_url)
        r = requests.post(request_url, data=data, files=files)
        print r.status_code
        print r.text
        print r.headers
        message = r.text
        if message.find("msgId") == -1:
            raise RuntimeError("Send Message Fail")
    except Exception,e:
        print e 
        
def download_apk(request_url, apk_path, apk_name):
    try:
        r = requests.get(request_url) 
        with open(apk_path+os.sep+apk_name, "wb") as code:
            code.write(r.content)
    except Exception,e:
        print e
        raise e

def get_request(request_url_header, sub_request_url):
    try:
        request_url='%s%s'%(request_url_header,sub_request_url)
        r = requests.get(request_url)
        print "=============="
        # print(r.headers)
        print 'Data:%s | StatusCode:%s'%(r.text,r.status_code)
        print "=============="
        return r.text
    except Exception,e:
        print e

if __name__=="__main__":
    print get_request("http://mon0.photo.163.org:18080/online/object/get?uuid=wutongya","")
#     send_post_request_with_file()
#     send_post_request_with_attach_file()

    # download_apk("http://10.240.155.199:8001/drill/Drill-Test1-G2-V1.apk","d:\\Drill-Test1-G2-V1.apk"
