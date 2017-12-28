# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 08:22:18 2017

@author: arnab
"""

"""
fast exponentiation:
O(logN)
"""

def fastExponentiation(a, N):
    if N == 0:
        return 1
    elif N == 1:
        return a
    else:
        r = fastExponentiation(a, N//2)
        if N % 2 == 0:
            return r * r
        else:
            return r * r * a

if __name__ == '__main__':
    a, N = 2, 11
    print (fastExponentiation(a, N))
    