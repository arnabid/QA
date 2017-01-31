# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:51:16 2017

@author: arnab
"""

"""
reference: https://www.hackerrank.com/challenges/castle-on-the-grid
"""

from collections import Counter
import Queue

def getNeighbors(grid, n, cell):
    neighbors, (x,y) = [], cell
    #right
    for i in xrange(y+1, n):
        if grid[x][i] == '.':
            neighbors.append((x,i))
        else:
            break
    #left
    for i in xrange(y-1, -1, -1):
        if grid[x][i] == '.':
            neighbors.append((x,i))
        else:
            break
    #down
    for i in xrange(x+1, n):
        if grid[i][y] == '.':
            neighbors.append((i,y))
        else:
            break
    #up
    for i in xrange(x-1, -1, -1):
        if grid[i][y] == '.':
            neighbors.append((i,y))
        else:
            break
    return neighbors


def sol(grid,n,start,end):
    q = Queue.Queue()
    q.put(start)
    dlabel = Counter()
    dlabel[start] = 0
    
    while not q.empty():
        cell = q.get()
        if cell == end:
            return dlabel[cell]
        for node in getNeighbors(grid,n,cell):
            if node not in dlabel:
                q.put(node)
                dlabel[node] = dlabel[cell] + 1


if __name__ == '__main__':
    n = int(raw_input())
    grid = []
    for _ in xrange(n):
        row = raw_input().strip()
        grid.append(row)
    a,b,c,d = map(int, raw_input().strip().split(" "))
    print (sol(grid,n,(a,b),(c,d)))