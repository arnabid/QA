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

These nodes are the critical nodes in the sense that maximum distance and total distance to
reach the a node(or all nodes) in the network will be minimum. Any sort of message propagation
will be most efficient from these node(s).
"""

from collections import Counter
import Queue

def findMinHeightTrees(graph):
	n = len(graph)
    degree = Counter()
    q = Queue.Queue()
    # build the degree map and put the leaves in the queue
    for node in graph:
        degree[node] = len(graph(node))
        if degree[node] == 1:
        	q.put(node)

    while n > 2:
        # prune the batch of leaves present in the queue
        for i in range(q.qsize()):
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
