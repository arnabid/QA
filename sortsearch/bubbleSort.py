# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 08:35:56 2017

@author: arnab
"""

def bubbleSort(arr):
    n = len(arr)
    
    for i in xrange(n-1):
        swap = False
        for j in xrange(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    
    return arr


if __name__ == '__main__':
    arr = [4,3,5,2,1,12,10]
    print (bubbleSort(arr))