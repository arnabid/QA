# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:40:11 2016

@author: arnab
"""

""" Scenario: Travel between two cities. Each route has some stops along the way
where you can fill up gas. We have no previous knowledge of the cost of each path; so our
optimum strategy at each stop is to fill up the gas tank.
How do we decide which route to take?

Answer: Take the minimum bottleneck path:
The bottleneck of each path is the max cost of all edges on that path """

from PriorityQueue import PriorityQueue
from BuildDGraph import BuildDGraph

class MinimumBottleneck(object):
    def __init__(self,G):
        self.G = G
        self.label = {}
        self.edgeTo = {}
    
    def printMinBottleneckPath(self,s,t):
        # prints the maximum capacity from s -> t in G
        path = []
        
        while t != s:
            path.append(t)
            t = self.edgeTo[t]
        path.append(s)
        path.reverse()
        
        print(path)
    
    def findPath(self,s,t):
        # finds the minimum bottleneck path from s -> t in G
        
        PQ = PriorityQueue()
        
        for node in self.G.nodes():
            PQ.add(node, float('inf'))
            self.label[node] = float('inf')
            
        # decrease the priority of source to 0
        PQ.add(s,0)
        self.label[s] = 0
        
        while PQ.entry_finder:
            v = PQ.pop()
            for w in self.G.out_adj(v):
                if max(self.label[v], self.G.get_edge_weight((v,w))) < self.label[w]:
                    self.label[w] = max(self.label[v], self.G.get_edge_weight((v,w)))
                    PQ.add(w, self.label[w])
                    self.edgeTo[w] = v

        self.printMinBottleneckPath(s,t)
        print ("The bottleneck of the minimum bottleneck path is %d" %self.label[t])
                    

if __name__ == '__main__':
    inputfilepath = input("Enter the input file path: ") # input file that describes G
    bg = BuildDGraph(inputfilepath)
    G = bg.buildDGraph() # returns a directed graph object
    
    mb = MinimumBottleneck(G)
    mb.findPath('s','t')