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