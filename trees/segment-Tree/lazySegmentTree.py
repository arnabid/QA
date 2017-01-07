# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:20:35 2017

@author: arnab
"""

"""
Lazy propagation in a segemnt tree to find the sum of given range.

When there are many updates and updates are done on a range, 
we can postpone some updates (avoid recursive calls in update) 
and do those updates only when required.
reference: http://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/
"""

import math


def updateRange(st, lazy, ss, se, qs, qe, diff, si):
    if lazy[si] != 0:
        st[si] += (se-ss+1) * lazy[si]
        
        if ss != se:
            lazy[2*si+1] += lazy[si]
            lazy[2*si+2] += lazy[si]
        
        lazy[si] = 0
    
    if qe < ss or qs > se:
        return
    
    if qs <= ss and qe >= se:
        st[si] += (se-ss+1) * diff
        
        if ss != se:
            lazy[2*si+1] += diff
            lazy[2*si+2] += diff
        return
    
    mid = ss + (se-ss)/2
    updateRange(st, lazy, ss, mid, qs, qe, diff, 2*si+1)
    updateRange(st, lazy, mid+1, se, qs, qe, diff, 2*si+2)
    st[si] = lazy[2*si+1] + lazy[2*si+2]

def sumRange(st, lazy, ss, se, qs, qe, si):
    if lazy[si] != 0:
        st[si] += (se-ss+1) * lazy[si]
        
        if ss != se:
            lazy[2*si+1] += lazy[si]
            lazy[2*si+2] += lazy[si]
        
        lazy[si] = 0
    
    if qe < ss or qs > se:
        return 0
    
    if qs <= ss and qe >= se:
        return st[si]

    mid = ss + (se-ss)/2
    return sumRange(st, lazy, ss, mid, qs, qe, 2*si+1) + \
    sumRange(st, lazy, mid+1, se, qs, qe, 2*si+2)

def buildST(arr, st, ss, se, si):

    if ss == se: # child node
        st[si] = arr[ss]
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
    
    st = [0] * max_size
    lazy = [0] * max_size
    
    # build the segment tree
    buildST(arr, st, 0, n-1, 0)

    # update all the values in a range
    qs, qe, diff = map(int, raw_input().strip().split(" "))
    updateRange(st, lazy, 0, n-1, qs, qe, diff, 0)
    print (sumRange(st, lazy, 0, n-1, qs, qe, 0))
