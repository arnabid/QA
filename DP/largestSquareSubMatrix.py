# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:01:46 2017

@author: arnab
"""

"""
Maximum size square sub-matrix with all 1s
reference: http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
"""
import random

def sol(arr):
    r, c = len(arr), len(arr[0])
    s = [[0 for i in xrange(c)] for i in xrange(r)]
    ans, maxi, maxj = arr[0][0], 0, 0
    
    # copy the first row
    for i in xrange(c):
        s[0][i] = arr[0][i]
        if s[0][i] > ans:
            ans, maxi, maxj = 1, 0, i
    
    # copy the first column
    for i in xrange(r):
        s[i][0] = arr[i][0]
        if s[i][0] > ans:
            ans, maxi, maxj = 1, i, 0
    
    for i in xrange(1, r):
        for j in xrange(1, c):
            if arr[i][j] == 1:
                s[i][j] = min(s[i][j-1], s[i-1][j-1], s[i-1][j]) + 1
                if s[i][j] > ans:
                    ans, maxi, maxj = s[i][j], i, j
    
    # return the size of the largest square sub-matrix
    # and the top left and bottom right corner
    return ans, (maxi-ans+1, maxj-ans+1), (maxi, maxj)

if __name__ == '__main__':
    arr = [[random.randint(0,1) for i in xrange(5)] for i in xrange(5)]
    print (arr)
    print (sol(arr))