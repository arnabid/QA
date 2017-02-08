# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:44:33 2016

@author: arnab
"""
from collections import Counter

def dfsUtil(graph, s, t):
    visited = Counter()
    visited[s] = True
    path = [s]
    
    def dfs(v):
        if v == t:
            print (path)
            path.pop()
            return
        visited[v] = True
        for w in graph[v]:
            if not visited.get(w, False):
                path.append(w)
                dfs(w)
        visited[v] = False
        path.pop()

    dfs(s)


if __name__ == '__main__':
    graph = Counter()
    graph[1] = [2]
    graph[2] = [3]
    graph[3] = [4,5]
    graph[5] = [2,4]
    s, t = 1, 4
    
    dfsUtil(graph, s, t)
    
    