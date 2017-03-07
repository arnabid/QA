# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:03:42 2017

@author: arnab
"""

"""
permutations of size k
P(n,k) = n!/(n-k)!
"""

def permuteK(arr, n, k):
    if k == 0:
        print (''.join(arr[n:]))
    else:
        for i in xrange(n):
            arr[n-1], arr[i] = arr[i], arr[n-1]
            permuteK(arr, n-1, k-1)
            arr[n-1], arr[i] = arr[i], arr[n-1]


if __name__ == '__main__':
    s = "ABCDA"
    arr = list(s)
    k = 2
    n = len(s)
    
    permuteK(arr, n, k)
    