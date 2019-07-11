# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:32:44 2016

@author: arnab
"""

"""
This program checks if 2 input strings are anagrams of each other.
"""

from collections import Counter
def checkAnagram(s1, s2):
	return sorted(s1) == sorted(s2)


def isAnagram(s1, s2):
    d1, d2 = Counter(s1), Counter(s2)
    return d1 == d2

if __name__ == '__main__':
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    print (isAnagram(s1,s2))