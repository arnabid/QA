# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 08:04:57 2017

@author: arnab
"""

import Queue
from collections import Counter

"""
Topological sorting using BFS

1.Count in-degree of all vertices.
2.Pick any vertex 'v' which has in-degree of 0. 
3.Print 'v'. Remove the vertex 'v' and all edges coming out of it.
  Decrement in-degrees of all neighbors of vertex 'v' by 1.
4.Repeat steps 2 and 3 till all vertices are removed.
"""


def tpSortBFS(graph):
    # find the in-degree of all nodes
    inDeg = Counter()
    for u in graph.keys():
        for v in graph.get(u, []):
            inDeg[v] += 1
    
    # put the nodes with in-degree = 0 in queue
    q = Queue.Queue()
    for u in graph.keys():
        if u not in inDeg:
            q.put(u)

    res = []
    while not q.empty():
        u = q.get()
        res.append(u)
        for v in graph.get(u, []):
            inDeg[v] -= 1
            if inDeg[v] == 0:
                q.put(v)
    return res



"""
topological sort DFS
"""
def tpSortDFSUtil(x, graph, visited, stack):
    visited.add(x)
    for w in graph.get(x, []):
        if w not in visited:
            tpSortDFSUtil(w, graph, visited, stack)
    stack.append(x)


def tpSortDFS(graph):
    """
    return a list of nodes in a valid order
    """
    visited = set()
    stack = []
    for node in graph.keys():
        if node not in visited:
            tpSortDFSUtil(node, graph, visited, stack)
    stack.reverse()
    return stack


if __name__ == '__main__':
    graph = Counter()
    graph['a'] = ['b']
    graph['b'] = ['c']
    graph['d'] = ['b', 'e', 'f']
    graph['e'] = ['g']
    graph['f'] = ['g']
    
    print (tpSortDFS(graph))
    print (tpSortBFS(graph))