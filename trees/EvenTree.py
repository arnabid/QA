# -*- coding: utf-8 -*-
"""
Created on Sun May 29 08:45:48 2016

@author: arnab
"""
""" 
Problem: https://www.hackerrank.com/challenges/even-tree
To get a forest such that each connected component of the forest contains
an even number of nodes requires that the toal number of nodes 'N' in the tree
has to be an even number. A solution exists only if N is even.
So the question reduces to finding the number of subtrees(except at the root node)
that have even number of nodes.
"""

from collections import defaultdict
from collections import Counter

class EvenTreeSolution():
    def __init__(self, graph):
        self.visited = set()
        self.graph = graph
        self.countlabel = Counter()
        self.snipEdges = 0
    
    def dfs(self, v):
        self.visited.add(v)
        for w in self.graph[v]:
            if w not in self.visited:
                self.edgeTo[w] = v
                self.countlabel[v] += self.dfs(w)
        self.countlabel[v] += 1
        # count the number of subtrees that have even number of nodes
        if self.countlabel % 2 == 0:
            self.snipEdges += 1
        return self.countlabel[v]

    def evenTreeSolution(self):
        # pick node 1 as the root and start a dfs
        self.dfs('1')
        
        # return the number of subtrees with even nodes except the main tree
        return self.snipEdges - 1

if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    graph = defaultdict(set)
    for _ in range(m):
        u, v = input().strip().split(" ")
        graph[u].add(v)
        graph[v].add(u)
    print (EvenTreeSolution(graph).evenTreeSolution())
