# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:23:38 2017

@author: arnab
"""

"""
Best meeting point
reference: https://leetcode.com/problems/best-meeting-point/description/
A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone
in the group. The distance is calculated using Manhattan Distance,
where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of
2+2+2=6 is minimal. So return 6.


similar problem: https://www.hackerrank.com/contests/booking-womenintech/challenges/visiting-manhattan/problem

"""

def minTotalDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    r, c = len(grid), len(grid[0])
    landmark_r, landmark_c = [0]*r, [0]*c
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] == 1:
                landmark_r[i] += 1
                landmark_c[j] += 1
    
    costleft_r, costright_r = [0]*r, [0]*r
    count = landmark_r[0]
    for i in xrange(1, r):
        costleft_r[i] = costleft_r[i-1] + count
        count += landmark_r[i]
    count = landmark_r[-1]
    for i in xrange(r-2,-1,-1):
        costright_r[i] = costright_r[i+1] + count
        count += landmark_r[i]

    costleft_c, costright_c = [0]*c, [0]*c
    count = landmark_c[0]
    for i in xrange(1, c):
        costleft_c[i] = costleft_c[i-1] + count
        count += landmark_c[i]
    count = landmark_c[-1]
    for i in xrange(c-2,-1,-1):
        costright_c[i] = costright_c[i+1] + count
        count += landmark_c[i]
    
    dmin = float('inf')
    for i in xrange(r):
        for j in xrange(c):
            d = costleft_r[i] + costright_r[i] + costleft_c[j] + costright_c[j]
            if d < dmin:
                dmin = d
    return dmin