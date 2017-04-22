# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:29:58 2017

@author: arnab
"""


"""
Given an array of integers, every element appears twice except for one.
Find that single one.

Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
def singleNumber(A):
    x = 0
    for i in A:
        x ^= i
    return x