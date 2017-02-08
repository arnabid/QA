# -*- coding: utf-8 -*-
"""
Created on Sun May 29 08:45:48 2016

@author: arnab
"""
""" 
Problem: https://www.hackerrank.com/challenges/even-tree
"""

from collections import Counter
import itertools
import heapq
class PriorityQueue(object):
    def __init__(self):
        self.pq = [] # list of entries arranged in a heap
        self.entry_finder = {} # mapping of tasks to entries
        self.REMOVED = '<removed-task>' # placeholder for a removed task
        self.counter = itertools.count() # unique sequence count

    def add(self, task, priority=0):
        """ Add a new task or update the priority of an existing task """
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        """ Mark an existing task in the heap as REMOVED and delete it from the
        entry_finder.  Raise KeyError if not found. """
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        """ Remove and return the lowest priority task from the heap. Raise KeyError if empty. """
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return (task, priority)
        raise KeyError('pop from an empty priority queue')

        
def solution(graph):
    
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited.get(w,False):
                edgeTo[w] = v
                dfs(w)
                countlabel[v] += countlabel[w]
        PQ.add(v, countlabel[v])

    # pick a vertex and start a dfs
    root = '1'
    visited = {}
    edgeTo = {}
    countlabel = Counter()
    for key in graph:
        countlabel[key] = 1
    PQ = PriorityQueue()
    dfs(root)
    
    count = 0
    while PQ.entry_finder:
        (node, label) = PQ.pop()
        if label % 2 == 0:
            count += 1
            while node != root:
                node = edgeTo[node]
                countlabel[node] -= label
                PQ.add(node, countlabel[node])
    return count-1

if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split(" "))
    graph = Counter()
    for i in xrange(m):
        u, v = raw_input().strip().split(" ")
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    print (solution(graph))
