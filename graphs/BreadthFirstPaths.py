import queue

'''
Breadth first search to find paths in a graph
'''

class BreadthFirstPaths(object):

    def __init__(self, G, s):
        self.marked = {} # Is a shortest path to this vertex known?
        self.edgeTo = {} # last vertex on known path to this vertex
        self.label = {} # label of each vertex
        self.s = s # source
        self.bfs(G,s)

    def bfs(self, G, s):
        q = queue.Queue()
        q.put(s) # mark the source and put it in the queue
        self.marked[s] = True
        self.label[s] = 0
        while not q.empty():
            v = q.get()
            for w in G.adj(v):
                if not self.marked.get(w, False):
                    q.put(w)
                    self.marked[w] = True
                    self.edgeTo[w] = v
                    self.label[w] = self.label[v] + 1

    def hasPathTo(self, v):
        # returns a boolean to indicate if there exists a
        # path from source s to vertex v in G
        return self.marked.get(v, False)

    def shortestDistance(self, v):
        # returns the length of the shortest path from source s to v
        return self.label.get(v, -1)

    def pathTo(self, v):
        # returns a list of nodes to denote a shortest path
        # from source s to vertex v in G
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

