from PriorityQueue import PriorityQueue
from BuildDGraph import BuildDGraph
"""
Dijkstra's single source shortest path algorithm

observations: Once we find a shortest path from 's' to 't', we also know the 
shortest path from s to all intermediate nodes 'x' on that path.
This is also true for any intermediate node 'x' on that path ie we know a
shortest path from 'x' to any node following it on that path.
"""

class Dijkstra(object):
    def __init__(self,G,s):
        self.G = G
        self.s = s # source node
        self.label = {}
        self.edgeTo = {}
        #self.findShortestPath()
        self.findShortestPathwithFewestHops()
    
    def findShortestPathwithFewestHops(self):
        # returns the shortest path with the fewest hops; 2 shortest paths of equal length
        # can differ in the number of hops.
        hops = {}
        PQ = PriorityQueue()
        for node in self.G.nodes():
            # add all nodes to the priority queue with infinite priority
            PQ.add(node, float('inf'))
            self.label[node] = float('inf')
            hops[node] = float('inf')

        # reduce source priority to zero
        PQ.add(self.s, 0)
        self.label[self.s] = 0
        hops[self.s] = 0

        while PQ.entry_finder:
            v = PQ.pop()  # gets the entry with the least priority
            for w in self.G.out_adj(v):
                edge_weight = self.G.get_edge_weight((v,w))
                if self.label[w] > self.label[v] + edge_weight or \
                self.label[w] == self.label[v] + edge_weight and hops[w] > hops[v] + 1:
                    self.label[w] = self.label[v] + edge_weight
                    PQ.add(w, self.label[w])
                    self.edgeTo[w] = v
                    hops[w] = hops[v] + 1

    def findShortestPath(self):
        # define a PriorityQueue object
        PQ = PriorityQueue()
        for node in self.G.nodes():
            # add all nodes to the priority queue with infinite priority
            PQ.add(node, float('inf'))
            self.label[node] = float('inf')

        # reduce source priority to zero
        PQ.add(self.s, 0)
        self.label[self.s] = 0

        while PQ.entry_finder:
            v = PQ.pop()  # gets the entry with the least priority
            for w in self.G.out_adj(v):
                if self.label[w] > self.label[v] + self.G.get_edge_weight((v,w)):
                    self.label[w] = self.label[v] + self.G.get_edge_weight((v,w))
                    PQ.add(w, self.label[w])
                    self.edgeTo[w] = v

    def shortestPathLength(self, v):
        # returns the length of shortest path from s to v; else returns -1
        return self.label.get(v, -1)

    def shortestPathTo(self, v):
        # returns a list of nodes to denote a path from source s to vertex v
        
        if v not in self.edgeTo: # v is not reachable from s
            return []

        path = []   
        while v != self.s:
            path.append(v)
            v = self.edgeTo[v]
        path.append(self.s)
        
        path.reverse()
        return path


if __name__ == '__main__':
    inputfilepath = input("Enter the input file path: ") # input file that describes G
    bg = BuildDGraph(inputfilepath)
    G = bg.buildDGraph() # returns a directed graph object
    
    dj = Dijkstra(G, 's')
    print (dj.shortestPathLength('t'))
    print (dj.shortestPathTo('t'))
