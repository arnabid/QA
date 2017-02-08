# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:47:19 2016

@author: arnab
"""

"""
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
Find the maximum number of connected cells in a grid
Defn of connected: (i,j) and (x,y) are connected iff 
grid[i][j] = 1, grid[x][y] = 1 and they are neighbors(8 cells)
"""

def solutionDFS(grid, visited, start, rn, cn, r, c):

    def DFS(grid, visited, start, rn, cn, r, c, total):
        visited[start[0]][start[1]] = 1
        total[0] = total[0] + 1
        for k in xrange(8):
            ii = start[0] + rn[k]
            jj = start[1] + cn[k]
            if (ii >= 0 and ii < r) and (jj >= 0 and jj < c) and (grid[ii][jj] == 1) \
            and (visited[ii][jj] != 1):
                DFS(grid, visited, (ii,jj), rn, cn, r, c, total)
    
    
    total = [0]
    DFS(grid, visited, start, rn, cn, r, c, total)
    return total[0]

if __name__ == '__main__':
    r = int(raw_input().strip())
    c = int(raw_input().strip())
    grid = [map(int, raw_input().strip().split(" ")) for i in xrange(r)]
    visited = [[0 for i in xrange(c)] for j in xrange(r)]
    ans = -float('inf')
    rn = [-1,-1,-1,0,0,1,1,1]
    cn = [-1,0,1,1,-1,-1,0,1]
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] == 1 and not visited[i][j]:
                ans = max(ans, solutionDFS(grid, visited, (i,j), rn, cn, r, c))
    print (ans)
