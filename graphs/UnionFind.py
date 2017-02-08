'''

Dynamic connectivity problem: a data structure that efficiently supports
commands of the following form on N objects:
1. connect 2 pbjects
2. are objects x and y connected?


Union-Find class; union based on rank
and find() also does path compression.
The path compression step reduces the height of a tree by 1/2
TODO: Finish union by height
'''

class UF(object):
    def __init__(self, sites):
        self.id = {} # link to parent
        self.sz = {} # rank of each node
        self.max = {} # largest element in the connected component
        self.count = len(sites) # number of components

        #initialize the id and sz arrays
        for i in sites:
            self.id[i] = i
            self.sz[i] = 1
            self.max[i] = i

    def get_components(self):
        # returns the components
        components = {}
        for node in self.id.keys():
            r = self.find(node) # finds the root of this node
            if r not in components: # O(1) operation
                components[r] = [node]
            else:
                components[r].append(node)

        return list(components.values())
            

    def count(self):
        # returns the number of components
        return self.count

    def connected(self, p, q):
        # returns a boolean to indicate if nodes p and q are connected
        return self.find(p) == self.find(q)

    def find(self, p):
        # returns the root of the component in which node p lies
        if not p in self.id:
            raise Exception("Node %s not present" % str(p))
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def findmax(self, p):
        # returns the maximum element in the component which contains p
        return self.max[self.find(p)]

    def union(self, p, q):
        # joins the 2 components in which nodes p and q lie
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot: # do nothing
            return
        # do union by rank and also maintain the max element in the
        # resultant component
        if self.sz[proot] < self.sz[qroot]:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]
            self.max[qroot] = max(self.max[qroot], self.max[proot])
        else:
            self.id[qroot] = proot
            self.sz[proot] += self.sz[qroot]
            self.max[proot] = max(self.max[proot], self.max[qroot])
        self.count -= 1

# testing
if __name__ == '__main__':
    nodes = [1,2,3,4,5,6,7,8]
    uf = UF(nodes)
    uf.union(2,3)
    uf.union(8,7)
    uf.union(1,4)
    uf.union(5,1)
    uf.union(4,5)
    uf.union(4,6)
    uf.union(6,5)
    print (uf.get_components())
    print (uf.connected(2,6))
    print (uf.count)
    print (uf.findmax(7))
    print (uf.findmax(5))
