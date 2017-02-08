from BuildGraph import BuildGraph

'''
Check if a graph G is 2 edge connected.
A graph G is 2 edge connected iff it remains connected after
the removal of any edge.
Brute force approach: Removing every edge and checking if the resulting
graph is connected. O(m2)
Remove the edge and start a DFS from one of its end-points. Check if there
exists a path to the other end-point after the DFS traversal is done.

A bridge edge is an edge whose removal makes the graph disconnected.

When backtracking from a node v, we need to ensure that there is a backedge from
some descendent of v(including v) to some proper ancestor of v.
'''


class TwoEC(object):

    def __init__(self, G):
        self.marked = {}
        self.arr = {}
        self.edgeTo = {}
        self.G = G
        self.time = 0
        self.bridgeEdge = [] # list of bridge edges in G
        
        # select a node arbitrarily to start a DFS
        v = list(self.G.nodes())[0]
        self.checkEC(v)

    def checkEC(self, v):
        self.marked[v] = True
        self.arr[v] = self.time
        self.time += 1
        dbe = self.arr[v] # deepest back edge
        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                self.edgeTo[w] = v
                dbe = min(dbe, self.checkEC(w))
            else:
                # make sure not to consider the tree edge (w,v)
                if w != self.edgeTo.get(v, -1):
                    dbe = min(dbe, self.arr[w])
        '''
        At this point we have the deepest back edge from v and its descendents
        information stored in dbe.
        '''
        if self.arr[v] != 0 and dbe == self.arr[v]:
            self.bridgeEdge.append((self.edgeTo[v], v))
        return dbe

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

ec = TwoEC(G)
print (len(ec.bridgeEdge) == 0) # If there are no bridge edges, then G is 2EC.
print ("The bridge edge(s) found %s" %str(ec.bridgeEdge))
