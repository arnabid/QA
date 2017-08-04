# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 08:03:47 2017

@author: arnab
"""

"""
find the duplicates in array; 1 ≤ a[i] ≤ n (n = size of array)
reference: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
"""

def findDuplicates(arr):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not arr:
        return []
    res = []
    for i in xrange(len(arr)):
        if arr[abs(arr[i])-1] < 0:
            res.append(abs(arr[i]))
        arr[abs(arr[i])-1] *= -1
    return res
