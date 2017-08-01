# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:52:42 2017

@author: arnab
"""

"""
check if s2 is a substring of s1
"""
def findSubString2(s1, s2):
    if s1 is None or s2 is None:
        return None
    
    n1, n2 = len(s1), len(s2)
    if n1 < n2:
        return None
    
    if n2 == 0:
        return s2
    
    for i in xrange(n1-n2+1):
        # check if the substring starting at i of length n2 == s2
        if s1[i:i+n2] == s2:
            return s1[i:i+n2]
    return None


if __name__ == '__main__':
    s1 = "ABCDEF"
    s2 = "ABCDEF"
    print (findSubString2(s1, s2))