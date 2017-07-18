# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 07:45:03 2017

@author: arnab
"""

import math

"""
reverse an integer
"""

def reverseInteger(n):
    res = 0
    
    flag = 1
    if n < 0:
        flag = -1
    
    n = abs(n)
    t = int(math.log(n, 10))
    
    while n > 0:
        res += (n%10) * (10**t)
        n = n/10
        t -= 1

    if flag == 1 and res > 2**32-1:
        return 0
    
    if flag == -1 and res > 2**32:
        return 0
    
    return res*flag

if __name__ == '__main__':
    n = -89
    print reverseInteger(n)
