# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:38:47 2016

@author: arnab
"""

"""
Merge sort: http://quiz.geeksforgeeks.org/merge-sort/
stable sorting algorithm; nlogn time, n space
counts the number of inversions; i < j and arr[i] > arr[j]
"""

import random

inversions = [0]

def merge(arr, temp, low, mid, high):    
    i,j,k = low,mid+1,low
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inversions[0] += mid-i+1
            j += 1
        k += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in xrange(low, high+1):
        arr[i] = temp[i]

def mergesort(arr, temp, low, high):
    if low < high:
        mid = low + (high-low)//2
        
        mergesort(arr, temp, low, mid)
        mergesort(arr, temp, mid+1, high)
        
        merge(arr, temp, low, mid, high)


def _mergesort(arr, low, high):
    temp = [0] * (high-low+1)
    mergesort(arr, temp, low, high)



if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(10)]
    print (arr)
    
    # sort test array and print result
    _mergesort(arr, 0, len(arr)-1)
    print (arr)
    
    # print the number of inversions in the array
    print ("The number of inversions = {} ".format(inversions[0]))