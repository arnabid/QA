# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:50:03 2017

@author: arnab
"""
import random

def quickSort(arr, l, r): # sort arr[l...r-1]
    if r - l <= 1:
        return
    yellow = l+1
    for green in xrange(l+1, r):
        if arr[green] <= arr[l]:
            arr[green], arr[yellow] = arr[yellow], arr[green]
            yellow += 1
    arr[l], arr[yellow-1] = arr[yellow-1], arr[l]
    quickSort(arr, l, yellow-1)
    quickSort(arr, yellow, r)


if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(10)]
    
    # create copy of test array
    res = list(arr)
    
    # sort test array and print result
    quickSort(arr, 0, len(arr))
    print (arr)
    
    # sort copy and print result
    res.sort()
    print (res)