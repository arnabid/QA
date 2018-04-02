# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 07:59:03 2017

@author: arnab
"""

"""
searching in bitonic arrays
"""

def findMaxBitonic(arr, s, e):
    if s <= e:
        if s == e:
            return arr[s]
        mid = s + (e-s)/2
        if arr[mid] <= arr[mid+1]:
            return findMaxBitonic(arr, mid+1, e)
        else:
            return findMaxBitonic(arr, s, mid)


if __name__ == '__main__':
    arr = [2,4,6,10,16,17,16,3,1,-1]
    n = len(arr)
    print (findMaxBitonic(arr,0,n-1))
