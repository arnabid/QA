
stack = []
visited = set()

def dfs(v):
	stack.append(v)
	print ("node = {}, stack = {}".format(v,stack))
	visited.add(v)
	for w in graph[v]:
		if w not in visited:
			dfs(w)
	stack.pop()


if __name__ == '__main__':
	graph = {}
	graph[1] = [2,5]
	graph[2] = [3,4]
	graph[3] = []
	graph[4] = []
	graph[5] = [4]
	dfs(1)