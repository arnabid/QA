import queue

# using BFS
def getSODbfs(graph, root):
	q = queue.Queue()
	q.put((root, 0))
	visited = set()
	visited.add(root)
	ans = 0
	while not q.empty():
		v, l = q.get()
		ans += l
		for w in graph[v]:
			if w not in visited:
				q.put((w, l+1))
				visited.add(w)
	return ans

ans = [0]
level = [0]
visited = set()
def getSODdfs(graph, v):
	ans[0] += level[0]
	level[0] += 1
	visited.add(v)
	for w in graph[v]:
		if w not in visited:
			getSODdfs(graph, w)
	level[0] -= 1


if __name__ == '__main__':
	"""
	graph = {}
	graph[1] = [2,3]
	graph[2] = [1,4,5]
	graph[3] = [1,5,6]
	graph[4] = [2,7]
	graph[5] = [2,3,7,8]
	graph[6] = [3,8]
	graph[7] = [4,5]
	graph[8] = [5,6]

	# get sum of distances to all nodes from start node = 1
	#print (getSODbfs(graph, 1))
	"""

	# dfs method will work only for trees
	graph = {}
	graph[1] = [2,3]
	graph[2] = [4,5]
	graph[3] = [6]
	graph[4] = [2]
	graph[5] = [2,7,8]
	graph[6] = [3]
	graph[7] = [5]
	graph[8] = [5]

	getSODdfs(graph, 1)
	print (ans[0])