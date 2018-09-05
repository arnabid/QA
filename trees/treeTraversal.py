"""
N-ary Tree Level Order Traversal
reference: https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
"""
def levelOrder(self, root):   
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    if root is None:return []
    res = []
    stack = [root]
    while stack:
        temp = []
        next_stack = []
        for node in stack:
            temp.append(node.val)
            for child in node.children:
                next_stack.append(child)
        stack = next_stack
        res.append(temp)
    return res
