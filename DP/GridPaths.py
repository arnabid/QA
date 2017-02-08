# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:53:44 2016

@author: arnab
"""

""" Grid Paths questions """

""" Number of unique paths when all the cells in the grid are open """
def countSimple(m,n):
    """ Optmization: linear memory instead of quadratic memory """
    a = [1] * n
    for i in xrange(1,m):
        for j in xrange(1,n):
            a[j] += a[j-1]
    
    return a[-1]

""" Number of unique paths when some of the cells in the grid are blocked """
def countBlocked(grid):
    m, n = len(grid), len(grid[0])
    
    # base case
    if grid[0][0] == 1:
        return 0
    
    a = [[0 for i in xrange(n)] for i in xrange(m)]
    a[0][0] = 1
    
    # process the first row
    for i in xrange(1,n):
        if grid[0][i] == 0:
            a[0][i] = a[0][i-1]
    
    # process the first column
    for i in xrange(1,m):
        if grid[i][0] == 0:
            a[i][0] = a[i-1][0]

    for i in xrange(1,m):
        for j in xrange(1,n):
            if grid[i][j] == 0:
                a[i][j] = a[i-1][j] + a[i][j-1]

    return a[-1][-1]

def minPathSum(grid):
    """ returns the path from top left to bottom right which minimizes
    the sum of all numbers along its path. """
    m, n = len(grid), len(grid[0])
    
    a = [[0 for i in xrange(n)] for i in xrange(m)]
    a[0][0] = grid[0][0]
    
    # process the first row
    for i in xrange(1,n):
        a[0][i] = a[0][i-1] + grid[0][i]
    
    # process the first column
    for i in xrange(1,m):
        a[i][0] = a[i-1][0] + grid[i][0]
    
    for i in xrange(1,m):
        for j in xrange(1,n):
            a[i][j] = min(a[i-1][j], a[i][j-1]) + grid[i][j]
    
    return a[-1][-1]

def calculateMinimumStart(grid):
    """  Determine the minimum initial value to reach the bottom right corner.
    Value reduces with negative integers upon entering these cells; other rooms are either
    empty (0's) or contain positive integers. The value cannot be 0 at any cell """
    # TODO: Also print the path
    m, n = len(grid), len(grid[0])
    a = [[1 for i in xrange(n)] for i in xrange(m)]
    
    if grid[-1][-1] < 0:
        a[-1][-1] = -grid[-1][-1] + 1
    
    # process the last column
    for i in xrange(m-2,-1,-1):
        if a[i+1][n-1] - grid[i][n-1] > 0:
            a[i][n-1] = a[i+1][n-1] - grid[i][n-1]

    # process the last row
    for i in xrange(n-2,-1,-1):
        if a[m-1][i+1] - grid[m-1][i] > 0:
            a[m-1][i] = a[m-1][i+1] - grid[m-1][i]
    
    for i in xrange(m-2,-1,-1):
        for j in xrange(n-2,-1,-1):
            temp = min(a[i+1][j], a[i][j+1])
            if temp - grid[i][j] > 0:
                a[i][j] = temp - grid[i][j]
    
    return a[0][0]


if __name__ == '__main__':
    grid = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    #print (countSimple(4,5))
    #print (countBlocked(grid))
    #print (minPathSum(grid))
    print (calculateMinimumStart(grid))