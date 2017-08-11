# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:16:05 2017

@author: arnab
"""

"""
Diameter of a general tree
diameter = length of the longest path between any 2 nodes in the tree

Why does the longest path between any 2 nodes in the tree pass through the 
min height node?

consider the tree rooted at the min height node. The longest path possible is
<= 2*h, h = height of tree. All other paths that do not pass through the min height
node are strictly less than the longest path through the min node. Therefore the longest
path which is <= 2*h will pass through the min height node.
"""

from collections import Counter
import Queue

def findDiameterTree(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n <= 2:
        return n-1
    degree = Counter()
    graph = Counter()
    # build the graph and the degree map
    for u,v in edges:
        degree[u] += 1
        degree[v] += 1
        graph[u] = graph.get(u,[])+[v]
        graph[v] = graph.get(v,[])+[u]
    
    # put the leaves in the queue
    q = Queue.Queue()
    for node in graph.keys():
        if degree[node] == 1:
            q.put(node)
    
    diameter = 0
    while n > 2:
        diameter += 1
        # prune the current batch of leaves
        for i in xrange(q.qsize()):
            v = q.get()
            n -= 1
            for w in graph.get(v, []):
                degree[w] -= 1
                if degree[w] == 1:
                    q.put(w)
    diameter *= 2
    if n == 2:
        return diameter + 1
    return diameter