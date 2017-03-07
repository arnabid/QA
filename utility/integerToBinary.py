# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 11:28:53 2017

@author: arnab
"""

"""
integer to binary
"""

def recursionIntegerToBinary(n):
    if n == 0:
        return
    recursionIntegerToBinary(n >> 1)
    print (n % 2),

def integerToBinary(n):
    s = []
    while n > 0:
        s.append(n % 2)
        n = n >> 1
    print (s[::-1])

if __name__ == '__main__':
    #integerToBinary(11)
    recursionIntegerToBinary(8)
    