# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 22:26:08 2017

@author: arnab
"""

"""
Rotate function
reference: https://leetcode.com/problems/rotate-function/#/description
"""

def maxRotateFunction(self, arr):
    """
    :type A: List[int]
    :rtype: int
    """
    n = len(arr)
    s = ls = rs = 0
    ss = sum(arr)

    lsum, rsum = {}, {}
    # lsum[i] - sum of arr elements [0...i)
    # rsum[i] - sum of arr elements [i+1...n)
    for i in xrange(n-1,0,-1):
        ls += arr[i]
        lsum[i] = ss - ls
        rsum[i] = rs
        rs += arr[i]
        
        # calculate initial sum
        s += i*arr[i]
    ans = s
    for i in xrange(n-1,0,-1):
        s += lsum[i] + rsum[i] - arr[i]*(n-1)
        ans = max(ans, s)
    return ans
