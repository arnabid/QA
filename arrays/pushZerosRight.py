# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 07:44:59 2017

@author: arnab
"""

"""
pos = sentiniel position
pos = starting index of the left most zero pushed to the right
of the array
"""
def pushZeroRight(arr):
    n = len(arr)
    
    pos = n
    for i in xrange(n-1,-1,-1):
        if arr[i] == 0:
            j = i
            while j+1 < pos:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j += 1
            pos = pos - 1
    print (arr)


def pushZeroToRight(arr):
    n = len(arr)
    
    for i in xrange(n-1,-1,-1):
        if arr[i] == 0:
            j = i
            while j+1 < n:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j += 1
    print (arr)

"""
O(N) solution
use 2 pointers i - index of leftmost zero; j marches ahead
cases:
i j
0 X - swap, inc i, j
0 0 - inc j
X X - inc i, j
X 0 - inc i, j
reference: https://leetcode.com/problems/move-zeroes/tabs/description
"""
def moveZerosRight(arr):
    n = len(arr)
    i, j = 0, 1
    while j < n:
        if arr[i] == 0 and arr[j] == 0:
            j += 1
        else:
            if arr[i] == 0 and arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i] # swap
            i += 1
            j += 1
    print arr

if __name__ == '__main__':
    arr = [0,0,0,0,0,6,1,-3]
    moveZerosRight(arr)
    
        