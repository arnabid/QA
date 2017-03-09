# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:29:58 2016

@author: arnab
"""

"""
find pairs that sum to a given value
array is sorted; array has distinct elements
"""
def sol(arr, k):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == k:
            print (i,j)
            i += 1
            j -= 1
        elif arr[i] + arr[j] > k:
            j -= 1
        else:
            i += 1

if __name__ == '__main__':
    arr = [3,4,5,6,7]
    k = 10
    sol(arr, k)
