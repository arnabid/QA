import queue

'''
Breadth first search to find all paths in a graph
'''

class BreadthFirstPaths(object):

    def __init__(self, G, s):
        self.s = s # source vertex
        self.pathTo = {} # parent of a vertex in BFS tree

    def bfs(self, G, s):
        q = queue.Queue()
        q.put(s) # mark the source and put it in the queue
        self.pathTo[s] = [s]
        while not q.empty():
            v = q.get()
            for w in G[v]:
                if not (w in self.pathTo): # vertex w has not been discovered
                    q.put(w)
                    self.pathTo[w] = self.pathTo.get(v) + [w]

    def hasPathTo(self, v):
        # returns a boolean to indicate if there exists a
        # path from source s to vertex v in G
        return (v in self.pathTo)

    def shortestDistance(self, v):
        # returns the length of the shortest path from source s to v
        return len(self.pathTo.get(v, [])) - 1
    
    
if __name__ == '__main__':
    graph = {}
    graph['a'] = ['b', 'g']
    graph['b'] = ['c', 'a', 'd']
    graph['c'] = ['e', 'b']
    graph['d'] = ['b', 'e', 'f']
    graph['e'] = ['g', 'c', 'd']
    graph['f'] = ['g', 'd']
    graph['g'] = ['a', 'f', 'e']
    
    bfs_obj = BreadthFirstPaths(graph, 'a')
    bfs_obj.bfs(graph, bfs_obj.s)
    
    print(bfs_obj.pathTo['a'])
    print(bfs_obj.pathTo['b'])
    print(bfs_obj.pathTo['c'])
    print(bfs_obj.pathTo['d'])
    print(bfs_obj.pathTo['e'])
    print(bfs_obj.pathTo['f'])
    print(bfs_obj.pathTo['g'])
    
    print(bfs_obj.shortestDistance('a'))
    print(bfs_obj.shortestDistance('b'))
    print(bfs_obj.shortestDistance('c'))
    print(bfs_obj.shortestDistance('d'))
    print(bfs_obj.shortestDistance('e'))
    print(bfs_obj.shortestDistance('f'))
    print(bfs_obj.shortestDistance('g'))
        
