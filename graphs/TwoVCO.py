from BuildGraph import BuildGraph

'''
Check if a graph G is 2 vertex connected.
A graph G is 2 vertex connected iff it remains connected after
the removal of any node(and the incident edges on that node).

A cut-vertex is a node whose removal makes the graph disconnected.
If the source vertex in the DFS tree(not considering the back edges) has more than
one children, then it is a cut-vertex.
'''

class TwoVC(object):

    def __init__(self, G):
        self.marked = {}
        self.arr = {}
        self.edgeTo = {}
        self.G = G
        self.time = 0
        self.count = 0
        self.is2VC = True # boolean that indicates if G is 2-edge connected
        self.cutVertex = []
        
        # select a node arbitrarily to start a DFS
        #v = list(self.G.nodes())[0]
        v = '2'
        self.checkVC(v)
        if self.count > 1:
            self.is2VC = False
            self.cutVertex.append(v)

    def checkVC(self, v):
        self.marked[v] = True
        self.arr[v] = self.time
        self.time += 1
        dbe = self.arr[v] # deepest back edge
        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                self.edgeTo[w] = v
                temp = self.checkVC(w)
                # deepest back edge for the sub-trees from the source cannot be less than 0
                if self.arr[v] != 0 and temp >= self.arr[v]:
                    self.is2VC = False
                    self.cutVertex.append(v)
                dbe = min(dbe, temp)
                if self.arr[v] == 0:
                    self.count += 1
            else:
                if w != self.edgeTo.get(v, -1):
                    dbe = min(dbe, self.arr[w])
        return dbe

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

vc = TwoVC(G)
print (vc.is2VC)
print ("The cut node(s) found %s" %str(vc.cutVertex))
