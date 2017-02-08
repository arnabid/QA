# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:57:03 2016

@author: arnab
"""

"""
Couting on a Tree
https://www.hackerrank.com/challenges/counting-on-a-tree
"""
from collections import Counter

def findPath(u, end, graph):
    stack = [u]
    visited = Counter()
    visited[u] = True
    edgeTo = Counter()
    
    while stack:
        v = stack.pop()
        if v == end:
            break
        for w in graph[v]:
            if not visited.get(w, False):
                stack.append(w)
                visited[w] = True
                edgeTo[w] = v
    
    path = set()
    while end != u:
        path.add(end)
        end = edgeTo[end]
    path.add(u)
    return path

if __name__ == '__main__':
    n, q = map(int, raw_input().strip().split(" "))
    count = [0]
    count.extend(map(int, raw_input().strip().split(" ")))
    
    # build the graph
    graph = Counter()
    for _ in xrange(n-1):
        u, v = map(int, raw_input().strip().split(" "))
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    
    # build the count -> nodes dictionary
    dic = Counter()
    for i in xrange(1,len(count)):
        if count[i] in dic:
            dic[count[i]].add(i)
        else:
            dic[count[i]] = set([i])
    
    for _ in xrange(q):
        u, v, x, y = map(int, raw_input().strip().split(" "))
        path1 = findPath(u, v, graph)
        path2 = findPath(x, y, graph)
        path2 = set()
        
        total = 0
        for node in path1:
            if len(dic[count[node]]) > 1:
                total += len(path2.intersection(dic[count[node]] - set([node])))
        print (total)
