# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:29:58 2016

@author: arnab
"""

if __name__ == '__main__':
#    arr = [3,3,4,5,6,7]
#    k = 10
#    n = len(arr)
#    i,j = 0,n-1
#    while i < j:
#        if arr[i] + arr[j] > k and j > 0:
#            j -= 1
#        if arr[i] + arr[j] == k and i != j:
#            print (i,j)
#        i += 1
    
    for i in xrange(3):
        for j in xrange(10):
            print (i,j)
            if j == 5:
                break

