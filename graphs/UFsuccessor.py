'''
Successor with delete. 
Given a set of N integers S={0,1,...,N} and a sequence of
requests of the following form:
Remove x from S
Find the successor of x: the smallest y in S such that y>=x.
Design a data type so that all operations (except construction) 
should take logarithmic time or better.
'''

'''

remove(x):
if rem[x+1]:
successor[x] = find(x+1)
else:
successor[x] = x+1

find(x):
if rem[x]:
s = find(x+1)
successor[x] = s
return s

return x

Take care of the corner case

'''

class UFsuccessor(object):
    def __init__(self, N):
        self.id = {} # link to parent
        self.sz = {} # rank of each node
        self.max = {} # largest element in the connected component
        self.N = N # number of elements in the set {0,1,2,...,N-1}

        #initialize the id and sz arrays
        for i in range(0,N):
            self.id[i] = i
            self.sz[i] = 1
            self.max[i] = i

    def find(self, x):
        # returns the root of the component which contains element x
        if x not in self.id:
            raise Exception("Element %s not present in S" % str(x))
        while x != self.id[x]:
            if self.id[x]== -1:
                return -1
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x
    
    def remove(self,x):
        # removes the element x from S
        # does a union(x,x+1) based on rank and updates the max table
    
        # check if x is already removed
        if self.id[x] != x:
            raise Exception("Element %s already removed from S" % str(x))
        
        # handle the special case of removing Nth element in S
        if x == self.N-1:
            self.id[x] = -1
            return
        
        # do a Union(x,x+1)
        rootl = self.find(x) # finds the root of x
        rootr = self.find(x+1) # finds the root of x+1
        
        if rootl == rootr:
            return # this should never happen
        
        # do union by rank and also maintain the max element in the
        # resultant component
        if self.sz[rootl] <= self.sz[rootr]:
            self.id[rootl] = rootr
            self.sz[rootr] += self.sz[rootl]
            self.max[rootr] = max(self.max[rootr], self.max[rootl])
        else:
            self.id[rootr] = rootl
            self.sz[rootl] += self.sz[rootr]
            self.max[rootl] = max(self.max[rootl], self.max[rootr])
        
    
    def successor(self,x):
        # returns the smallest element y in S such that y >= x
        # return -1 if such an element does not exist
        root = self.find(x)
        if root == -1:
            return -1
        
        return self.max[root]

if __name__ == '__main__':
    uf = UFsuccessor(11)
    print (uf.successor(7)) # return 7
    uf.remove(7)
    uf.remove(8)
    uf.remove(10)
    uf.remove(9)
    #print (uf.successor(3)) # return 5
    #print (uf.successor(7)) # return -1
    
    