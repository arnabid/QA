# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:39:06 2016

@author: arnab
"""
def sol(s, n, k):
    s = list(s)
    changed = [0] * n
    
    for i in xrange(0, n//2):
        if k > 0:
            if s[i] < s[n-1-i]:
                s[i] = s[n-1-i]
                k -= 1
                changed[i] = 1
            elif s[i] > s[n-1-i]:
                s[n-1-i] = s[i]
                k -= 1
                changed[n-1-i] = 1
        else:
            if s[i] != s[n-1-i]:
                return -1
    
    for i in xrange(0, n//2):
        if k > 0:
            if (changed[i] or changed[n-1-i]) and s[i] != '9':
                s[i], s[n-1-i] = '9', '9'
                k -= 1
            elif k >= 2 and changed[i] == 0 and changed[n-1-i] == 0 and s[i] != '9':
                s[i], s[n-1-i] = '9', '9'
                k -= 2

    if n%2 and k > 0:
        s[n//2] = '9'
    return ("".join(s))

if __name__ == '__main__':
    n, k = map(int, raw_input().strip().split(" "))
    s = raw_input().strip()
    
    print (sol(s, n, k))

            
        
        