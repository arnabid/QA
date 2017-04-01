# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 08:05:35 2017

@author: arnab
"""

"""
min_seen[i][j] = min elevation seen in the best path to (i,j)
"""
def sol(heights):
    nr, nc = len(heights), len(heights[0])
    
    min_seen = [[0 for i in xrange(nc)] for j in xrange(nr)]
    
    # initialize the first column of min_seen
    for i in xrange(nr):
        print (heights[i][0])
        min_seen[i][0] = heights[i][0]
    
    print (min_seen)
    
    for j in xrange(1,nc):
        for i in xrange(nr):
            min_seen[i][j] = min_seen[i][j-1]
            if i-i >= 0 and i-1 < nr:
                min_seen[i][j] = max(min_seen[i][j], min_seen[i-1][j-1])
            if i+i >= 0 and i+1 < nr:
                min_seen[i][j] = max(min_seen[i][j], min_seen[i+1][j-1])
            
            if heights[i][j] < min_seen[i][j]:
                min_seen[i][j] = heights[i][j]
    
    res = min_seen[0][-1]
    for i in xrange(1, nr):
        res = max(res, min_seen[i][-1])
    
    print (min_seen)
    return res

if __name__ == '__main__':
    heights = [[3,4,5],
               [2,1,2],
               [1,2,1]]
    print (sol(heights))
