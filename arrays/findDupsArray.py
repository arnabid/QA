# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 08:03:47 2017

@author: arnab
"""

"""
find the duplicates in array; 1 ≤ a[i] ≤ n (n = size of array)
reference: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
solution: https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/218682/Python-Negative-Notation
"""

def findDuplicates(arr):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    n = len(arr)
    for i in range(n):
        index = abs(arr[i]) - 1
        if arr[index] > 0:
            arr[index] = -arr[index]
        elif arr[index] < 0:
            res.append(abs(arr[i]))
    return res
