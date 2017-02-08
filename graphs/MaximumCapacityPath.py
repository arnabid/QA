# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:00:09 2016

@author: arnab
"""

""" Find the maximum capacity/bottleneck path between 2 nodes
The capacity of a path is the minimum weight of all edges in the path.
Here the weight of an edge is the capacity of the edge and not the length of the edge.

We use the Max heap as a Priority Queue PQ. At any point once we pull out the node with the max priority(capacity) 
from PQ, its capacity cannot increase, any other path to it from s will have a capacity
less than or equal to it.
"""

from PriorityQueue import PriorityQueue
from BuildDGraph import BuildDGraph

class MaximumCapacity(object):
    def __init__(self,G):
        self.G = G
        self.label = {}
        self.edgeTo = {}
    
    def printMaxCapacityPath(self,s,t):
        # prints the maximum capacity from s -> t in G
        path = []
        
        while t != s:
            path.append(t)
            t = self.edgeTo[t]
        path.append(s)
        path.reverse()
        
        print(path)
    
    def findPath(self,s,t):
        # finds the maximum capacity path from s -> t in G
        
        PQ = PriorityQueue()
        
        for node in self.G.nodes():
            PQ.add(node, 0)
            self.label[node] = 0
            
        # increase the priority of source to infinity
        PQ.add(s,-float('inf'))
        self.label[s] = float('inf')
        
        while PQ.entry_finder:
            v = PQ.pop()
            for w in self.G.out_adj(v):
                if min(self.label[v], self.G.get_edge_weight((v,w))) > self.label[w]:
                    self.label[w] = min(self.label[v], self.G.get_edge_weight((v,w)))
                    PQ.add(w, -self.label[w])
                    self.edgeTo[w] = v

        self.printMaxCapacityPath(s,t)
        print ("The capacity of the maximum capacity path is %d" %self.label[t])
                    

if __name__ == '__main__':
    inputfilepath = input("Enter the input file path: ") # input file that describes G
    bg = BuildDGraph(inputfilepath)
    G = bg.buildDGraph() # returns a directed graph object
    
    mc = MaximumCapacity(G)
    mc.findPath('s','t')


