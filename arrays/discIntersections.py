# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:06:48 2017

@author: arnab
"""

"""
Problem statement: https://codility.com/programmers/challenges/beta2010/
reference: http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-
challenge-number-of-disc-intersections/
"""
def intersections(arr):
    n = len(arr)
    events = []
    for i in xrange(n):
        events += [(i-arr[i],-1), (i+arr[i],1)]
    
    events.sort(key = lambda x: (x[0], x[1]))
    activeCircles, result = 0, 0
    for event in events:
        if event[1] == -1:
            result += activeCircles
            activeCircles += 1
        else:
            activeCircles -= 1
    return result
            

if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(","))
    
    print (intersections(arr))