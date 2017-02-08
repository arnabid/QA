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
    
    print (findsol(s))