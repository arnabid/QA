import queue
from BuildUGraph import BuildUGraph
'''
You are given a binary tree in which each node contains a value.
Design an algorithm to print all paths which sum to a given value.
The path does not need to start or end at the root or a leaf.
Problem 4.9 on page 246 Cracking the Coding Interview 5th edition
'''

'''
Input: Binary tree represented as an undirected graph G.
I will first do a BFS and assign level numbers to each node.
These level numbers will be value assigned to each node.
'''

class FindPaths(object):
    def __init__(self, G, pval):
        self.G = G
        self.pval = pval
        self.edgeTo = {}
        self.marked = {}
        self.label = {}
        self.paths = [] # list of paths whos sum equals given value

        # lets first do a preliminary BFS to assign label numbers
        v = self.G.nodes()[0]
        self.doBFS(v)

        # At this point each node is assigned a value. Now let's get to the question.
        # Start a BFS from every node
        for node in self.G.nodes():
            self.marked = {}
            self.findPaths(node)

    def doBFS(self, v):
        # does a preliminary BFS to asign each node a label
        q = queue.Queue()
        self.marked[v] = True
        self.label[v] = 0
        q.put(v)
        while not q.empty():
            v = q.get()
            for w in self.G.adj(v):
                if not self.marked.get(w, False):
                    q.put(w)
                    self.marked[w] = True
                    self.label[w] = self.label[v] + 1

    def findPaths(self, v):
        # finds all the paths whose sum equals given value
        root = v
        sumlabel = {}
        sumlabel[v] = self.label[v]
        q = queue.Queue()
        self.marked[v] = True
        q.put(v)
        if sumlabel[v] == self.pval:
            self.paths.append(v)
        while not q.empty():
            v = q.get()
            for w in self.G.adj(v):
                if not self.marked.get(w, False):
                    q.put(w)
                    self.marked[w] = True
                    self.edgeTo[w] = v
                    sumlabel[w] = self.label[w] + sumlabel[v]
                    if sumlabel[w] == self.pval:
                        path = []
                        while w != root:
                            path.append(w)
                            w = self.edgeTo[w]
                        path.append(root)
                        self.paths.append(path)

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildUGraph(inputfilepath)
G = bg.buildUGraph() # returns a graph object

fp = FindPaths(G, 6)
print (fp.label)
print (fp.paths)
