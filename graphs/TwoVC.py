from BuildGraph import BuildGraph

'''
Check if a graph G is 2 vertex connected.
A graph G is 2 vertex connected iff it remains connected after
the removal of any node(and the incident edges on that node).

A cut-vertex is a node whose removal makes the graph disconnected.
If the root vertex in the DFS tree(not considering the back edges) has more than
one child, then it is a cut-vertex, otherwise it is not.

For all other nodes, check if the deepest back-edge from EVERY subtree goes to a proper
ancestor(parent and above) of the node. If it does for all the sub-trees rooted at that vertex, then
it is NOT a cut-vertex.

ALL leaf nodes in a DFS tree are not cut-vertices.

The class below determines if G is 2 vertex connected and also finds all the
cut-vertices in G.
'''

class TwoVC(object):

    def __init__(self, G):
        self.marked = {}
        self.arr = {}
        self.edgeTo = {}
        self.G = G
        self.time = 0
        self.count = 0
        self.cutVertex = set()
        
        # select a node arbitrarily to start a DFS
        v = list(self.G.nodes())[0]
        self.checkVC(v)
        if self.count > 1:
            self.cutVertex.add(v)

    def checkVC(self, v):
        self.marked[v] = True
        self.arr[v] = self.time
        self.time += 1
        dbe = self.arr[v] # deepest back edge
        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                self.edgeTo[w] = v
                
                # count children of root
                if self.arr[v] == 0:
                    self.count += 1
                
                temp = self.checkVC(w)
                # check that for each subtree the deepest back-edge goes to a proper ancestor
                if self.arr[v] != 0 and temp >= self.arr[v]:
                    self.cutVertex.add(v)
                dbe = min(dbe, temp)

            else:
                if w != self.edgeTo.get(v, -1):
                    dbe = min(dbe, self.arr[w])
        return dbe

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

vc = TwoVC(G)
print (len(vc.cutVertex) == 0) # G is 2 vertex connected if there are no cut-vertices.
print ("The cut node(s) found %s" %str(vc.cutVertex))
    
        

    
        
