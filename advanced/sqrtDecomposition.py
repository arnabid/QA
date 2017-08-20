# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:24:36 2017

@author: arnab
"""

"""
sqrt decomposition
reference: https://www.youtube.com/watch?v=gWbDocYhwDA
divide array into blocks of size = ceil(sqrt(n))
"""
import math


"""
build the blocks structure
"""
def build(arr):
    n = len(arr)
    nblocks = int(math.ceil(n**0.5)) # number of blocks
    blocks = [0]*nblocks
    
    for i in xrange(n):
        blocks[i/nblocks] += arr[i]
    
    return blocks

"""
update arr[i] to k
"""
def update(arr, blocks, i, k):
    nblocks = len(blocks)
    blocks[i/nblocks] += k - arr[i]
    arr[i] = k


"""
return the sum of arr[l...r]
"""
def sumQuery(arr, blocks, l, r):
    nblocks = len(blocks)
    startblock, endblock = l/nblocks, r/nblocks
    res = 0
    
    # sum of blocks between start block and end block
    for i in xrange(startblock+1, endblock):
        res += blocks[i]
    
    # calculate last index of start block
    lp_end = (startblock+1)*nblocks
    lp_end = min(lp_end, r+1)
    for i in xrange(l, lp_end):
        res += arr[i]
    
    # calculate first index of end block
    rp_start = (endblock)*nblocks
    rp_start = max(rp_start, l)
    for i in xrange(rp_start, r+1):
        res += arr[i]
    
    if startblock == endblock:
        res = res/2
    return res

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10,11]
    n = len(arr)
    blocks = build(arr)
    for i in xrange(n):
        for j in xrange(i,n):
            print i,j," Sum = ",sumQuery(arr, blocks, i, j)
