# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 08:00:42 2017

@author: arnab
"""

"""
find the kth smallest element in array
using the quick select method
worst case - O(n^2); average case - O(n)
"""

def quickSelect(arr, l, r, k): # sort elements in arr[l...r-1]
    if r - l <= 1:
        return arr[l]
    
    y = l+1
    for g in xrange(l+1, r):
        if arr[g] <= arr[l]:
            arr[g], arr[y] = arr[y], arr[g]
            y += 1
    
    # swap with pivot
    arr[y-1], arr[l] = arr[l], arr[y-1]
    
    # check if pivot position (y-1) is equal to desired position
    if k-1 == y-1:
        return arr[k-1]
    # desired position less than pivot position - recurse only left of pivot
    elif k-1 < y-1:
        return quickSelect(arr, l, y-1, k)
    # else recurse only right of pivot
    else:
        return quickSelect(arr, y, r, k)


if __name__ == '__main__':
    arr = [1,4,7,2,9,8]
    n = len(arr)
    k = 2
    
    if k < 1 or k > n:
        raise ValueError("invalid value of k; valid range is [1...n]")
    
    print (quickSelect(arr, 0, n, k))
