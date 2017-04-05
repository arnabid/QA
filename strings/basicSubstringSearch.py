# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:52:42 2017

@author: arnab
"""
def findSubString(s1, s2):
    if s1 is None or s2 is None:
        return None
    
    n1, n2 = len(s1), len(s2)
    if n1 < n2:
        return None
    
    if n2 == 0:
        return s1
    
    for i in xrange(n1-n2+1):
        if s1[i] == s2[0]:
            j = 0
            while j < n2:
                if s1[i+j] != s2[j]:
                    break
                j += 1
            if j == n2:
                return s1[i:i+j]
    return None

if __name__ == '__main__':
    s1 = "ABCDEF"
    s2 = "BC"
    print (findSubString(s1, s2))