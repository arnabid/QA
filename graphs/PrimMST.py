import heapq
from UGraph import UGraph
from BuildUGraph import BuildUGraph

'''
Prim's MST algorithm
'''

class PrimMST(object):
    def __init__(self, G):
        self.G = G

    def findMST(self):
        # returns the MST
        
        # get a list of nodes in the input graph
        nodes = self.G.nodes()

        # initialize the output MST, n nodes, n-1 edges
        outG = UGraph(len(nodes), len(nodes)-1)

        # initialize heap and s[], s[v] = 1 if v is already reached
        heap = []
        s = {}
        for node in nodes:
            s[node] = 0

        # pick root
        r = nodes[0]
        s[r] = 1

        for w in self.G.adj(r):
            # insert edge and weight(priority) in the heap
            heapq.heappush(heap, (self.G.get_edge_weight((r,w)),(r,w)))

        while heap:
            # get the minimum edge from the cut (does not delete)
            weight, (u,v) = heap[0]
            if s[u] == 1 and s[v] == 1: # both u and v are in the same cut
                heapq.heappop(heap) # delete edge, since this will form a cycle
                continue

            s[v] = 1
            outG.add_edge((u,v), weight)
            heapq.heappop(heap) # delete min edge

            for w in self.G.adj(v):
                if s[w] == 0:
                    heapq.heappush(heap, (self.G.get_edge_weight((v,w)),(v,w)))
        return outG

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildUGraph(inputfilepath)
G = bg.buildUGraph() # returns a graph object

pmst = PrimMST(G)
g = pmst.findMST()
print (g.graphToString())