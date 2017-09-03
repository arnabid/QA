# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:39:39 2017

@author: arnab
"""

"""
given an array of non-negative integers, select integers that maximize the total sum
subject to the condition that adjacent integers cannot be selected.

Reference:
https://leetcode.com/problems/house-robber/description/
"""

def rob(self, arr):
    # return 0 if arr is empty
    if not arr:
        return 0

    # array size
    n = len(arr)
    
    # at each i, calculate the maximum amount in arr[0...i]
    # if arr[i] is included or not included
    inc, ninc = 0, 0
    for i in range(n):
        # inc[i] = arr[i] + ninc[i-1]
        # ninc[i] = max(inc[i-1], ninc[i-1])
        inc, ninc = arr[i] + ninc, max(inc, ninc)
    return max(inc, ninc)

"""
Bonus: Also find the integers that are in the final solution
"""
def robBonus(self, arr):
    # return 0 if arr is empty
    if not arr:
        return 0

    # array size
    n = len(arr)
    
    # at each i, calculate the maximum amount in arr[0...i]
    # if arr[i] is included or not included
    inc, ninc = 0, 0
    status, res = [], []
    for i in range(n):
        # inc[i] = arr[i] + ninc[i-1]
        # ninc[i] = max(inc[i-1], ninc[i-1])
        inc, ninc = arr[i] + ninc, max(inc, ninc)
        status.append([inc, ninc])
    ans = max(inc, ninc)
    
    i = n-1
    while i >= 0:
        if status[i][0] > status[i][1]:
            res.append(arr[i])
            i -= 2
        else:
            i -= 1
    return ans, res
