import queue
from BuildUGraph import BuildUGraph

'''
Color the nodes of a bipartite graph G: 0 or 1
Also support the operation if 2 nodes have the same color
Assumption: G is connected.

'''

class BPColor(object):

    def __init__(self, G):
        self.G = G
        self.marked = {}
        self.label = {}

        # select a node arbitarily and start a BFS
        v = G.nodes()[0]
        self.color(v)

    def color(self, v):
        q = queue.Queue()
        q.put(v)
        self.marked[v] = True
        self.label[v] = 0
        while not q.empty():
            v = q.get()
            for w in self.G.adj(v):
                if not self.marked.get(w, False):
                    q.put(w)
                    self.marked[w] = True
                    self.label[w] = int(not self.label[v])

    def isSameColor(self, u, v):
        return self.label[u] == self.label[v]

inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildUGraph(inputfilepath)
G = bg.buildUGraph() # returns a graph object

bpc = BPColor(G)
print (bpc.isSameColor('1', '6'))

