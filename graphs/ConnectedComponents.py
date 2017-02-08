"""
Find all the connected components in a graph G
"""
import Queue
from collections import Counter
class ConnectedComponents(object):

    def __init__(self, G):
        self.label = {}
        self.count = 0 # number of connected components in G
        self.findComponents(G)

    def findComponents(self, G):
        # finds all the connected components in G
        for node in G:
            self.label[node] = 0

        # Start BFS from any node
        for node in self.label:
            if self.label[node] == 0:
                # start a BFS on this node
                self.count += 1
                q = Queue.Queue()
                q.put(node)
                self.label[node] = self.count
                while not q.empty():
                    v = q.get()
                    for w in G[v]:
                        if self.label[w] == 0:
                            q.put(w)
                            self.label[w] = self.label[v]
        
    def isSameComponent(self, u, v):
        # returns a boolean to indicate if nodes u and v are in the same component in G
        if u not in self.label or v not in self.label:
            return KeyError("Invalid input: node(s) not present in graph")
        return self.label.get(u) == self.label.get(v)

    def numComponents(self):
        # returns the number of components in G
        return self.count

if __name__ == '__main__':
    G = Counter()
    G['a'] = ['b','c']
    G['b'] = ['a','c']
    G['c'] = ['b','a']
    G['d'] = []
    G['e'] = []
    cc = ConnectedComponents(G)
    print (cc.numComponents())
    print (cc.label)
    print (cc.isSameComponent('a','f'))