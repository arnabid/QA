from BuildGraph import BuildGraph
'''
Find all the connected components in a graph G using DFS
'''

class ConnectedComponents(object):

    def __init__(self, G):
        self.label = {}
        self.marked = {}
        self.G = G
        self.count = 0 # number of connected components in G
        self.findComponents()

    def dfsSearch(self, v):
        self.marked[v] = True
        self.label[v] = self.count
        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                self.dfsSearch(w)

    def findComponents(self):
        # finds all the connected components in G
        for node in self.G.nodes():
            self.label[node] = 0

        for node in self.label:
            if self.label[node] == 0:
                # start a DFS on this node
                self.count += 1
                self.dfsSearch(node)
        
    def isSameComponent(self, u, v):
        # returns a boolean to indicate if nodes u and v are in the same component in G
        return self.label.get(u, -1) == self.label.get(v, -2)

    def numComponents(self):
        # returns the number of components in G
        return self.count

    def id(self, v):
        # returns the component identifier for v(between 1 and count), -1 if v is not in G
        return self.label.get(v, -1)

    def listNodes(self, v):
        # returns a list of nodes(including v) that are in the same component as v
        node_list = []
        vid = self.id(v)
        for node in self.label:
            if self.id(node) == vid:
                node_list.append(node)
        return node_list

#testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

cc = ConnectedComponents(G)
print (cc.id('9'))
print (cc.listNodes('8'))
print (cc.numComponents())
print (cc.isSameComponent('7', '8'))
