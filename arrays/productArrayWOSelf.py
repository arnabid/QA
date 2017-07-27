# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 08:17:45 2017

@author: arnab
"""

"""
product of array except self
reference: https://leetcode.com/problems/product-of-array-except-self/#/description
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    res = [1] * n
    
    # res[i] = product of array elements to the left of i
    for i in xrange(1,n):
        res[i] = nums[i-1]*res[i-1]
    
    # accumulate product of array elements and traverse left
    k = nums[-1]
    for i in xrange(n-2,-1,-1):
        res[i] = res[i]*k
        k = k * nums[i]
    
    return res
