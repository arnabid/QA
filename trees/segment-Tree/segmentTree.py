# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:26:54 2016

@author: arnab
"""

import math
from collections import Counter

def sumRange(st, ss, se, qs, qe, si):
    if qs > se or qe < ss:
        return 0
    
    if qs <= ss and qe >= se:
        return st[si]
    
    mid = ss + (se-ss)/2
    return sumRange(st, ss, mid, qs, qe, 2*si+1) + \
    sumRange(st, mid+1, se, qs, qe, 2*si+2)

# recursive implementation of the update function
def updateRecur(st, ss, se, i, diff, si):
    if i < ss or i > se:
        return
    if ss == se:
        st[si] += diff
        return
    mid = ss + (se-ss)/2
    updateRecur(st, ss, mid, i, diff, 2*si+1)
    updateRecur(st, mid+1, se, i, diff, 2*si+2)

def updateRange(st, ss, se, qs, qe, diff, si):
    if qe < ss or qs > se:
        return
    
    if ss == se:
        st[si] += diff
        return

    mid = ss + (se-ss)/2
    updateRange(st, ss, mid, qs, qe, diff, 2*si+1)
    updateRange(st, mid+1, se, qs, qe, diff, 2*si+2)
    st[si] = st[2*si+1] + st[2*si+2]

def update(i, diff):
    si = index[i]
    while si != 0:
        st[si] += diff
        si = (si-1) // 2
    st[si] += diff

def buildST(arr, st, ss, se, si):

    if ss == se: # child node
        st[si] = arr[ss]
        index[ss] = si
    else:
        mid = ss + (se-ss)/2
        buildST(arr, st, ss, mid, 2*si+1)
        buildST(arr, st, mid+1, se, 2*si+2)
        st[si] = st[2*si+1] + st[2*si+2]
    

if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(" "))
    n = len(arr) # leaves
    
    # calculate the size of the st array
    x = int (math.ceil(math.log(n) / math.log(2)))
    max_size = 2 * (2**x) - 1
    print (max_size)
    
    st = [0]*max_size
    
    # index is the dictionary that maps arr[index] to st[index]
    index = Counter()
    
    # build the segment tree
    buildST(arr, st, 0, n-1, 0)
    print (index)
    print (st)

    # find the sum of arr[qs:qe]
    qs, qe = map(int, raw_input().strip().split(" "))
    print (sumRange(st, 0, n-1, qs, qe, 0))
    
    # update arr[i] to new_val; get the index and new value from stdin
    i, new_val = map(int, raw_input().strip().split(" "))
    diff = new_val - arr[i]
    arr[i] = new_val
    #update(i, diff)
    updateRecur(st, 0, n-1, i, diff, 0)
    print (arr)
    print (st)

    # update all the values in a range
    qs, qe, diff = map(int, raw_input().strip().split(" "))
    updateRange(st, 0, n-1, qs, qe, diff, 0)
    print (sumRange(st, 0, n-1, qs, qe, 0))
    
    