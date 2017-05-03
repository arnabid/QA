# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:42:22 2017

@author: arnab
"""


def spiralPrint(arr):
    n = len(arr)
    res = []
    for gap in xrange(n):
        i, x = 0,[]
        for j in xrange(gap, -1, -1):
            x.append(arr[i][j])
            i += 1
        res.append(x)

    for gap in xrange(1,n):
        j, x = n-1, []
        for i in xrange(gap, n):
            x.append(arr[i][j])
            j -= 1
        res.append(x)

    return res
    

if __name__ == '__main__':
    arr = [[1,2], [3,4]]
    #arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    print (spiralPrint(arr))