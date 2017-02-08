# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:32:46 2016

@author: arnab
"""
import Queue
from collections import Counter
"""
Problem statement:
https://www.hackerrank.com/contests/master/challenges/count-luck?h_r=internal-search
"""

# backtracking
def findforks(arr, v, n, m, parent):
    forks = 0
    x = [0,-1,0,1]
    y = [-1,0,1,0]
    for k in xrange(4):
        if v[0] + x[k] >= 0 and v[0] + x[k] < n and v[1] + y[k] >= 0 \
        and v[1] + y[k] < m and parent[v] != (v[0] + x[k], v[1] + y[k]) and \
        (arr[v[0] + x[k]][v[1] + y[k]] in ".*"):
            forks += 1
    return forks

def findNeighbors(arr, v, visited, n, m):
    neighbors = []
    x = [0,-1,0,1]
    y = [-1,0,1,0]
    for k in xrange(4):
        if v[0] + x[k] >= 0 and v[0] + x[k] < n and v[1] + y[k] >= 0 \
        and v[1] + y[k] < m and (arr[v[0] + x[k]][v[1] + y[k]] in ".*") \
        and (v[0] + x[k], v[1] + y[k]) not in visited:
            neighbors.append((v[0] + x[k], v[1] + y[k]))
    return neighbors

def solDFS(arr, start, end, n, m):
    stack = [start]
    visited = Counter()
    parent = Counter()
    parent[start] = start
    while stack:
        v = stack.pop()
        visited[v] = True
        if v == end:
            break
        for w in findNeighbors(arr, v, visited, n, m):
            if not visited.get(w, False):
                stack.append(w)
                parent[w] = v

    p, ans = parent[end], 0
    #print (p)
    while p != start:
        if findforks(arr,p,n,m,parent) > 1:
            ans += 1
        p = parent[p]
    if findforks(arr,p,n,m,parent) > 1:
        ans += 1
    return ans

def solBFS(arr,start,end,n,m):
    # start a BFS from 'start' index
    q = Queue.Queue()
    q.put(start)
    visited = Counter()
    parent = Counter()
    parent[start] = start
    visited[start] = True
    ans = 0
    
    while not q.empty():
        v = q.get()
        
        if v == end:
            break
        for w in findNeighbors(arr, v, visited, n, m):
            q.put(w)
            parent[w] = v
            visited[w] = True
    #print (parent)
    
    # backtrack to start
    p = parent[end]
    while p != start:
        if findforks(arr,p,n,m,parent) > 1:
            ans += 1
        p = parent[p]
    if findforks(arr,p,n,m,parent) > 1:
        ans += 1
    return ans

if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        start, end = None, None
        arr = []
    
        n,m = map(int, raw_input().strip().split(" "))
        for i in xrange(n):
            temp = raw_input().strip().split(" ")
            if 'M' in temp[0]:
                start = (i,temp[0].find('M'))
            if '*' in temp[0]:
                end = (i,temp[0].find('*'))
            arr.append(temp[0])
        #print start, end, arr
        k = int(raw_input().strip())
        if solDFS(arr,start,end,n,m) == k:
            print ("Impressed")
        else:
            print ("Oops!")
