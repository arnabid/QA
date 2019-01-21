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
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                rs.add(i)
                cs.add(j)
    
    for i in range(c):
        for j in range(c):
            if i in rs or j in cs:
                arr[i][j] = 0
    
    print (arr)

if __name__ == '__main__':
    rows,cols = 4,4
    arr = [[1 for i in range(cols)] for i in range(rows)]
    arr[0][0] = 0
    setZeros(arr)