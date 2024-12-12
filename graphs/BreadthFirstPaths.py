import queue

'''
Breadth first search to find paths in a graph
'''

class BreadthFirstPaths(object):

    def __init__(self, G, s):
        self.parent = {} # parent of a vertex in BFS tree
        self.label = {} # distance label of each vertex
        self.s = s # source vertex
        self.bfs(G,s)

    def bfs(self, G, s):
        q = queue.Queue()
        q.put(s) # mark the source and put it in the queue
        self.label[s] = 0
        while not q.empty():
            v = q.get()
            for w in G.adj(v):
                if not (w in self.label): # vertex w has not been discovered
                    q.put(w)
                    self.parent[w] = v
                    self.label[w] = self.label[v] + 1

    def hasPathTo(self, v):
        # returns a boolean to indicate if there exists a
        # path from source s to vertex v in G
        return (v in self.label)

    def shortestDistance(self, v):
        # returns the length of the shortest path from source s to v
        return self.label.get(v, -1)

    def pathTo(self, v):
        # returns a list of nodes in shortest path
        # from source s to vertex v in G
        path = []

        if self.hasPathTo(v):
            while v != self.s:
                path.append(v)
                v = self.parent[v]
            path.append(self.s)

        path.reverse()
        return path
