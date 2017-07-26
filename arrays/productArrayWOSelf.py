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
    res = [1]*len(nums)
    
    # res[i] = product of array elements to the left of i
    for i in range(1,len(nums)):
        res[i] = nums[i-1]*res[i-1]
    
    # accumulate product of array elements and traverse left
    k = 1
    for i in range(len(nums)-2,-1,-1):
        k = k*nums[i+1]
        res[i] = res[i]*k
    
    return res
