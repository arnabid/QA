# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:24:27 2016

@author: arnab
"""

"""
Beautiful binary string
https://www.hackerrank.com/challenges/beautiful-binary-string
"""

if __name__ == '__main__':
    n = int(raw_input().strip())
    s = raw_input().strip()
    
    modified_s = s.replace("010", "")
    ans = (len(s) - len(modified_s))/3
    print (ans)
