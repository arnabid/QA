# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:47:25 2016

@author: Arnab
"""

""" Codility - ShortestKnightPath
Time complexity: O(M*N)
Space complexity: O(M*N)

Find the minimum number of moves in which a knight can travel from 
the top left corner to the bottom right corner of a grid.
The knight can make a valid move on the grid given the ending position
on the grid is not blocked (i.e has value 1)

If the destination is not reachable, return -1

"""

import Queue

""" Bonus addition - also print the shortest path """
def printShortestPath(edgeTo, start, end):
    path = []
    while end != start:
        path.append(end)
        end = edgeTo[end]
    path.append(start)
    path.reverse()
    print ("The shortest path is: " + "->".join(str(node) for node in path))

def solution(grid):
    
    r, c = len(grid), len(grid[0])
    start, end = (0, 0), (r-1, c-1)
    
    # base case
    if grid[start[0]][start[1]] or grid[end[0]][end[1]] :
        return -1
    
    label, edgeTo = {}, {}
                
    q = Queue.Queue()
    q.put(start)
    label[start] = 0
    
    X = [-2,-1,1,2,2,1,-1,-2]
    Y = [1,2,2,1,-1,-2,-2,-1]
    
    while not q.empty():
        (i,j) = q.get()

        if (i,j) == end:
            printShortestPath(edgeTo, start, end) # print the shortest path
            return label[(i,j)]
        
        for k in xrange(8):
            ii = i + X[k]
            jj = j + Y[k]
            
            if ii >= 0 and ii < r and jj >= 0 and jj < c \
            and grid[ii][jj] == 0 and (ii,jj) not in label:
                q.put((ii,jj))
                label[(ii,jj)] = label[(i,j)] + 1
                edgeTo[(ii,jj)] = (i,j)
    
    return -1
    
if __name__ == '__main__':
    grid = [[0,0,0],[0,1,1],[1,0,0]]
    steps = solution(grid)
    print ("The shortest path has {} steps".format(steps))
    