# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:06:35 2017

@author: arnab
"""

"""
find the pair with the maximum product in the array
sol: find the 2 greatest and the 2 smallest elements; compare their products
"""

def findMaxProductPair(arr):
    mx1, mx2 = -float('inf'), -float('inf')
    mn1, mn2 = float('inf'), float('inf')
    for x in arr:
        if x > mx1:
            mx2 = mx1
            mx1 = x
        elif x > mx2:
            mx2 = x
        # find mins
        if x < mn1:
            mn2 = mn1
            mn1 = x
        elif x < mn2:
            mn2 = x

    if mx1*mx2 > mn1*mn2:
        return mx2, mx1
    else:
        return mn1, mn2


if __name__ == '__main__':
    arr = [-17,1,2,0,6,10,7,-3]
    print findMaxProductPair(arr)