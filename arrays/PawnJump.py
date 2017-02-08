# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:47:30 2016

@author: arnab
"""

""" Codility - Pawn jump """

def solution(ml):
    
    n = len(ml)
    dest, steps = 0,0
    visited = {}
    visited[0] = True
    
    while True:
        dest += ml[dest]
        steps += 1
        
        if dest >= n or dest < 0:
            return steps
        
        if not visited.get(dest, False):
            visited[dest] = True
        else:
            return -1

    
if __name__ == '__main__':
    ml = [1,1,2,1,-5]
    result = solution(ml)
    print ("The answer is %d" %result)