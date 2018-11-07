"""
program to implement the quick-find algorithm
to merge components containing p and q, change all entries whose id equals id[p] to id[q]
union operation results in connected components that are trees with height at most 1 at any given instant


Side note: how to verify that the connected components are all trees with height atmost 1 in linear time O(N)?
=========

Time complexity:
initialization - O(N)
union - O(N)
connected - O(1)
"""

class QuickFind():
	def __init__(self, N):
		self.id = [i for i in range(N)]

	def connected(self, p, q):
		return self.id[p] == self.id[q]

	def union(self, p, q):
		idp = self.id[p]
		idq = self.id[q]
		if idp != idq:
			for i in range(len(self.id)):
				if self.id[i] == idp:
					self.id[i] = idq

	def verifyTree(self):
		# idea is that for each entry in id; id[id[i]] = id[i] holds
		for i in range(len(self.id)):
			if self.id[self.id[i]] != self.id[i]: return False
		return True

if __name__ == '__main__':
    qf = QuickFind(9)
    qf.union(2,3)
    qf.union(8,7)
    qf.union(1,4)
    qf.union(5,1)
    qf.union(4,5)
    qf.union(4,6)
    qf.union(6,5)
    print (qf.connected(2,5))
    print (qf.connected(5,2))
    print (qf.connected(0,4))
    print (qf.connected(4,7))
    print (qf.connected(1,5))
    print ("Verify = {}".format(qf.verifyTree()))
    print (qf.id)
