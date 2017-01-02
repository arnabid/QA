# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:56:16 2017

@author: arnab
"""

"""
Range Minimum Query
Reference: http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
"""

import math

def buildST(arr, st, ss, se, si):
    if ss == se:
        st[si] = arr[ss]
    else:
        mid = ss + (se-ss)/2
        st[si] = min(buildST(arr, st, ss, mid, 2*si+1), \
        buildST(arr, st, mid+1, se, 2*si+2))
    return st[si]

def findMin(st, ss, se, qs, qe, si):
    if qe < ss or qs > se:
        return float('inf')
    
    if qs <= ss and qe >= se:
        return st[si]
    
    mid = ss + (se-ss)/2
    return min(findMin(st, ss, mid, qs, qe, 2*si+1), \
    findMin(st, mid+1, se, qs, qe, 2*si+2))

if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(" "))
    n = len(arr) # leaves
    
    # calculate the size of the st array
    x = int (math.ceil(math.log(n) / math.log(2)))
    max_size = 2 * (2**x) - 1
    print (max_size)
    
    st = [0] * max_size
    
    # build the segment tree
    buildST(arr, st, 0, n-1, 0)
    
    # find the min in arr[qs:qe]; inclusive of qs and qe
    qs, qe = map(int, raw_input().strip().split(" "))
    print (findMin(st, 0, n-1, qs, qe, 0))
    