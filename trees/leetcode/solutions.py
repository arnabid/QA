# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:01:22 2017

@author: arnab
"""

"""
Leetcode questions - Trees
"""
from typing import List

import math
def pathInZigZagTree(self, label: int) -> List[int]:
    # if the initial label is in an even row, replace it with the
    # original(unswapped) label
    r = math.floor(math.log(label, 2) + 1) # row number
    if r % 2 == 0:
        l, e = 2**(r-1), 2**r-1 # lower and upper limits of row
        d = label - l
        label = e - d
    # form the result array with no swapping
    ans = [label]
    while label != 1:
        label = label // 2
        ans.append(label)
        
    # change the swapped elements in the array
    # starting index idx
    idx = len(ans) % 2
    while idx < len(ans):
        label = ans[idx]
        r = math.floor(math.log(label, 2) + 1)
        l, e = 2**(r-1), 2**r-1
        ans[idx] = e - label + l
        idx += 2
    return ans[::-1]

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

"""
Flatten binary tree to linked list
Reference: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description
"""

def join(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    t = l1
    while t.right:
        t = t.right
    t.right = l2
    return l1

def flatten2(root):
    if root:
        lft = flatten2(root.left)
        rft = flatten2(root.right)
        root.right = join(lft, rft)
        root.left = None
    return root

def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    root = flatten2(root)

"""
count the number of nodes in a complete binary tree
reference: https://leetcode.com/problems/count-complete-tree-nodes/#/description
"""

def height(root):
    if root is None:
        return - 1
    return 1 + height(root.left)

"""
iterative solution
"""
def countNodesI(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    n, h = 0, height(root)
    while root:
        if height(root.right) == h - 1:
            n += 1 << h
            root = root.right
        else:
            n += 1 << h-1
            root = root.left
        h -= 1
    return n

"""
recursive solution
"""
def countNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    h = height(root)
    if h < 0:
        return 0
    else:
        if height(root.right) == h - 1:
            return (1 << h) + countNodes(root.right)
        else:
            return (1 << h - 1) + countNodes(root.left)
