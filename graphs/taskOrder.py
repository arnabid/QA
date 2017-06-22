# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:23:03 2017

@author: arnab
"""

"""
input: lists of tasks
Each task has a list of dependencies: tasks which need to complete
before the current task can begin

output: give a valid ordering of tasks
"""

from collections import Counter

class Task(object):
    def __init__(self, key = None, ancestors = []):
        self.key = key
        self.ancestors = ancestors
    
    def setAncestors(self, ancestors):
        self.ancestors = ancestors


def buildGraph(tasks, graph):
    for task in tasks:
        if task.key not in graph:
            graph[task.key] = []
        parents = task.ancestors
        for parent in parents:
            if parent.key in graph:
                graph[parent.key].append(task.key)
            else:
                graph[parent.key] = [task.key]

def createOrderUtil(graph, node, stack, visited):
    visited.add(node)
    for w in graph[node]:
        if w not in visited:
            createOrderUtil(graph, w, stack, visited)
    stack.append(node)
    
def createOrder():
    
    stack = []
    visited = set()
    for node in graph.keys():
        if node not in visited:
            createOrderUtil(graph, node, stack, visited)
    
    stack.reverse()
    return stack

if __name__ == '__main__':
    tA = Task("A")
    tB = Task("B")
    tC = Task("C")
    tD = Task("D")
    
    tD.setAncestors([tB])
    tB.setAncestors([tA,tC])
    tC.setAncestors([tA])
    tA.setAncestors([])
    
    tasks = [tA, tB, tC, tD]
    graph = Counter()
    
    # build the graph 
    buildGraph(tasks, graph)
    print (graph)
    
    # find a topological ordering of the nodes
    print (createOrder())
    
    
    
        
    
    
        