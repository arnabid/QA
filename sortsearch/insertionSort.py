# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:38:24 2016

@author: arnab
"""

"""
insertion sort is an in-place and stable sort.
intuition: sorting a hand while playing cards

Factors that influence sorting time:
1) size of the input
2) if the input is already partially sorted

Worst case time is O(n^2), if the array is sorted in descending order

Invariant that remains true:
After we have processed the element at index 'i' E [0..n-1], the array[0:i] is sorted.

The total number of times the inner loop runs is equal to:
the number of inversions in the array, a[i] > a[j]; i < j

sort a k sorted array - O(nk)

For a partially sorted array; the number of swaps is equal to the number of
inversions in the array
"""
import random

def insertionSort(arr):
    n = len(arr)
    
    #ascending order
    for j in xrange(1,n):
        i = j-1
        
        while i >= 0 and arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    
    #descending order
    """
    for j in xrange(1,n):
        i = j-1
        
        while i >= 0 and arr[i] < arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    """
    
    return arr


if __name__ == '__main__':
    
    # set random seed
    random.seed()
    
    # generate test array
    arr = [random.randint(1,20) for i in xrange(10)]
    
    # create copy of test array
    res = list(arr)
    
    # sort test array and print result
    print (insertionSort(arr))
    
    # sort copy and print result
    res.sort()
    print (res)