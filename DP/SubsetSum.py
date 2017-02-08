# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:50:24 2016

@author: arnab
"""

""" Find if a subset from a given set of N non-negative integers sums upto
a given value K """

def solution(S,k):
    S.insert(0,0)
    n = len(S)
    A = [[False for i in xrange(k+1)] for i in xrange(n)]
    
    # make the first column True
    for i in xrange(n):
        A[i][0] = True
    
    #print (A)
    for j in xrange(1,k+1):
        for i in xrange(1,n):
            if A[i-1][j] == True:
                A[i][j] = True
            elif j - S[i] >= 0:
                A[i][j] = A[i-1][j - S[i]]
            # else: default value is false initially
    
    print (A)
    return A[-1][-1]

if __name__ == '__main__':
    k = 5
    S = [1,3,2,4]
    print (solution(S, k))