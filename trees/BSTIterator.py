# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:31:37 2017

@author: arnab
"""

"""
Build a BST iterator
reference: https://leetcode.com/problems/binary-search-tree-iterator/description/
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.buildStack(root)
    
    def buildStack(self, x):
        while x:
            self.stack.append(x)
            x = x.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0
        

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.buildStack(node.right)
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())