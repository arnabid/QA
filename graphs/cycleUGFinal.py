"""
detect cycle in an undirected graph G

reference: https://algs4.cs.princeton.edu/41graph/Cycle.java.html
"""
class Solution:
	def __init__(self):
		self.cycleExists = False
		self.edgeTo = {}
		self.visited = set()
		self.cycle = []

	def getCycle(self):
		return self.cycle

	def hasCycle(self, G):

		def dfs(u, v):
			self.visited.add(v)
			self.edgeTo[v] = u
			if self.cycleExists:
				return
			for w in G[v]:
				if w not in visited:
					dfs(v,w)
				else:
					if w != u:
						self.cycleExists = True
						while edgeTo[v] != w:
							self.cycle.append(v)
							v = self.edgeTo[v]
						self.cycle.append(w)
						self.cycle.append(v)

		N = len(G)
		for v in range(N):
			if v not in self.visited:
				dfs(-1,v)
		return self.cycleExists
