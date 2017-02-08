# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:51:10 2016

@author: arnab
"""

""" Number of distinct binary strings of length n without any consecutive 1s """
# TODO: number of distinct binary strings w/o any consecutive 0s  and is the remaining strings
# such that there are no consecutive 1s and 0s.

def solution(n):
    """ let a[i] be the number of strings of length 'i' w/o consecutive 1s ending in 0
    and b[i] be the number of such strings ending in 1
    Then a[i] = a[i-1] + b[i-1]
    b[i] = a[i-1] """
    
    a, b = 1,1
    for i in xrange(1,n):
        a,b = a+b,a
    return a+b
    

if __name__ == '__main__':
    n = 4
    print (solution(n))