# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 21:23:04 2016

@author: arnab
"""

"""
A directed graph has 4 types of edges:
tree, forward, back and cross edges
The presence of a back edge implies a cycle
"""

from collections import Counter
visited, edgeTo, onStack = {}, {}, {}
cycles = []
cycleExists = False

def addCycle(start, end):
    global cycleExists
    cycleExists = True
    cycleFound = []
    temp = start
    while temp != end:
        cycleFound.append(temp)
        temp = edgeTo[temp]
    cycleFound.extend([end,start])
    cycles.append(cycleFound[::-1])

def detectCycle(graph):
    nodes = graph.keys()
    
    for node in nodes:
        if not visited.get(node, False):
            DFS(node)

def DFS(v):
    visited[v] = True
    onStack[v] = True
    for w in graph.get(v, []):
        if not visited.get(w, False):
            edgeTo[w] = v
            DFS(w)
        elif onStack[w]:
            addCycle(v,w)
    onStack[v] = False
        

if __name__ == '__main__':
    # n - vertices, m - edges
    n, m = map(int, raw_input().strip().split(" "))
    graph = Counter()
    
    for _ in xrange(m):
        u, v = map(int, raw_input().strip().split(" "))
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    #print (graph)
    
    detectCycle(graph)
    print (cycleExists)
    # print cyclea
    for item in cycles:
        print ("->".join(str(node) for node in item))
