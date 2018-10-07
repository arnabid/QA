"""
serialize and deserialize a N-ary tree
reference: https://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/
"""

class Node(object):
    def __init__(self, key):
    	self.children = []
    	self.val = key


# global variables
arr = []
index = [0]

# serialize the N-ary tree
def sr(root):
	arr.append(root.val)
	for child in root.children:
		sr(child)
	arr.append(")")


# de-serialize the N-ary tree
def ds():
	if arr[index[0]] == ')':
		return None
	root = Node(arr[index[0]])
	while True:
		index[0] += 1
		child = ds()
		if child:
			root.children.append(child)
		else:
			return root


if __name__ == '__main__':
	# Build the tree
	root = Node('A')
	nodeB = Node('B')
	nodeC = Node('C')
	nodeD = Node('D')
	nodeE = Node('E')
	nodeF = Node('F')
	nodeG = Node('G')
	nodeH = Node('H')
	nodeI = Node('I')
	nodeJ = Node('J')
	nodeK = Node('K')
	root.children.extend([nodeB, nodeC, nodeD])
	nodeB.children.extend([nodeE, nodeF])
	nodeF.children.append(nodeK)
	nodeD.children.extend([nodeG, nodeH, nodeI, nodeJ])

	# serialize
	sr(root)
	print (arr)

	# de-serialize
	droot = ds()

	# verify the tree structure
	stack = [droot]
	while stack:
		nlevel = []
		for node in stack:
			print (node.val, end=",")
			for child in node.children:
				nlevel.append(child)
		stack = nlevel
		print ("")
	print (index)

