# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:21:45 2017

@author: arnab
"""

"""
maximun contiguous sub array
reference: http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""

def maxsubarray(arr):
    n = len(arr)
    mx_end_here, mx_sofar = 0, -float('inf')
    start, end, s = 0,0,0
    for i in xrange(n):
        mx_end_here += arr[i]
        if mx_end_here > mx_sofar:
            mx_sofar = mx_end_here
            start = s
            end = i
        if mx_end_here < 0:
            mx_end_here = 0
            s = i + 1
    print mx_sofar, start, end
    
    
if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(" "))
    maxsubarray(arr)