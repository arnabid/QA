# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 09:32:04 2017

@author: arnab
"""

"""
print permutations of a string
http://introcs.cs.princeton.edu/java/23recursion/Permutations.java.html
"""

def perm1(s):
    perm1UT("", s)

def perm1UT(prefix, s):
    n = len(s)
    if n == 0:
        print (prefix)
    for i in xrange(n):
        perm1UT(prefix + s[i], s[:i] + s[i+1:])

def perm2(s, k):
    perm2UT("", s, k)

def perm2UT(prefix, s, k):
    if k == 0:
        print (prefix)
        return
    for i in xrange(len(s)):
        perm2UT(prefix + s[i], s[:i] + s[i+1:], k-1)

if __name__ == '__main__':
    s = "ABC"
    perm1(s)
    
    k = 2
    perm2(s, 2)
