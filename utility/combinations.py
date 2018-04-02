# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:08:29 2017

@author: arnab
"""

"""
generate all 2^n combinations
"""
def comb1(s):
    comb1Util("", s)

def comb1Util(prefix, s):
    print (prefix)
    for i in range(len(s)):
        comb1Util(prefix + s[i], s[i+1:])


def comb2(s, k):
    comb2Util("", s, k)

def comb2Util(prefix, s, k):
    if k == 0:
        print (prefix)
        return
    for i in range(len(s)):
        comb2Util(prefix + s[i], s[i+1:], k-1)

if __name__ == '__main__':
    s = "ABC"
    #comb1(s)
    comb2(s, 2)