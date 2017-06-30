# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 08:21:20 2017

@author: arnab
"""
from collections import Counter
import Queue

"""
cycle detection in undirected graph
"""

"""
using BFS
"""

def findPath(x, y, edgeTo):
    # returns the path from x -> y
    path = []
    while x != y:
        path.append(x)
        x = edgeTo[x]
    path.append(y)
    return path[::-1]

def findCycle(x, y, start, edgeTo):
    """
    returns the cycle as a simple path
    list[int]
    """
    path_start_x = findPath(x, start, edgeTo) # path from start to x
    path_start_y = findPath(y, start, edgeTo) # path from start to y
    
    # find index of common ancestor
    i, j = 0, 0
    while i < len(path_start_x) and j < len(path_start_y) and \
    path_start_x[i] == path_start_y[j]:
        i += 1
        j += 1
    
    # cycle = [common ancestor to x] + [y to common ancestor]
    return path_start_x[i-1:] + path_start_y[j-1:][::-1]

"""
assumptions:
graph is connected
there are no parallel edges between any 2 nodes in the graph
"""
def findCycleBFS(graph):
    """
    returns True, list[int] if cycle exists
    return False, [] if cycle does not exist
    """
    label, edgeTo = Counter(), Counter()
    start = graph.keys()[0]    # starting vertex of BFS tree
    label[start] = 0
    edgeTo[start] = start
    
    q = Queue.Queue()
    q.put(start)
    
    cycleExists = False
    v, w = None, None
    while not q.empty():
        v = q.get()
        for w in graph.get(v, []):
            if w in label:
                # edge to node at same level
                if label[w] == label[v]:
                    cycleExists = True
                    break
                # edge to predecessor that is not a parent
                elif label[w] < label[v] and edgeTo[v] != w:
                    cycleExists = True
                    break
                # parallel edges; will be represented as duplicate
                # entries in the adjacency list
                elif edgeTo[w] == v:
                    cycleExists = True
                    break
            else:
                label[w] = label[v] + 1
                edgeTo[w] = v
                q.put(w)
    if cycleExists:
        return True, findCycle(v, w, start, edgeTo)
    return False, []

if __name__ == '__main__':
    graph = Counter()
    graph[1] = [2]
    graph[2] = [3,1,4]
    graph[3] = [4,2]
    graph[4] = [3,2]
    
    print (findCycleBFS(graph))
