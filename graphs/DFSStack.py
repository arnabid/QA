from BuildUGraph import BuildUGraph
'''
DFS implementation using an explicit stack/without recursion
Here a list is used as a stack, addition and removal from the end of the list
'''

class DFSStack(object):
    def __init__(self,G,s):
        self.G = G
        self.s = s # source of the DFS tree
        self.marked = {}
        self.edgeTo = {}
        self.iterator = {}
        # to be able to iterate over each adjacency list, keeping track of which
        # vertex in each adjacency list needs to be explored next
        for node in G.nodes():
            self.iterator[node] = G.adj(node)

        # start DFS from given source s
        self.DFS(s)

    def DFS(self,s):
        stack = []
        arr = {}
        self.marked[s] = True
        stack.append(s) # push s onto the stack
        time = 0
        arr[s] = time
        time += 1 

        while stack:
            v = stack[-1] # peek at the top element in the stack
            if self.iterator[v]:
                w = self.iterator[v].pop() # removes and returns the last item
                if not self.marked.get(w,False):
                    self.marked[w] = True
                    self.edgeTo[w] = v
                    stack.append(w)
                    arr[w] = time
                    time += 1
            else:
                # backtrack here
                stack.pop()
            
        print (arr)

    def hasPathTo(self, v):
        # returns a boolean to indicate if there exists a path
        # from source s to vertex v in G
        return self.marked.get(v, False)

    def pathTo(self, v):
        # returns a list of nodes to denote a path from source s to vertex v
        path = []
        if not self.hasPathTo(v):
            return path
        else:
            while v != self.s:
                path.insert(0,v)
                v = self.edgeTo[v]
            path.insert(0,self.s)

        return path

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildUGraph(inputfilepath)
G = bg.buildUGraph() # returns a graph object

dfs = DFSStack(G,'a')
print (dfs.pathTo('d'))
