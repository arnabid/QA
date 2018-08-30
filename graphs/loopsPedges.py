"""
program to check for self-loops and parallel edges in 
an undirected graph G.
G is assumed to have vertices numbered from 0 ... N-1

reference: https://algs4.cs.princeton.edu/41graph/Cycle.java.html
"""

def hasSelfLoop(G):
	N = len(G)
	for v in range(N):
		for w in G[v]:
			if w == v:
				return True
	return False


# check to see if neighbors of any vertex has duplicate entry 
def hasParallelEdges(G):
	visited = set()
	N = len(G)

	for v in range(N):
		visited.clear()
		for w in G[v]:
			if w in visited:
				return True
			visited.add(w)
	return False
