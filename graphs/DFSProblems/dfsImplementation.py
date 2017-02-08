# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:29:11 2016

@author: arnab
"""
from collections import Counter


"""
this approach visits some edges more than twice
be careful***
"""
def dfsIter3(root, graph):
    stack = [root]
    visited = Counter()
    visited[root] = True
    print (root),
    while stack:
        v = stack[-1]
        fav = True
        for w in graph[v]:
            #print (v,w),- check # times each edge is traversed
            if not visited.get(w, False):
                stack.append(w)
                visited[w] = True
                fav = False
        if fav:
            print (stack.pop()),

"""
The following dfs procedure works ONLY for trees.
"""
def dfsIter1(root, graph):
    stack = [root]
    visited = Counter()
    while stack:
        v = stack.pop()
        visited[v] = True
        print (v),
        for w in graph[v]:
            #print (v,w), - check # times each edge is traversed
            if not visited.get(w, False):
                stack.append(w)


"""
DFS by modifying the input graph data structure
"""
def dfsIteration1(root, graph):
    stack = [root]
    visited = Counter()
    visited[root] = True
    print (root),
    
    while stack:
        v = stack[-1]
        if graph[v]: # checking if any edge left to be explored
            w = graph[v].pop()
            #print (v, w), - check # times each edge is traversed
            if not visited.get(w, False):
                # visiting w for first time, next start DFS from w
                # stack[] holds the ancestors of w at any point in time
                print (w),
                stack.append(w)
                visited[w] = True
        else:
            # backtrack from v
            stack.pop()

"""
DFS without modifying the input graph data structure
stack[i] = (node, index)
node -> node in the graph; index -> index in list of neighbors 
"""
def dfsIteration2(root, graph):
    stack = [(root,0)]
    visited = Counter()
    visited[root] = True
    print (root),
    
    while stack:
        v, index = stack[-1]
        if index < len(graph[v]): # checking if any edge left to be explored
            w = graph[v][index]
            #print (v, w), - check # times each edge is traversed
            stack[-1] = (v, index+1)
            if not visited.get(w, False):
                # visiting w for first time, next start DFS from w
                # stack[] holds the ancestors of w at any point in time
                print (w),
                stack.append((w,0))
                visited[w] = True
        else:
            # backtrack from v
            stack.pop()


"""
each node is processed once
each edge is traversed twice
time complexity : O(|V| + |E|)
space complexity : O(|V| + |E|)
O(|E|) -> adjacency list representation of graph
O(|V|) -> visited nodes
"""
def dfs_recursion(root, graph):
    visited = Counter()
    
    def dfs(v):
        visited[v] = True
        print (v), # process node v
        for w in graph[v]:
            #print (v,w), - check # times each edge is traversed
            if not visited.get(w, False):
                dfs(w)
    dfs(root)


if __name__ == '__main__':
    graph = Counter()
    
    graph['a'] = ['b','c']
    graph['b'] = ['a','c','d']
    graph['c'] = ['b','e','a','d']
    graph['d'] = ['c','b']
    graph['e'] = ['c']

#    graph[1] = [3,2]
#    graph[2] = [1,4,5]
#    graph[3] = [1,7,6]
#    graph[4] = [2,8]
#    graph[5] = [2]
#    graph[6] = [3]
#    graph[7] = [3,9]
#    graph[8] = [4]
#    graph[9] = [7]
    
    root = 'a'
    dfsIter1(root, graph)
    #print ("")
    #dfsIter3(root, graph)