# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:57:16 2017

@author: arnab
"""

"""
problem: https://www.hackerrank.com/challenges/the-quickest-way-up
"""

from collections import Counter
import Queue

def solution(source, end):
    dlabels = Counter()
    dlabels[source] = 0
    q = Queue.Queue()
    q.put(source)
        
    while not q.empty():
        v = q.get()
        if v == end:
            return dlabels[v]
        for w in graph[v]:
            if w not in dlabels:
                q.put(w)
                dlabels[w] = 1 + dlabels[v]
    return -1

if __name__ == '__main__':
    t = int(raw_input().strip())
    for _ in xrange(t):
        graph = Counter()
        nodes = [i for i in xrange(0,101)]
        nl = int(raw_input().strip())
        for ladder in xrange(nl):
            u, v = map(int, raw_input().strip().split(" "))
            nodes[u] = v
        ns = int(raw_input().strip())
        for snake in xrange(ns):
            u, v = map(int, raw_input().strip().split(" "))
            nodes[u] = v
        # make the graph
        for i in xrange(1, 100):
            graph[nodes[i]] = [nodes[x] for x in xrange(nodes[i]+1, min(nodes[i]+7,101) )]
        print (solution(1, 100))
