# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:43:04 2016

@author: arnab
"""
n = int(raw_input().strip())
val = map(int, raw_input().strip().split(" ")) # can be used as a dict
total = sum(val)

marked = {}
s = '1'
mindiff = float('inf')

def adj(node):
    pass

def DFS(v):
    marked[v] = True
    value = val[int(v)-1]
    for w in adj(v):
        if not marked.get(w, False):
            value += DFS(w)
    mindiff = min(mindiff, total - value)
    return value
    

"""
====
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
mindiff = float('inf')
n = int(raw_input().strip())
val = map(int, raw_input().strip().split(" ")) # can be used as a dict
total = sum(val)
marked = {}
s = '1'

def adj(node):
    return adj_list[node]

def DFS(v):
    global mindiff
    marked[v] = True
    value = val[int(v)-1]
    for w in adj(v):
        if not marked.get(w, False):
            value += DFS(w)
    # here you are backtracking to v's parent; update mindiff
    if v != '1':
        mindiff = min(mindiff, abs(total - 2*value))
    return value

# build the adjacency list
adj_list = {}
for case in xrange(n-1):
    u, v = raw_input().strip().split(" ")
    if u in adj_list:
        adj_list[u].append(v)
    else:
        adj_list[u] = list(v)
    if v in adj_list:
        adj_list[v].append(u)
    else:
        adj_list[v] = list(u)

DFS(s)
print (mindiff)

"""
=====
""""
        

if __name__ == '__main__':
    DFS(s)
    

        
    