# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 17:46:48 2016

@author: arnab
"""

"""
Cut the Tree: https://www.hackerrank.com/challenges/cut-the-tree
This problem is quite useful in the sense that it uses DFS to find the 
sum of all vertex values rooted at a vertex for all vertices in a tree.
Use of iterative DFS - recursion was giving TLE 
"""
from collections import Counter

def solution(n, graph, labels):
    
    def DFS(root):
        stack = [root]
        visited[root] = True
        
        while stack:
            v = stack[-1]
            if graph[v]:
                w = graph[v].pop()
                if not visited.get(w, False):
                    visited[w] = False
                    edgeTo[w] = v
                    stack.append(w)
            else:
                countlabel[v] += labels[v-1]
                if v != root:
                    countlabel[edgeTo[v]] += countlabel[v]
                stack.pop()
    
    visited, edgeTo = {}, {}
    countlabel = Counter()
    root = 1
    DFS(root)
    ans = float('inf')
    for node in xrange(2, n+1):
        ans = min(ans, countlabel[root] - 2 * countlabel[node])
    return ans

if __name__ == '__main__':
    n = int(raw_input().strip())
    labels = map(int, raw_input().strip().split(" "))       
    graph = Counter()
    for i in xrange(n-1):
        u, v = map(int, raw_input().strip().split(" "))
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    print (solution(n, graph, labels))