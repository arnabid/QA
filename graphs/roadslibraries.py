
"""
reference: https://www.hackerrank.com/challenges/torque-and-development
"""


from collections import Counter

class UF(object):
    def __init__(self, n):
        self.id = {} # link to parent
        self.sz = Counter() # maintains rank of each node
        self.count = n # number of components

        #initialize the id and sz arrays
        for i in xrange(1,n+1):
            self.id[i] = i
            self.sz[i] = 1

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

    def union(self, p, q):
        # joins the 2 components in which nodes p and q lie
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot: # do nothing
            return

        # do union by rank
        if self.sz[proot] < self.sz[qroot]:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]
        else:
            self.id[qroot] = proot
            self.sz[proot] += self.sz[qroot]
        self.count -= 1

if __name__ == '__main__':

    q = int(raw_input().strip())
    for _ in xrange(q):
        n,m,cl,cr = map(int, raw_input().strip().split(" "))
        uf = UF(n)
        for edge in xrange(m):
            u, v = map(int, raw_input().strip().split(" "))
            uf.union(u,v)

        # array having the number of nodes in each component
        nelements = []
        for key in uf.id:
            if uf.id[key] == key:
                nelements.append(uf.sz[key])

        ans = 0
        for cn in nelements:
            tempans = cn*cl
            for i in xrange(cn):
                tempans = min(tempans, i*cr + (cn - i)*cl)
            ans += tempans
        print (ans)
