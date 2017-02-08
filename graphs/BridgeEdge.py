from BuildGraph import BuildGraph

'''
Check if an edge (u,v) in G is a bridge edge.
A bridge edge is an edge whose removal makes the graph disconnected.

Notes:
mark[u] = 1, start DFS on v. This will create a DFS tree rooted at u, and it will
only visit v as the child of u. The other children of u in the DFS tree
will not be visited. Also, no need to complete the whole DFS procedure on v
As soon as any back-edge from sub tree rooted at v to u is found, we can
conclude that (u,v) is not a back-edge.
'''

class BridgeEdge(object):

    def __init__(self, G, edge):
        self.x, self.y = edge # edge is the input edge
        self.marked = {}
        self.arr = {}
        self.edgeTo = {}
        self.G = G
        self.time = 1
        self.isBridgeEdge = True # boolean to indicate if edge is a bridge

        # check if given edge exists in the graph G
        if not self.G.has_edge(edge):
            raise Exception("Edge %s not present in G" %str(edge))
        
        # mark one end-point of the given edge as visited and start a DFS
        # from the other end-point
        self.marked[self.x] = True
        self.arr[self.x] = 0
        self.edgeTo[self.y] = self.x
        self.checkBridgeEdge(self.y)

    def checkBridgeEdge(self, v):
        self.marked[v] = True
        self.arr[v] = self.time
        self.time += 1
        dbe = self.arr[v] # deepest back edge
        for w in self.G.adj(v):
            '''
            A back edge from subtree rooted at v to u already found
            then (u,v) cannot be a bridge edge, no need to scan other
            adjacent nodes of v
            '''
            if self.isBridgeEdge == False:
                return dbe # back-edge to root has already been discovered and it is stored in dbe
            if not self.marked.get(w, False):
                self.edgeTo[w] = v
                dbe = min(dbe, self.checkBridgeEdge(w))
            else:
                # make sure not to consider the tree edge (w,v)
                if w != self.edgeTo.get(v, -1):
                    dbe = min(dbe, self.arr[w])

        # at any point if a back edge is found to the root, edge is not a bridge
        if dbe == 0:
            self.isBridgeEdge = False

        return dbe

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

edge = ('6', '4') 
be = BridgeEdge(G, edge)
print (be.isBridgeEdge)
# To check that DFS calls on unnecessary nodes are avoided
print ("Nodes visited = %s" %str(list(be.marked.keys())))

'''
tinyG.txt
7
8
1 4 1
1 2 1
2 4 1
6 4 1
7 6 1
3 2 1
3 5 1
2 5 1
'''
