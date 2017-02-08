from BuildGraph import BuildGraph

'''
Check if a vertex is a cut-vertex.
A cut-vertex is a node whose removal(and its incident edges) makes the graph disconnected.

If the root in the DFS tree(not considering the back edges upto the root) has more than
one children, then it is a cut-vertex.
'''

class IsCutVertex(object):

    def __init__(self, G, v):
        self.marked = {}
        self.arr = {}
        self.G = G
        self.time = 0
        self.count = 0 # number of children of root node in the DFS tree
        self.isCV = False # boolean that indicates if given node is a cut-vertex

        # check if input node present in G
        if not self.G.has_node(v):
            raise Exception("Vertex %s not in graph" %str(v))

        # start a DFS on the input vertex as the root
        self.checkCV(v)

    def checkCV(self, v):
        self.marked[v] = True
        self.arr[v] = self.time
        self.time += 1
        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                '''
                If the root node has more than 1 child, it is a cut-vertex.
                There is no need to complete the DFS calls on all its children
                '''
                if self.arr[v] == 0:
                    self.count += 1
                    if self.count > 1:
                        self.isCV = True
                        return
                self.checkCV(w)

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

s = '2'
cv = IsCutVertex(G, s)
print (cv.isCV)
# To check that DFS calls on unnecessary nodes are avoided
print ("Nodes visited = %s" %str(list(cv.marked.keys())))

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
    
        

    
        
