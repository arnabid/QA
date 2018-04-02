# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 10:31:44 2017

@author: arnab
"""
from collections import Counter
import Queue

"""
find all the shortest paths between s and t in G
"""
def findAllShortestPaths(graph, start, end):
    parent = Counter()
    label = Counter()
    label[start] = 0
    parent[start] = []
    
    q = Queue.Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        for w in graph.get(v,[]):
            if w not in label:
                q.put(w)
                label[w] = label[v]+1
                parent[w] = [v]
            else:
                if parent[w] and label[parent[w][0]] == label[v]:
                    parent[w].append(v)
    
    # start DFS from end
    visited = set()
    stack = []
    dfs(end, stack, parent, visited, start)


"""
print all shortest paths from start to end
"""
def dfs(v, stack, parent, visited, start):
    visited.add(v)
    stack.append(v)
    if v == start:
        print ('-'.join(stack[::-1]))
    for w in parent[v]:
        if w not in visited:
            dfs(w, stack, parent, visited, start)
    visited.remove(stack.pop())



if __name__ == '__main__':
    graph = Counter()
    graph['s'] = ['a','b','c']
    graph['a'] = ['s','d']
    graph['b'] = ['s','e']
    graph['c'] = ['s','f','g']
    graph['d'] = ['a','h']
    graph['e'] = ['b','h']
    graph['f'] = ['c','i']
    graph['g'] = ['j','c']
    graph['i'] = ['f','t']
    graph['h'] = ['d','e','t']
    graph['j'] = ['g','k']
    graph['k'] = ['j','t']
    graph['t'] = ['h','i','j','k']
    
    findAllShortestPaths(graph, 's', 't')
