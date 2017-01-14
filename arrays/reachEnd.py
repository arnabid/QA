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
    

if __name__ == '__main__':
    #arr = map(int, raw_input().strip().split(" "))
    #start = 0
    
    # Testing consistency of BFS and DFS
    arr = [random.randint(0,3) for _ in xrange(0,10)]
    start = random.randint(0,9)
    
    
    print (DFSsol(arr, start))
    print (BFSsol(arr, start))
