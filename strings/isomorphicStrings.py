# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 08:07:32 2017

@author: arnab
"""

"""
check if 2 strings are isomorphic
"""

def isIsomorphic(s, t):
    l1, l2 = len(s), len(t)
    
    if l1 != l2:
        return False

    map1, map2 = {}, {}
    for i in xrange(l1):
        # same char in s mapping to different chars in t
        if s[i] in map1 and map1[s[i]] != t[i]:
            return False
        # different chars in s mapping to same char in t
        if s[i] not in map1 and t[i] in map2:
            return False
        map1[s[i]] = t[i]
        map2[t[i]] = s[i]
    return True

if __name__ == '__main__':
    s = "paper"
    t = "title"
    print (isIsomorphic(s, t))
    