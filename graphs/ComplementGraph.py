# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:46:51 2016

@author: arnab
"""
"""
BFS on the complement of G, where G is a sparse graph
Tweak to reduce time complexity
Problem: https://www.hackerrank.com/challenges/rust-murderer
"""
import Queue
from collections import Counter
def solution(n,graph,source):
    q = Queue.Queue()
    q.put(source)
    visited = {}
    visited[source] = True
    dlabel = Counter()
    L1, L2 = set(), set()
    for node in range(1, source) + range(source+1, n+1):
        L1.add(node)

    while not q.empty():
        u = q.get()
        if u in graph:
            for node in graph[u]:
                if not visited.get(node, False):
                    L1.remove(node)
                    L2.add(node)
        for l in L1:
            visited[l] = True
            q.put(l)
            dlabel[l] = dlabel[u] + 1
        L1 = L2.copy()
        L2.clear()
    s = ""
    for i in xrange(1,n+1):
        if i in dlabel:
            s += str(dlabel[i]) + " "
    print (s.strip())
                

if __name__ == '__main__':
    t = int(raw_input().strip())
    for case in xrange(t):
        n, m = map(int, raw_input().strip().split(" "))
        graph = Counter()
        for i in xrange(m):
            u, v = map(int, raw_input().strip().split(" "))
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        source = int(raw_input().strip())
        solution(n, graph, source)
