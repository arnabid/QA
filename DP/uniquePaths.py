# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:24:36 2017

@author: arnab
"""

"""
reference: https://leetcode.com/problems/unique-paths-ii/
"""

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # base case
    if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
        return 0
    
    obstacleGrid[0][0] = 1

    # process the first row
    for i in xrange(1,n):
        if obstacleGrid[0][i-1] - obstacleGrid[0][i] > 0:
            obstacleGrid[0][i] = 1
        else:
            obstacleGrid[0][i] = 0

    # process the first column
    for i in xrange(1,m):
        if obstacleGrid[i-1][0] - obstacleGrid[i][0] > 0:
            obstacleGrid[i][0] = 1
        else:
            obstacleGrid[i][0] = 0

    for i in xrange(1,m):
        for j in xrange(1,n):
            obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1-obstacleGrid[i][j])

    return obstacleGrid[-1][-1]
        