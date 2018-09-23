"""
max depth of a BT - maximum number of hops to a leaf node
"""
def mxDepth(root):
	if root is None: return -1
	ld = mxDepth(root.left)
	rd = mxDepth(root.right)
	return max(ld, rd) + 1

"""
min depth of a BT - minimum number of hops to a leaf node
"""
def mnDepth(root):
	if root.left is None and root.right is None: return 0
	ld, rd = float('inf'), float('inf')
	if root.left:
		ld = mnDepth(root.left)
	if root.right:
		rd = mnDepth(root.right)
	return min(ld, rd) + 1