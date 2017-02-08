# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:32:44 2016

@author: arnab
"""

"""
This program checks if 2 input strings are anagrams of each other.
"""

from collections import Counter
def isAnagram(s1,s2):
    # returns True if 2 input strings are anagrams
#    n = len(s1)
#    if n != len(s2):
#        return False
    d1, d2 = Counter(s1), Counter(s2)
    return d1 == d2
#    if len(d1) != len(d2):  # check number of keys
#        return False
#    for item in d1:
#        if item not in d2: # check same keys
#            return False
#        elif d1[item] != d2[item]: # check value of each key
#            return False
#    return True

if __name__ == '__main__':
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    print (isAnagram(s1,s2))