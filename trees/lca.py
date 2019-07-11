# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
solution 1
"""
class Solution(object):
    def findPath(self, root, x, path):
        if root:
            path.append(root)
            if root == x:
                return True
            if self.findPath(root.left, x, path):
                return True
            if self.findPath(root.right, x, path):
                return True
            path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        p1, p2 = [], []
        self.findPath(root, p, p1)
        self.findPath(root, q, p2)
        
        """
        find the lca node of p and q
        i, j = 0,0
        n1, n2 = len(p1), len(p2)
        while i < n1 and j < n2 and p1[i] == p2[j]:
            i += 1
            j += 1
        return p1[i-1]
        """

        """
        return the distance between 2 nodes and p and q
        """
        n1, n2 = len(p1), len(p2)
        i, j = 0, 0
        while i < n1 and j < n2 and p1[i] == p2[j]:
            i += 1
            j += 1
        return n1 + n2 - 2*i


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        if root == p or root == q:
            return root
        lca = self.lowestCommonAncestor(root.left, p , q)
        rca = self.lowestCommonAncestor(root.right, p, q)
        if lca and rca:
            return root
        elif lca:
            return lca
        elif rca:
            return rca
        return None

        