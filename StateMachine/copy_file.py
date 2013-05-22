#coding=utf-8
import os
import shutil
# import tempfile
import time


def copy_log_to_logfile():
    path = os.path.dirname(__file__)#获取当前文件所在的路径
    filename1 = path + os.sep + 'test.log'
    temp = str(time.strftime("%Y-%m-%d,%H-%M-%S", time.localtime())) + '.log'
    if os.path.isdir(path + os.sep +'test_log'):
        filename2 = path + os.sep + 'test_log' + os.sep + temp
    else:
        os.mkdir(path + os.sep +'test_log')
        filename2 = path + os.sep + 'test_log' + os.sep + temp
    print filename1, "=>", filename2
    shutil.copy(filename1, filename2)
    f=open(filename1,'w')
    f.close()

    # os.remove(filename1)
    # shutil.move(filename2,)
    # os.remove(filename1)
    # os.rename(filename1,filename2)


if __name__ == '__main__':
    copy_log_to_logfile()

# filename1 = tempfile.mktemp (".txt")
# open (filename1, "w").close ()
# filename2 = filename1 + ".copy"
# print filename1, "=>", filename2
#
# #拷文件
# shutil.copy (filename1, filename2)
#
# if os.path.isfile (filename2): print "Success"
#
# dirname1 = tempfile.mktemp (".dir")
# os.mkdir (dirname1)
# dirname2 = dirname1 + ".copy"
# print dirname1, "=>", dirname2
#
# #拷目录
# shutil.copytree (dirname1, dirname2)
#
# if os.path.isdir (dirname2): print "Success"
