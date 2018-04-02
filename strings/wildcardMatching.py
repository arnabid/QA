# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 07:35:35 2017

@author: arnab
"""

"""
wildcard pattern matching
refernce: http://www.geeksforgeeks.org/wildcard-pattern-matching/
"""

def isMatch(s, pattern):
    n, m = len(s), len(pattern)
    
    # empty pattern can only match empty string
    if m == 0:
        return n == 0
    
    """
    table[i][j] = True if first i chars in string match first j chars in pattern
    """
    
    table = [[False for j in xrange(m+1)] for i in xrange(n+1)]
    
    table[0][0] = True
    
    # Fill first column
    for i in xrange(1, n+1):
        table[i][0] = False
    
    # Fill first row
    for j in xrange(1, m+1):
        if pattern[j-1] == '*':
            table[0][j] = table[0][j-1]
    
    for i in xrange(1, n+1):
        for j in xrange(1, m+1):
            if pattern[j-1] == s[i-1] or pattern[j-1] == '?':
                table[i][j] = table[i-1][j-1]
            elif pattern[j-1] == '*':
                table[i][j] == table[i-1][j] or table[i][j-1]
            else:
                table[i][j] = False
    return table[n][m]