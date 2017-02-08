# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:48:35 2016

@author: arnab
"""
def isOK(n, cnt):
    for i in xrange(4):
        if cnt[i] > n /4:
            return False
    return True

def solution(s):
    n = len(s)
    if n % 4 != 0:
        raise ValueError("input string length is not valid")

    mydict = {'A':0, 'C':1, 'T':2, 'G':3}
    cnt = [0]*4
    
    for i in xrange(n):
        if s[i] in mydict:
            cnt[mydict[s[i]]] += 1
        else:
            raise ValueError("Inavlid letter in input string")

    if isOK(n, cnt):
        return 0
    
    ans = n
    j = 0
    for i in xrange(n):
        while j < n and not isOK(n, cnt):
            cnt[mydict[s[j]]] -= 1
            j += 1
        if isOK(n, cnt):
            ans = min(ans, j-i)
        cnt[mydict[s[i]]] += 1
    return ans

if __name__ == '__main__':
    inp_string = raw_input().strip()
    ans = solution(inp_string)
    print (ans)