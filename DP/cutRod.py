# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:24:27 2017

@author: arnab
"""

"""
rod cutting problem
reference: CLRS: pg 360
"""

""" recursive solution """
def cutRod(p, n):
    if n == 0:
        return 0
    
    q = -float('inf')
    for i in xrange(1,n+1):
        q = max(q, p[i] + cutRod(p, n-i))
    return q

""" top down with memoization"""
def cutRodM(p,n):
    r = [-float('inf')] * len(n)+1
    return cutRodMAux(p,n,r)

def cutRodMAux(p,n,r):
    if r[n] >= 0:
        return r[n]
    
    q = None
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in xrange(1,n+1):
            q = max(q, p[i] + cutRodMAux(p,n-i,r))
    r[n] = q
    return q

""" bottom-up method """
def BUcutRod(p,n):
    r = [-float('inf')] * len(n)+1
    r[0] = 0
    s = [0] * len(n)+1

    for j in xrange(1, n+1):
        q = -float('inf')
        for i in xrange(1,j+1):
            if p[i] + r[j-i] > q:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r[n], s
