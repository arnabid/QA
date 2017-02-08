from PriorityQueue import PriorityQueue
from UGraph import UGraph
from BuildUGraph import BuildUGraph
'''
Prim's MST algorithm
'''

class PrimMST2(object):
    def __init__(self,G):
        self.G = G

    def findMST(self):
        #returns the MST
        label = {} # label for each node
        s = {}
        edgeTo = {}

        #get a list of nodes in the input graph
        nodes = self.G.nodes()

        # initialize the output MST, n nodes, n-1 edges
        outG = UGraph(len(nodes), len(nodes)-1)

        # pick root
        r = nodes[0]
        
        # define a PriorityQueue object
        PQ = PriorityQueue()
        for node in nodes:
            # add all nodes to the priority queue with infinite priority
            PQ.add(node, float('inf'))
            label[node] = float('inf')
            s[node] = 0

        # reduce source priority to zero
        PQ.add(r, 0)
        label[r] = 0

        while PQ.entry_finder:
            v = PQ.pop()
            s[v] = 1
            for w in self.G.adj(v):
                if s[w] == 0 and label[w] > self.G.get_edge_weight((v,w)):
                    label[w] = self.G.get_edge_weight((v,w))
                    PQ.add(w, label[w])
                    edgeTo[w] = [v, label[w]]
        
        # add the edges in the MST to the output graph
        for key in edgeTo:
            outG.add_edge((edgeTo[key][0],key),edgeTo[key][1])
            
        return outG

    
# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildUGraph(inputfilepath)
G = bg.buildUGraph() # returns a graph object

pmst = PrimMST2(G)
g = pmst.findMST()
print (g.graphToString())
