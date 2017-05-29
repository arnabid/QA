# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:33:14 2017

@author: arnab
"""

"""
find the number of islands in the grid
0 - water
1 - land
"""
import Queue

X = [-1,1,0,0]
Y = [0,0,-1,1]

"""
reference: https://discuss.leetcode.com/topic/16749/7-lines-python-14-lines-java
"""
def countIslands(grid):
    def sink(i,j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = 0
            map(sink, (i-1, i+1, i, i), (j, j, j-1, j+1))
            return 1
        return 0
    return sum(sink(i,j) for i in xrange(len(grid)) for j in xrange(len(grid[i])))

def solDFS(grid):
    r, c = len(grid), len(grid[0])
    islands = 0
    visited = set()
    
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] == 1 and (i,j) not in visited:
                # start a DFS traversal from (i,j)
                islands += 1
                stack = [(i,j)]
                visited.add((i,j))
                
                while stack:
                    ii, jj = stack.pop()
                    for k in xrange(4):
                        x = ii + X[k]
                        y = jj + Y[k]
                        if x >= 0 and x < r and y >= 0 and y < c and \
                        grid[x][y] == 1 and (x,y) not in visited:
                            stack.append((x,y))
                            visited.add((x,y))
    return islands

def solBFS(grid):
    r, c = len(grid), len(grid[0])
    islands = 0
    visited = set()
    
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] == 1 and (i,j) not in visited:
                # start a BFS traversal from (i,j)
                islands += 1
                q = Queue.Queue()
                q.put((i,j))
                visited.add((i,j))
                
                while not q.empty():
                    ii, jj = q.get()
                    for k in xrange(4):
                        x = ii + X[k]
                        y = jj + Y[k]
                        if 0 <= x < r and 0 <= y < c and \
                        grid[x][y] == 1 and (x,y) not in visited:
                            q.put((x,y))
                            visited.add((x,y))
    return islands

if __name__ == '__main__':
    grid = [[1,0,1,0], [1,1,1,0], [1,0,0,1]]
    print (solDFS(grid)) # using DFS
    print (solBFS(grid)) # using BFS
    print (countIslands(grid))