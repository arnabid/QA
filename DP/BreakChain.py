# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:50:18 2016

@author: arnab
"""

""" Break the chain using DP """

def solution(ml):
    n = len(ml)
    
    if n < 5:
        return -1
    
    if n == 5:
        return ml[1] + ml[3]
    
    a = [(ml[1],ml[3])]
    temp = [(ml[1],ml[3]), (ml[1],ml[4]), (ml[2],ml[4])]
    temp.sort(key = lambda x: x[0] + x[1])
    a.append(temp[0])
    
    t = 2
    for i in xrange(5,n-1):
        temp = [a[t-1], (ml[i],a[t-2][0]), (ml[i],a[t-2][1])]
        temp.sort(key = lambda x: x[0] + x[1])
        a.append(temp[0])
        t += 1
    
    return a[-1][0] + a[-1][1]

if __name__ == '__main__':
    ml = [9,1,8,1,5,7,1,10]
    ans = solution(ml)
    print (ans)