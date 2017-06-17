# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:03:46 2016

@author: arnab
"""

""" Serialize and De-serialize a given BT """

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Codec:
    
    def __init__(self):
        self.arr = []
        self.index = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: List
        """
        if root is None:
            self.arr.append("#")
            return
        self.arr.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)
        

    def deserialize(self):
        """Decodes your encoded data to tree.
 
        :rtype: TreeNode
        """
        #print (self.k)
        val = self.arr[self.index]
        self.index += 1
        if val == "#":
            return None
        root = Node(val)
        root.left = self.deserialize()
        root.right = self.deserialize()
        return root
