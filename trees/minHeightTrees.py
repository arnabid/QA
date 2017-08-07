# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 08:11:03 2017

@author: arnab
"""

"""
Minimum height trees
reference: https://leetcode.com/problems/minimum-height-trees/description/

Notes:
There can be only 1 or 2 nodes with minimum height trees.

These nodes are the critical nodes in the sense that maximum cost needed to
reach the farthest node in the network will be minimum. Any sort of message propagation
will be most efficient from these node(s).
"""

from collections import Counter
import Queue

def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n <= 2:
        return list(xrange(n))
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

    while n > 2:
        # prune the batch of leaves
        for i in xrange(q.qsize()):
            v = q.get()
            n -= 1
            for w in graph.get(v, []):
                degree[w] -= 1
                if degree[w] == 1:
                    q.put(w)
    res = []
    while not q.empty():
        res.append(q.get())
    return res
