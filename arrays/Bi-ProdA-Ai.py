# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:19:18 2017

@author: arnab
"""

"""
Given an array A, how would you create an array B where for each i from 0 to n, 
b[i] = a[0] * a[1] * ... * a[n-1] /a[i] 
You should do this in O(n) time without using division. 

As an example, if A = {1,2,3,4}, B should be (24,12,8,6).
"""

def sol(A):
    n = len(A)
    B = [1] * n
    
    # store left products in B; B[i] = product of all elements before i
    for i in xrange(1,n):
        B[i] = B[i-1]*A[i-1]
        
    x = A[-1]
    if A[-1] == 0:
        B[-1] = None
    
    # traverse right to left and update B[i] to final value
    for i in xrange(n-2,-1,-1):
        if A[i] != 0:
            B[i] *= x
        else:
            B[i] = None
        x *= A[i]
    
    return B

if __name__ == '__main__':
    A = [1,1,2,5,2]
    print (sol(A))