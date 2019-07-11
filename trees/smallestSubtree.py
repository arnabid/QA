"""

"""
# A class that represents an individual node in a Binary Tree
class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def dfs(root, stack, curr_mxdepth, curr_depth, hmap):
	if root:
		stack.append(root)
		curr_depth [0] += 1

		if curr_depth[0] > curr_mxdepth[0]:
			hmap["deep"] = [[x for x in stack]]
			curr_mxdepth[0] = curr_depth[0]
		elif curr_depth[0] == curr_mxdepth[0]:
			hmap["deep"].append([x for x in stack])

		dfs(root.left, stack, curr_mxdepth, curr_depth, hmap)
		dfs(root.right, stack, curr_mxdepth, curr_depth, hmap)
		stack.pop()
		curr_depth[0] -= 1


if __name__ == '__main__':
    root = Node(1)
    
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    
    root.right = Node(5)
    #root.right.left = Node(6)
    #root.right.left.right = Node(7)
    
    stack, hmap = [], {}
    curr_mxdepth, curr_depth = [-1], [-1]
    dfs(root, stack, curr_mxdepth, curr_depth, hmap)

    # find the lowest common ancestor
    if len(hmap["deep"]) == 1:
    	print (hmap["deep"][0][-1].val)
    else:
    	isDone = False
    	l = hmap["deep"]
    	i = 0
    	while i < len(l[0]):
    		node = l[0][i]
    		for j in range(1,len(l)):
    			if l[j][i] != node:
    				isDone = True
    				break
    		if isDone: break
    		i += 1
    	print ("ans is {}".format(l[0][i-1].val))
