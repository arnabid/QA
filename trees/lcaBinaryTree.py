"""
Find the lowest common ancestor of 2 nodes in a binary tree
"""

# A binary tree node 
class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LCASolution():
    def findPath(self, root, x, path):
        if root:
            path.append(root)
            if root== x:
                return True
            if self.findPath(root.left, x, path):
                return True
            if self.findPath(root.right, x, path):
                return True
            path.pop()
            return False

    def lowestCommonAncestor(self, root, x, y):
        if root is None:
            return None
        p1, p2 = [], []
        self.findPath(root, x, p1)
        self.findPath(root, y, p2)
        
        i, j = 0,0
        while i < len(p1) and j < len(p2) and p1[i].data == p2[j].data:
            i += 1
            j += 1
        return p1[i-1].data

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    x = root.left.left
    y = root.right
    sol = LCASolution()
    print (sol.lowestCommonAncestor(root, x, y))
