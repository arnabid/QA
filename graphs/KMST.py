from UnionFind import UF
from UGraph import UGraph
from BuildUGraph import BuildUGraph
'''
Kruskal's MST
'''

class KMST(object):
    def __init__(self, G):
        self.G = G # G is the input graph

    def findMST(self):
        # returns the MST
        
        # get a list of nodes in the input graph
        nodes = self.G.nodes()

        # initialize the output MST
        outG = UGraph(len(nodes), len(nodes)-1)

        # initialize the Union-Find object
        uf = UF(nodes)

        # get the list of edges in the input graph
        edges = self.G.get_edges()

        # sort the edges by weight
        edges.sort(key=lambda tup: tup[0])

        # perform Kruskal MST algo
        for edge in edges:
            w, (u,v) = edge
            if not uf.connected(u,v):
                uf.union(u,v)
                outG.add_edge((u,v),w)
        return outG

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildUGraph(inputfilepath)
G = bg.buildUGraph() # returns a graph object

kmst = KMST(G)
g = kmst.findMST()
print (g.graphToString())

        
