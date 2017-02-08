# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:17:24 2016

@author: arnab
"""

def solution(ml):
    res = ml[-1]
    
    for item in ml[-2::-1]:
        for i in xrange(len(item)):
            res[i] = item[i] + min(res[i], res[i+1])
    
    return res[0]

if __name__ == '__main__':
    ml = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print (solution(ml))