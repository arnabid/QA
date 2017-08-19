# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:38:47 2016

@author: arnab
"""

"""
Merge sort: http://quiz.geeksforgeeks.org/merge-sort/
stable sorting algorithm
"""

import random

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    
    L = arr[low:mid+1]
    R = arr[mid+1:high+1]
    
    i,j,k = 0,0,low
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

def mergesort(arr, low, high):
    if low < high:
        mid = low + (high-low)/2
        
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        
        merge(arr, low, mid, high)

if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(10)]
    
    # create copy of test array
    res = list(arr)
    
    # sort test array and print result
    mergesort(arr, 0, len(arr)-1)
    print (arr)
    
    # sort copy and print result
    res.sort()
    print (res)