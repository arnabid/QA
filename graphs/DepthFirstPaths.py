'''
DFS - Depth First Search
'''

class DepthFirstPaths(object):

    def __init__(self, G, s):
        self.marked = {} # Is the vertex visited?
        self.edgeTo = {} # parent in the DFS tree
        self.arr = {} # arrival time at this vertex
        self.dep = {} # backtrack time from this vertex
        self.s = s # source/root of the DFS tree
        self.G = G # graph G on which the processing is done
        self.time = 0
        self.dfs(s)

    def dfs(self, v):
        # starts a DFS traversal in G from s
        self.marked[v] = True
        self.arr[v] = self.time
        self.time += 1

        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                self.edgeTo[w] = v
                self.dfs(w)
        
        self.dep[v] = self.time
        self.time += 1

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
                path.append(v)
                v = self.edgeTo[v]
            path.append(self.s)

        path.reverse()
        return path
            

    
