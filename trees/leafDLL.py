# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution():
	def __init__(self):
		self.prev = Node('dummy')
		self.cur = None
		self.head = self.prev

	def extractLeafList(self, root):
		if root is None:
			return None

		if root.left is None and root.right is None:
			self.cur = root
			self.cur.left = self.prev
			self.prev.right = self.cur
			self.prev = self.cur
			root = None
			return root

		if root.left:
			root.left = self.extractLeafList(root.left)

		if root.right:
			root.right = self.extractLeafList(root.right)

		return root

	# Utility function for printing tree in InOrder
	def printInorder(self, root):
	    if root:
	        self.printInorder(root.left)
	        print (root.data, end=" ")
	        self.printInorder(root.right)
	 
	 
	def printList(self, head):
	    while head:
	        print (head.data, end=" ")
	        head = head.right


if __name__ == '__main__':
	# Driver program to test above function
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(6)
	root.left.left.left = Node(7)
	root.left.left.right = Node(8)
	root.right.right.left = Node(9)
	root.right.right.right = Node(10)


	sol = Solution()
	 
	print ("Inorder traversal of given tree is:")
	sol.printInorder(root)
	 
	root = sol.extractLeafList(root)
	 
	print ("\nExtract Double Linked List is:")
	sol.printList(sol.head.right)
	 
	print ("\nInorder traversal of modified tree is:")
	sol.printInorder(root)
	print ("")