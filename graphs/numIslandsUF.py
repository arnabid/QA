# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:22:20 2017

@author: arnab
"""

"""
reference: https://leetcode.com/problems/number-of-islands/#/description
"""

from collections import Counter

class UF(object):
    def __init__(self, sites):
        self.id = {} # link to parent
        self.sz = {} # rank of each node
        self.count = len(sites) # number of components

        #initialize the id and sz arrays
        for i in sites:
            self.id[i] = i
            self.sz[i] = 1

    def find(self, p):
        # returns the root of the component in which node p lies
        if not p in self.id:
            raise Exception("Node %s not present" % str(p))
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        # joins the 2 components in which nodes p and q lie
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot: # do nothing
            return
        # do union by rank
        if self.sz[proot] < self.sz[qroot]:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]
        else:
            self.id[qroot] = proot
            self.sz[proot] += self.sz[qroot]
        self.count -= 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        graph = Counter()
        r, c = len(grid), len(grid[0])
        for i in xrange(r):
            for j in xrange(c):
                if grid[i][j] == 1:
                    index = c*i + j
                    graph[index] = []
                    if j + 1 < c and grid[i][j+1] == 1:
                        graph[index].append(index + 1)
                    if i + 1 < r and grid[i+1][j] == 1:
                        graph[index].append(index + c)

        uf = UF(graph.keys())
        for cell in graph.keys():
            for neighbor in graph[cell]:
                uf.union(cell, neighbor)
        
        return uf.count
