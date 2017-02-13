# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:04:49 2017

@author: arnab
"""

"""
reference: http://www.ideserve.co.in/learn/find-median-of-two-sorted-arrays
"""

def Median(arr, start, end):
    indexdiff = end - start
    if indexdiff % 2 == 0:
        return arr[start + indexdiff/2]
    else:
        index = start + indexdiff/2
        return (arr[index] + arr[index+1])/2.0

def findMedianFast(A, B, sa, ea, sb, eb):
    """ returns the median of 2 sorted arrays A and B of size n w/o merge step"""
    if (ea-sa) == 0 and (eb-sb) == 0:
        return (A[0] + B[0])/2.0
    
    if (ea-sa) == 1 and (eb-sb) == 1:
        return (max(A[sa],B[sb]) + min(A[ea],B[eb]))/2.0
    
    m1 = Median(A, sa, ea)
    m2 = Median(B, sb, eb)
    
    if m1 == m2:
        return m1
    elif m1 < m2:
        if (ea-sa) % 2 == 0:
            eb = sb + (eb-sb)/2
        else:
            eb = sb + (eb-sb)/2 + 1
        sa = sa + (ea-sa)/2
    else:
        if (eb-sb) % 2 == 0:
            ea = sa + (ea-sa)/2
        else:
            ea = sa + (ea-sa)/2 + 1
        sb = sb + (eb-sb)/2
    return findMedianFast(A, B, sa, ea, sb, eb)

def findMedian(A, B):
    """ returns the median of 2 sorted arrays A and B of size n by using merge step"""
    n = len(A)
    
    i, j, tmp= 0, 0, 0
    first, second = 0, 0
    while i < n and j < n:
        if A[i] <= B[j]:
            tmp = A[i]
            i += 1
        else:
            tmp = B[j]
            j += 1
        if i + j == n:
            first = tmp
        if i + j == n+1:
            second = tmp
            break
    
    if i == 0:
        second = A[0]
    
    if j == 0:
        second = B[0]
    
    print first, second
    return (first + second)/2.0

if __name__ == '__main__':
    A = [1,3,5,6]
    B = [2,2,2,3]
    
    print findMedianFast(A, B, 0, 3, 0, 3)
    
        