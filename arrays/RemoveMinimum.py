# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:49:50 2016

@author: arnab
"""

"""
Remove elements from the ends of an array such that 2*min > max
in the resized array.
Find the minimum number of elements that have to be removed to satisfy the
above condition.
Bonus: Find all possible combinations
reference: http://www.geeksforgeeks.org/remove-minimum-elements-either-side-2min-max/
"""

"""
recursion with memoization
"""
def solRecursion(arr, l, h, table):
    
    if l >= h:
        return 0
    
    if (l,h) in table:
        return table[(l,h)]

    mn = min(arr[l:h+1])
    mx = max(arr[l:h+1])
    
    if 2 * mn > mx:
        table[(l,h)] = 0
        return table[(l,h)]
    
    table[(l,h)] = min(solRecursion(arr,l+1,h), solRecursion(arr,l,h-1)) + 1
    return table[(l,h)]

"""
DP solution
"""
def solDP(arr):
    n = len(arr)
    table = [[0] * n] * n
    
    for gap in xrange(n):
        i = 0
        for j in xrange(gap,n+1):
            mn = min(arr[i:j+1])
            mx = max(arr[i:j+1])
            
            if 2 * mn > mx:
                table[i][j] = 0
            else:
                table[i][j] = min(table[i][j-1], table[i+1][j]) + 1
            i += 1
    return table[0][n-1]
            


def solution(arr):
    n = len(arr)
    longest_start, longest_end = -1, 0
    
    for start in xrange(n):
        mn, mx = float('inf'), -float('inf')
        
        for end in xrange(start,n):
            val = arr[end]
            
            if val < mn:
                mn = val
            if val > mx:
                mx = val
            
            if 2 * mn <= mx:
                break
            
            if end - start > longest_end - longest_start or longest_start == -1:
                longest_start = start
                longest_end = end

    if longest_start == -1:
        return n
    return (n - (longest_end - longest_start + 1))
