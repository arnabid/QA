# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Find the node in a tree whose value matches a target value
Assume the values of the nodes of the tree are unique.
"""
def getTargetCopy(root: TreeNode, target: int) -> TreeNode:
    def dfs(node):
        if node:
            if node.val == target:
                return node
            return dfs(node.left) or dfs(node.right)
    return dfs(root)
