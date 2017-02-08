# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:12:15 2016

@author: arnab
"""
"""
Perform basic string compression
"abcdddddd" -> "a1b1c1d6"
"abcd" -> "abcd"
"""
def compress(s):
    # perform basic string compression
    i, cs = 0, ""
    n = len(s)
    while i < n:
        t, count = s[i], 0
        while i < n and s[i] == t:
            count += 1
            i += 1
        cs += t + str(count)
    if len(cs) < n:
        return cs
    else:
        return s

if __name__ == '__main__':
    s = "abcdddddd"
    print (compress(s))