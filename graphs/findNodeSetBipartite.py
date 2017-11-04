# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:29:41 2017

@author: arnab
"""
import Queue
from collections import Counter

"""
given a bipartite graph G, find the two sets of nodes A, B
"""

def partitionNodes(graph):
    A, B = set(), set()
    
    # select a arbitrary node and start a BFS
    n = len(graph.keys())
    start = graph.keys()[0]
    A.add(start)
    q = Queue.Queue()
    q.put(start)
    step = 1
    
    while not q.empty():
        for _ in range(q.qsize()):
            v = q.get()
            for w in graph[v]:
                if w not in A and w not in B:
                    q.put(w)
                    if step % 2:
                        B.add(w)
                    else:
                        A.add(w)
        if len(A) + len(B) == n:
            break
        step += 1
    return A, B

if __name__ == '__main__':
    graph = Counter()
    graph[1] = [2,6]
    graph[2] = [1,3]
    graph[3] = [2,4]
    graph[4] = [5,3]
    graph[5] = [6,4]
    graph[6] = [1,5]
    
    print (partitionNodes(graph))