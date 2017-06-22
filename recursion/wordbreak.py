# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:33:54 2017

@author: arnab
"""
"""
work break
reference: http://www.geeksforgeeks.org/word-break-problem-using-backtracking/
"""

dictionary = set(["man","mango", "icecream","and","go","i","love","ice","cream", "iloveicecreamandmango"])

def wordbreak(s):
    wordbreakUtil(s, len(s), "")

def wordbreakUtil(s, n, result):
    for i in xrange(1,n+1):
        prefix = s[0:i]
        
        if prefix in dictionary:
            if i == n:
                print result + prefix
                return
            wordbreakUtil(s[i:n], n-i, result + prefix + " ")

if __name__ == '__main__':
    s = "iloveicecreamandmango"
    wordbreak(s)