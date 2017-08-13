# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:30:29 2017

@author: arnab
"""

"""
Selection sort - select the min element and put it
in its correct position
"""
import random

def selectionSortVER1(arr):
    n = len(arr)
    
    for i in xrange(n-1):
        mi = i
        for j in xrange(i+1, n):
            if arr[j] < arr[mi]:
                mi = j
        arr[i], arr[mi] = arr[mi], arr[i]
    return arr


def selectionSortVER2(arr):
    n = len(arr)
    
    for i in xrange(n-1):
        for j in xrange(i+1, n):
            # does unnecessary swaps
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(10)]
    
    # create copy of test array
    res = list(arr)
    
    # sort test array and print result
    print (selectionSortVER1(arr))
    
    # sort copy and print result
    res.sort()
    print (res)