# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:31:28 2016

@author: arnab
"""
def setZeros(arr):
    # makes the entire row and column of arr zero if arr[i][j] = 0
    r = len(arr)
    c = len(arr[0])
    rs, cs = set(), set()
    for i in xrange(r):
        for j in xrange(c):
            if arr[i][j] == 0:
                rs.add(i)
                cs.add(j)
    
    for i in xrange(c):
        for j in xrange(c):
            if i in rs or j in cs:
                arr[i][j] = 0
    
    print (arr)

if __name__ == '__main__':
    rows,cols = 4,4
    arr = [[1 for i in xrange(cols)] for i in xrange(rows)]
    arr[0][0] = 0
    setZeros(arr)