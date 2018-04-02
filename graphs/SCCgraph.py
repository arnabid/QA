# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 07:50:35 2017

@author: arnab
"""
# program to determine if a directed graph is strongly connected ie;
# there is a path between any pair of vertices

from collections import defaultdict
  
class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    #A function used by isSC() to perform DFS
    def DFSUtil(self,v,visited):
        visited[v]= True
        for w in self.graph[v]:
            if not visited[w]:
                self.DFSUtil(w,visited)
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
         
        return g

    # The main function that returns true if graph is strongly connected
    # using kosaraju's algorithm
    def isSC(self):
        visited =[False]*(self.V)
        
        # Do DFS
        self.DFSUtil(0,visited)
 
        # If DFS traversal doesnt visit all vertices, then return false
        for i in xrange(self.V):
            if not visited[i]:
                return False
 
        # Create a reversed graph
        gr = self.getTranspose()
         
        # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
 
        # Do DFS for reversed graph starting from first vertex.
        # Staring vertex must be same starting point of first DFS
        gr.DFSUtil(0,visited)
 
        # If all vertices are not visited in second DFS, then
        # return false
        for i in xrange(self.V):
            if not visited[i]:
                return False
 
        return True

if __name__ == '__main__':
    g1 = Graph(5)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)
    g1.addEdge(3, 0)
    g1.addEdge(2, 4)
    g1.addEdge(4, 2)
    
    if g1.isSC():
        print "graph is strongly connected"
    else:
        print "graph is not strongly connected"