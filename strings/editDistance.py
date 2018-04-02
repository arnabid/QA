# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 08:12:11 2017

@author: arnab
"""

"""
check if 2 strings s, t are one edit distance apart
edits: insert, remove, replace
"""
def isOneEdit(s, t):
    m, n = len(s), len(t)
    if abs(m - n) > 1:
        return False
    
    for i in xrange(min(m,n)):
        if s[i] != t[i]:
            if m == n:
                return s[i+1:] == t[i+1:]
            elif m > n:
                return s[i+1:] == t[i:]
            else:
                return s[i] == t[i+1:]
    return m != n


"""
find the minimum edit distance between s and t
reference: http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
"""
def editDistDP(str1, str2):
    m, n = len(str1), len(str2)
    
    if m == 0:
        return n
    
    if n == 0:
        return m

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    
    # fill first row
    for i in xrange(n+1):
        dp[0][i] = i
    
    # fill first column
    for i in xrange(m+1):
        dp[i][0] = i
 
    # Fill d[][] in bottom up manner
    for i in range(1, m+1):
        for j in range(1, n+1):
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])      # Replace
 
    return dp[m][n]
