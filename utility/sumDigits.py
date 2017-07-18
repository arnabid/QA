# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:25:49 2017

@author: arnab
"""

"""
find the sum of digits of a positive integer
"""

def findSumDigits(n):
    if n < 10:
        return n
    return n%10 + findSumDigits(n/10)

if __name__ == '__main__':
    n = 9729
    print (findSumDigits(n))
