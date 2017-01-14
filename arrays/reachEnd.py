# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:21:41 2016

@author: arnab
"""

"""
given an 1D array and start index, find out if the end index can be reached
a[i] = upto a[i] steps can be taken from index i
"""

from collections import Counter
import Queue
import random

"""
returns the min number of steps to reach end of array
returns -1 if end is not reachable
"""
def BFSsol(arr, start):
    if arr[start] == 0:
        return -1

    n = len(arr)
    q = Queue.Queue()
    q.put(start)
    
    visited, label = Counter(), Counter()
    label[start] = 0
    while not q.empty():
        v = q.get()
        if v == n-1:
            return label[v]
        for w in xrange(v+1, min(n,v+arr[v]+1)):
            if not visited.get(w, False):
                q.put(w)
                visited[w] = True
                label[w] = label[v] + 1
                if w == n-1:
                    return label[w]
    return -1


def DFSsol(arr, start):
    if arr[start] == 0:
        return -1

    n = len(arr)
    visited = Counter()
    
    def dfs(v):
        if v == n-1:
            return True
        visited[v] = True
        for w in xrange(v+1, min(n,v+arr[v]+1)):
            if not visited.get(w, False):
                found = dfs(w)
                if found:
                    return True
        return False
    
    return dfs(start)


def DPsol(arr, start):
    if arr[start] == 0:
        return -1
    
    n = len(arr)
    if start == n-1:
        return 0

    steps = [float('inf')] * n
    steps[start] = 0
    
    lv = start #last visited
    for i in xrange(start, n-1):
        if steps[i] == float('inf'):
            return -1
        
        for w in xrange(lv+1, min(n, i+arr[i]+1)):
            steps[w] = min(steps[w], steps[i]+1)
            if w == n-1:
                return steps[w]
        lv = max(lv, min(n-1,i+arr[i]))
    return -1
    
    

if __name__ == '__main__':
    #arr = map(int, raw_input().strip().split(" "))
    #start = 0
    
    # Testing consistency of BFS, DFS, DP
    arr = [random.randint(0,6) for _ in xrange(0,100)]
    start = random.randint(0,9)
    
    
    print (DPsol(arr, start))
    print (BFSsol(arr, start))
    print (DFSsol(arr, start))
