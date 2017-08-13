# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 08:35:56 2017

@author: arnab
"""

"""
bubble sort
stable sorting algorithm
"""

import random

def bubbleSort(arr):
    n = len(arr)
    
    # in each iteration move the largest element to the right end of the array
    inv = 0 # number of inversions in the array
    for i in xrange(n-1, 0, -1):
        swap = False
        for j in xrange(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                inv += 1
                swap = True
        if not swap:
            break
    
    print (inv)
    return arr


if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(10)]
    
    # create copy of test array
    res = list(arr)
    
    # sort test array and print result
    print (bubbleSort(arr))
    
    # sort copy and print result
    res.sort()
    print (res)