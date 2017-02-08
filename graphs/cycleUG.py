# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:37:37 2016

@author: arnab
"""

""" 
Detection of cycle in a undirected graph G
In an undirected graph, there are only tree and back edges. The presence of a backedge to a
node that is not the parent implies a cycle. If there are no parallel edges b/w 2 nodes,
the backedge to a parent is the tree edge. If there are parallel edges, then the 
backedge found need not be the tree edge.

Also consider that the graph might have multiple connected components. Have to start
a DFS from each connected component.

Requirements:
Determine if there exists a cycle in G
Find all the cycle(s) in G

"""
from collections import Counter
visited, edgeTo, onStack = {}, {}, {}
backEdges = Counter()
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
    cycles.append(cycleFound)

def detectCycle(graph):
    nodes = graph.keys()
    
    for node in nodes:
        if not visited.get(node, False):
            DFS(node)

def DFS(v):
    visited[v] = True
    onStack[v] = True
    for w in graph[v]:
        if not visited.get(w, False):
            edgeTo[w] = v
            DFS(w)
        elif onStack[w] and w != edgeTo[v]:
            addCycle(v,w)
        elif onStack[w] and w == edgeTo[v]: # deal parallel edges
            backEdges[(v,w)] += 1
            if backEdges[(v,w)] > 1:
                addCycle(v,w)
    onStack[v] = False
        

if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split(" "))
    graph = Counter()
    
    for _ in xrange(m):
        u, v = map(int, raw_input().strip().split(" "))
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    #print (graph)
    
    detectCycle(graph)
    print (cycleExists)
    # print cyclea
    for item in cycles:
        print ("->".join(str(node) for node in item))