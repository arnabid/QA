# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:47:15 2016

@author: arnab
"""

"""
Find the largest palindromic substring in a given string
"""

def findPalindrome(s, beg, end, n):
    while (beg >= 0 and end < n) and s[beg] == s[end]:
        beg -= 1
        end += 1
    return s[beg+1:end]

def solution(s):
    """
    for each i as center, exapnd left and right as much as possible
    for each i and i+1 as center, expand left and right as much as possible
    """
    n = len(s)
    maxlen, result = 1, ''
    for i in xrange(n):
        temp = findPalindrome(s, i, i, n)
        if len(temp) > maxlen:
            maxlen = len(temp)
            result = temp
        
        temp = findPalindrome(s, i, i+1, n)
        if len(temp) > maxlen:
            maxlen = len(temp)
            result = temp
    return (result)


def DPSolution(s):
    n = len(s)
    arr = [[0 for _ in xrange(n)] for _ in xrange(n)]
    
    """
    a[i][j] = 1 if substring(i,j) is a palindrome; i and j inclusive
    a[i][j] = 1 if s[i] == s[j] and a[i+1][j-1] = 1
    """
    
    for i in xrange(n):
        arr[i][i] = 1
    
    """
    fill the top half of arr diagonally from NW -> SE direction
    """
    maxlen, result = 1, ''
    for l in xrange(1,n):
        i,j = 0,l
        while i < n and j < n:
            if s[i] == s[j] and (j-i <=2 or arr[i+1][j-1]):
                arr[i][j] = 1
                if maxlen < j-i+1:
                    maxlen = j-i+1
                    result = s[i:j+1]
            i += 1 
            j += 1
    return (result)
    

if __name__ == '__main__':
    s = raw_input().strip()
    #print (s)
    
    print (solution(s))
    
