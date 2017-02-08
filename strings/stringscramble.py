# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:51:21 2016

@author: arnab
"""

""" Check if one string is a scrambled version of the other """
def solution(s1,s2):
    
    # build a (key, count) map
    mp = {}
    for c in s1:
        if c in mp:
            mp[c] += 1
        else:
            mp[c] = 1
    
    for c in s2:
        if c in mp:
            mp[c] -= 1
            if mp[c] == 0:
                del mp[c]
        else:
            return False
    
    if len(mp) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s1 = "ABCDE"
    s2 = "CBADEA"
    print (solution(s1,s2))
