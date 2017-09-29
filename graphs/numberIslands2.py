# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:08:09 2017

@author: arnab
"""
"""
A 2d grid map of m rows and n columns is initially filled with water.
We may perform an addLand operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

reference: https://leetcode.com/problems/number-of-islands-ii/description/
For each cell in positions, that cell becomes an island and may join other islands
only horizontally and vertically. Find the number of resulting islands after each 
addLand operation.
"""

class UF(object):
    def __init__(self):
        self.id = {} # link to parent
        self.sz = {} # rank of each node
    
    def find(self, p):
        # returns the root of the component in which node p lies
        if not p in self.id:
            self.id[p] = p
            self.sz[p] = 1
            return p
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p
    
    def connected(self, p, q):
        # returns a boolean to indicate if nodes p and q are connected
        proot = self.find(p)
        qroot = self.find(q)
        return proot == qroot, proot, qroot

    def union(self, proot, qroot):
        # do union by rank
        if self.sz[proot] < self.sz[qroot]:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]
        else:
            self.id[qroot] = proot
            self.sz[proot] += self.sz[qroot]

class Solution(object):
    def numIslands2(self, r, c, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf = UF()
        ans, islands = [], 0
        grid = [[0 for i in xrange(c)] for i in xrange(r)]
        
        X = [-1,1,0,0]
        Y = [0,0,-1,1]
        for x,y in positions:
            islands += 1
            grid[x][y] = 1
            for k in xrange(4):
                ii = x + X[k]
                jj = y + Y[k]
                if 0 <= ii < r and 0 <= jj < c and grid[ii][jj] == 1:
                    connected, uroot, vroot = uf.connected((ii,jj), (x,y))
                    if not connected:
                        uf.union(uroot, vroot)
                        islands -= 1
            ans.append(islands)
        return ans

if __name__ == '__main__':
    r,c = 3,3
    positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
    s = Solution()
    print s.numIslands2(r,c,positions)