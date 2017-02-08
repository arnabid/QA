# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:49:55 2016

@author: arnab
"""
import random
def rotate(arr):
    r = len(arr)
    c = len(arr[0])
    # transpose arr
    for i in xrange(r-1):
        for j in xrange(i+1,c):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    print (arr)
    for j in xrange(c/2):
        # exchange the j and the n-1-j column
        for i in xrange(r):
            arr[i][j], arr[i][c-1-j] = arr[i][c-1-j], arr[i][j]
    print (arr)

if __name__ == '__main__':
    # rotate the matrix 90 degrees clockwise
    rows, cols = 4, 4
    arr = [[random.randint(1,9) for i in xrange(cols)] for i in xrange(rows)]
    print (arr)
    rotate(arr)