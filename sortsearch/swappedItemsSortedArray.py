# -*- coding: utf-8 -*-
"""
Created on Mon May 22 08:06:04 2017

@author: arnab
"""

def findSwappedItems(arr):
    first = second = None
    prev = -float('inf')
    for item in arr:
        if first == None and prev > item:
            first = prev
        if first != None and prev > item:
            second = item
        prev = item
    return first, second

if __name__ == '__main__':
    arr = [12, 2, 3, 4, 5, 5, 8, 2]
    print (findSwappedItems(arr))