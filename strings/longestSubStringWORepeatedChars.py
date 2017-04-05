# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:39:16 2016

@author: arnab
"""

"""
find the longest substring with non-repeating characters
addition: find all the substrings with non-repeated chars
"""
from collections import Counter

def allUnique(s, start, end):
    u = set()
    for ch in s[start:end]:
        if ch in u:
            return False
        u.add(ch)
    return True

def bruteForcesol(s):
    ans = 0
    n = len(s)
    
    for i in xrange(n):
        for j in xrange(i+1,n+1):
            if allUnique(s, i, j):
                ans = max(ans, j-i)
    return ans


def solVER2(s):
    c = Counter()
    n, i = len(s), 0
    ans = 0
    for j in xrange(n):
        if s[j] in c:
            i = c[s[j]] + 1
        ans = max(ans, j-i+1)
        c[s[j]] = j
    return ans


def solVER1(s):
    n = len(s)
    u = set()
    i, j = 0, 0
    ans = 0
    for i in xrange(n):
        while j < n and s[j] not in u:
            u.add(s[j])
            j += 1
        ans = max(ans, j-i)
        u.remove(s[i])
    return ans
    

def findsol(s):
    n = len(s)
    front, c = 0, Counter()
    maxlen, res = 0, ''
    allStrings = []
    
    for back in xrange(n):
        while front < n and s[front] not in c:
            if back < front:
                allStrings.append(s[back:front])
            c[s[front]] = 1
            front += 1
        if back < front:
            allStrings.append(s[back:front])
        if front - back > maxlen:
            maxlen = front - back
            res = s[back:front]
        del c[s[back]]
    
    print (allStrings)
    return res, maxlen
    
            

if __name__ == '__main__':
    s = raw_input().strip()
    
    #print (solVER1(s))
    print (solVER2(s))