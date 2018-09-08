
"""
find all nodes at distance k from the root in a binary tree
using BFS (3 variations)/ DFS
"""

from collections import deque

# A binary tree node 
class Node:
	# A constructor to create a new node
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def nodesatK1(root, k):
	q = deque([root])
	for _d in range(k):
		for _c in range(len(q)):
			v = q.popleft()
			if v.left:
				q.append(v.left)
			if v.right:
				q.append(v.right)

	return [node.val for node in q]

def nodesatK2(root, k):
	q = deque([(root, 0)])
	while q:
		if q[0][1] == k:
			return [v.val for v, level in q]
		v, level = q.popleft()
		if v.left:
			q.append((v.left, level+1))
		if v.right:
			q.append((v.right, level+1))

	return []

def nodesatK3(root, k):
	clevel = [root]
	for _ in range(k):
		nlevel = []
		for v in clevel:
			if v.left:
				nlevel.append(v.left)
			if v.right:
				nlevel.append(v.right)
		clevel = nlevel
		if not clevel:
			break
	return [node.val for node in clevel]



"""
Annote parent of each node in a binary tree
using BFS/DFS
"""
def annotateParent1(root, par = None):
	if root:
		root.par = par
		annotateParent1(root.left, root)
		annotateParent1(root.right, root)

def annotateParent2(root):
	q = deque([root])
	root.par = None
	while q:
		v = q.popleft()
		if v.left:
			q.append(v.left)
			v.left.par = v
		if v.right:
			q.append(v.right)
			v.right.par = v


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    k = 10000
    print (nodesatK3(root, k))
    root.par = None
    print (root.par)

