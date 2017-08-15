# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:34:46 2017

@author: arnab
"""

"""
shell sort
reference: 
https://www.youtube.com/watch?v=0sUVZlHrZGg&index=22&list=PLxc4gS-_A5VDXUIOPkJkwQKYiT2T1t0I8
"""

import random

def shellSort(arr):
    n = len(arr)
    
    h = 1
    while h < n/3:
        h = 3*h + 1  # 1, 4, 13, 40, 121, ....
    
    while h >= 1:
        for i in xrange(h, n):
            j = i
            while j >= h and arr[j] < arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
        h = h/3
    return arr

if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(17)]
    
    # create copy of test array
    res = list(arr)
    
    # sort test array and print result
    print (shellSort(arr))
    
    # sort copy and print result
    res.sort()
    print (res)