# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:57:36 2016

@author: arnab
"""
from collections import Counter

if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input().strip()
    
    notvalid, c = set(), Counter()
    c[s[0]] = 1
    for i in xrange(1,n):
        c[s[i]] += 1
        if s[i] == s[i-1]:
            notvalid.add(s[i])
    
    print (c)
    print (notvalid)
    for ch in notvalid:
        del c[ch]
    print (c)
    
    if len(c) < 2:
        print (0)

    ans = 0
    for item in c.most_common(2):
        ans += item[1]
    print (ans)
    print (c.most_common(2))
     