"""
Find nodes at distance k from a given node
1. convert the tree to a undirected graph
2. do a BFS traversal from target node
"""

from collections import defaultdict
import queue

# A binary tree node 
class Node:
	# A constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class KDistanceNodes:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def createGraph(self, root):
        if root.left:
            self.graph[root].add(root.left)
            self.graph[root.left].add(root)
            self.createGraph(root.left)
        if root.right:
            self.graph[root].add(root.right)
            self.graph[root.right].add(root)
            self.createGraph(root.right)
        
    def BFS(self, root, target, k):
        q = queue.Queue()
        q.put(target)
        visited = set()
        visited.add(target)
        
        for _ in range(k):
            for i in range(q.qsize()):
                node = q.get()
                for w in self.graph[node]:
                    if w not in visited:
                        q.put(w)
                        visited.add(w)
        while not q.empty():
            print (q.get().data)


from collections import deque
class Solution(object):
    def findDistanceK(self, root, n1, k):
        # Do DFS
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        # start BFS
        q = deque([(n1, 0)])
        visited = {n1}
        while q:
            if q[0][1] == k:
                return [node.val for node, d in q]
            node, d = q.popleft()
            for w in (node.par, node.left, node.right):
                if w and w not in visited:
                    q.append((w, d+1))
                    visited.add(w)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    target = root.left.left
    sol = KDistanceNodes()
    sol.createGraph(root)
    sol.BFS(root, target, 2)

