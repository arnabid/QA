# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 07:55:16 2016

@author: arnab
"""

"""
replace all occurences of given substring
in a string with '#'
"""

if __name__ == '__main__':
    s = raw_input().strip()
    ss = raw_input().strip()
    output = ""
    
    n, k = len(s), len(ss)
    i = 0
    while i < (n-k+1):
        if s[i] == ss[0]:
            flag = True
            for j in xrange(k):
                if ss[j] != s[i+j]:
                    flag = False
                    break
            if flag:
                for j in xrange(k):
                    output += "#"
                i += k
            else:
                output += s[i]
                i += 1
        else:
            output += s[i]
            i += 1
    
    while i < n:
        output += s[i]
        i += 1
    
    print (output)

                