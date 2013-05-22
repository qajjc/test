#coding=utf-8
'''
冒泡排序算法
'''
def bubbleSort(L):
    assert (type(L) == type(['']))
    length = len(L)
    if length == 0 or length == 1:
        return L
    for i in xrange(length):
        for j in xrange(length - 1 - i):
            if L[j] > L[j + 1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
    return L


if __name__=='__main__':
    l=['hzomu', 'bmdqto', 'bqljen', 'qurfaq', 'yrtkj','azzz','azzbz']
    print bubbleSort(l)