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

def printSolution(graph, edgeTo, start, end):
    path, rolls = [], []
    while end != start:
        path.append(end)
        rolls.append(graph[edgeTo[end]][end])
        end = edgeTo[end]
    path.append(start)
    path.reverse()
    rolls.reverse()
    print ("Quickest way up is " + "->".join(str(node) for node in path))
    print ("The sequence of dice rolls is " + ",".join(str(roll) for roll in rolls))

def solution(graph, start, end):
    dlabels = Counter()
    edgeTo = Counter()
    dlabels[start] = 0
    q = Queue.Queue()
    q.put(start)
        
    while not q.empty():
        v = q.get()
        if v == end:
            printSolution(graph, edgeTo, start, end)
            return dlabels[v]
        for w in graph[v]:
            if w not in dlabels:
                q.put(w)
                dlabels[w] = 1 + dlabels[v]
                edgeTo[w] = v
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
        """ make the graph; graph is a dict of dicts
        graph[u][v] = w
        to reach v from u, roll w on the dice
        """
        for i in xrange(1, 100):
            graph[nodes[i]] = Counter()
            for x in xrange(nodes[i]+1, min(nodes[i]+7,101) ):
                graph[nodes[i]][nodes[x]] = x - nodes[i]
            #graph[nodes[i]] = [nodes[x] for x in xrange(nodes[i]+1, min(nodes[i]+7,101) )]
        print (solution(graph, 1, 100))
