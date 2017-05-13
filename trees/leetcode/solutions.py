# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:01:22 2017

@author: arnab
"""

"""
Leetcode questions - Trees
"""

"""
Sum of left leaves
reference: https://leetcode.com/problems/sum-of-left-leaves/#/description
"""
def getTotal(root, total, isLC):
    if root:
        if isLC:
            if root.left is None and root.right is None:
                total[0] += root.val
        getTotal(root.left, total, True)
        getTotal(root.right, total, False)

def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    total = [0]
    getTotal(root, total, False)
    return total[0]


"""
Convert BST to greater tree
reference: https://leetcode.com/problems/convert-bst-to-greater-tree/#/description
"""

def traverse(root, count):
    if root:
        traverse(root.right, count)
        root.val += count[0]
        count[0] = root.val
        traverse(root.left, count)

def convertBST(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    count = [0]
    traverse(root, count)
    return root

"""
Binary tree tilt
reference: https://leetcode.com/problems/binary-tree-tilt/#/description
"""

def findSum(root, tilt):
    if root is None:
        return 0
    lSum = findSum(root.left, tilt)
    rSum = findSum(root.right, tilt)
    tilt[0] += abs(lSum-rSum)
    return lSum + rSum + root.val

def findTilt(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    tilt = [0]
    findSum(root, tilt)
    return tilt[0]

"""
Binary Tree Right Side View
Reference: https://leetcode.com/problems/binary-tree-right-side-view/#/description
"""

"""
solution 1
"""
def rsvTraverse(root, nodes, currDepth):
    if root is None:
        return
    if len(nodes) == currDepth:
        nodes.append(root.val)
    traverse(root.right, nodes, currDepth+1)
    traverse(root.left, nodes, currDepth+1)

def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    nodes = []
    rsvTraverse(root, nodes, 0)
    return nodes


"""
solution 2
"""
def rightSideView2(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    nodes = [root.val]
    level = [root]
    nextlevel = []
    while True:
        for node in level:
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        if nextlevel:
            nodes.append(nextlevel[-1].val)
            level = nextlevel
            nextlevel = []
        else:
            break
    return nodes



