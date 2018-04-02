# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:14:09 2016

@author: arnab
"""
"""
Problem: https://www.hackerrank.com/challenges/cut-the-tree
http://algs4.cs.princeton.edu/41graph/NonrecursiveDFS.java
The iterativeDFS case passed all the test cases.
"""

"""
Preferred solution:
use the technique of pruning leaves as in the min height nodes question
"""
from collections import Counter
import Queue

if __name__ == '__main__':
    n = int(raw_input().strip())
    labels = map(int, raw_input().strip().split(" "))
    total = sum(labels)
    
    # graph object
    graph = Counter()
    
    # degree of each node to track leaves
    degree = Counter()
    
    #  build graph and the degree counter
    for i in xrange(n-1):
        u, v = map(int, raw_input().strip().split(" "))
        degree[u] += 1
        degree[v] += 1
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
   
    # put the first batch of leaves in the queue
    q = Queue.Queue()
    for node in graph.keys():
        if degree[node] == 1:
            q.put(node)

    # prune each leaf and calc the difference in labels between the rest of the tree
    # and the particular leaf
    res = float('inf')
    while n > 2:
        # prune the batch of leaves
        for i in xrange(q.qsize()):
            v = q.get()
            n -= 1
            res = min(res, abs(total-2*labels[v-1]))
            for w in graph.get(v, []):
                # increment label of parent as you prune the leaf
                labels[w-1] += labels[v-1] 
                degree[w] -= 1
                if degree[w] == 1:
                    q.put(w)
    
    # do a final calculation if the number of nodes remaining 
    # in the queue is 2
    if n == 2:
        n1 = q.get()
        res = min(res, abs(total - 2*labels[n1-1]))
    print (res)


""""
def solution(n, graph, labels):
    
    def IterativeDFS(s):
        stack = []
        visited[s] = True
        stack.append(s) # push s onto the stack

        while stack:
            v = stack[-1] # peek at the top element in the stack
            if graph[v]:
                w = graph[v].pop() # removes and returns the last item
                if not visited.get(w, False):
                    visited[w] = True
                    edgeTo[w] = v
                    stack.append(w)
            else:
                # backtrack here
                countlabel[v] += labels[v-1]
                if v != s:
                    countlabel[edgeTo[v]] += countlabel[v]
                stack.pop()
    
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited.get(w,False):
                dfs(w)
                countlabel[v] += countlabel[w]
        countlabel[v] += labels[v-1]
            

    # pick a vertex and start a dfs
    root = 1
    visited = {}
    edgeTo = {}
    countlabel = Counter()
    IterativeDFS(root)
    ans = float('inf')
    for i in xrange(2,n+1):
        ans = min(ans, abs(countlabel[root] - 2 * countlabel[i]))
    return ans

def BFSsolution(n, graph, labels):

    def bfs(s):
        q = Queue.Queue()
        q.put(s)
        visited[s] = True
        while not q.empty():
            v = q.get()
            for w in graph[v]:
                if not visited.get(w, False):
                    q.put(w)
                    visited[w] = True
                    edgeTo[w] = v

    # pick a vertex and start a bfs
    root = 1
    visited = {}
    edgeTo = {}
    edgeTo[root] = -1
    countlabel = Counter()
    bfs(root)
    for i in xrange(2, n+1):
        node, label = i, labels[i-1]
        while node != -1:
            countlabel[node] += label
            node = edgeTo[node]
    countlabel[root] += labels[0]
    ans = float('inf')
    for i in xrange(2,n+1):
        ans = min(ans, abs(countlabel[root]-2*countlabel[i]))
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
"""