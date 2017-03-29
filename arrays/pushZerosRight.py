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

if __name__ == '__main__':
    arr = [0,0,0,0,0,6,1,-3]
    pushZeroRight(arr)
    
        