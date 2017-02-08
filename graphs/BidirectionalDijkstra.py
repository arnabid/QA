# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:47:11 2016

@author: arnab
"""

"""
Bidirectional Dijkstra single source single target shortest path algorithm;
alternating forward and reverse search.

Reference:
http://www.cs.princeton.edu/courses/archive/spr06/cos423/Handouts/EPP%20shortest%20path%20algorithms.pdf
"""

from PriorityQueue import PriorityQueue
from BuildDGraph import BuildDGraph

class Dijkstra(object):
    def __init__(self, G):
        self.G = G
        self.flabel = {} # distance labels for the forward search
        self.blabel = {} # distance labels for the reverse search
        self.fedgeTo = {} # parent links
        self.bedgeTo = {} # child links
    
    def printShortestPath(self, s, t, x, y, mu):
        path = []
        
        # construct the path from s --> y
        while x != s:
            path.append(x)
            x = self.fedgeTo[x]

        path.append(s)
        path.reverse()
        
        # construct the part of the path from y to t
        while y != t:
            path.append(y)
            y = self.bedgeTo[y]

        path.append(t)
        
        # print the shortest path from s --> t
        print (path, mu)

    def shortestPath(self, s, t):
        # returns the shortest path from s -> t in G
        fscan = set() # set of vertices that have been scanned during the forward search
        rscan = set() # set of vertices that have been scanned during the reverse search

        # define the forward and reverse PriorityQueue objects
        PQf = PriorityQueue()
        PQb = PriorityQueue()
        for node in self.G.nodes():
            # add all nodes to the priority queues with infinite priority
            PQf.add(node, float('inf'))
            PQb.add(node, float('inf'))
            self.flabel[node] = float('inf')
            self.blabel[node] = float('inf')

        # reduce source priority to zero in the forward priority queue
        PQf.add(s, 0)
        self.flabel[s] = 0
        
        # reduce the target priority to zero in the reverse priority queue
        PQb.add(t, 0)
        self.blabel[t] = 0
        
        # Alternate the forward and reverse search till the termination condition is met
        mu = float('inf')  # length of the best path seen so far
        """ let (x,y) be the last scanned arc in the forward search when mu gets updated
        or let (y,x) be the last scanned arc in the reverse search when mu gets updated. """
        x,y = None,None
        flag = True # True -> do forward search; else do reverse search

        while True:
            if flag:
                # do one iteration of the forward search
                if PQf.entry_finder:
                    if PQf.pq[0][0] + PQb.pq[0][0] >= mu:
                        self.printShortestPath(s,t,x,y,mu)
                        break
                    v = PQf.pop()
                    fscan.add(v)
                    for w in self.G.out_adj(v):
                        vw_weight =  self.G.get_edge_weight((v,w))
                        
                        # update the forward distance labels and the parent pointers
                        if self.flabel[w] > self.flabel[v] + vw_weight:
                            self.flabel[w] = self.flabel[v] + vw_weight
                            PQf.add(w, self.flabel[w])
                            self.fedgeTo[w] = v
                        
                        # update mu and x, y
                        if  w in rscan and self.flabel[v] + vw_weight + self.blabel[w] < mu:
                            mu = self.flabel[v] + vw_weight + self.blabel[w]
                            x,y = v,w
                flag = False
            else:
               # do one iteration of the reverse search
                if PQb.entry_finder:
                    if PQf.pq[0][0] + PQb.pq[0][0] >= mu:
                        self.printShortestPath(s,t,x,y,mu)
                        break
                    v = PQb.pop()
                    rscan.add(v)
                    for w in self.G.in_adj(v):
                        wv_weight =  self.G.get_edge_weight((w,v))
                        
                        # update the reverse distance labels and the child pointers
                        if self.blabel[w] > self.blabel[v] + wv_weight:
                            self.blabel[w] = self.blabel[v] + wv_weight
                            PQb.add(w, self.blabel[w])
                            self.bedgeTo[w] = v
                        
                        # update mu and x, y
                        if w in fscan and self.blabel[v] + wv_weight + self.flabel[w] < mu:
                            mu = self.blabel[v] + wv_weight + self.flabel[w]
                            x,y = w,v
                flag = True

if __name__ == '__main__':
    inputfilepath = input("Enter the input file path: ") # input file that describes G
    bg = BuildDGraph(inputfilepath)
    G = bg.buildDGraph() # returns a directed graph object
    
    dj = Dijkstra(G)
    dj.shortestPath('s','t')
    