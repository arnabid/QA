# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 09:44:56 2016

@author: arnab
"""

""" Pick max weight independent set from n items """

def solution(ml):
    n = len(ml)
    A = []
    A.append(0)
    A.append(ml[0])
    
    for i in xrange(2,n+1):
        A[i] = max(A[i-1], A[i-2] + ml[i-1])
    
    return A[-1]
    

if __name__ == '__main__':
    ml = [5,3,6]
    print (solution(ml))