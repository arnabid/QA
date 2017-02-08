# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:29:00 2016

@author: arnab
"""

"""
https://www.hackerrank.com/challenges/alternating-characters
"""
if __name__ == '__main__':   
    n = int(raw_input().strip())
    for _ in xrange(n):
        s = raw_input().strip()
        size = len(s)
        count = 0
        for i in xrange(1,size):
            if s[i] == s[i-1]:
                count += 1
        print (count)