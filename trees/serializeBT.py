# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:03:46 2016

@author: arnab
"""

""" Serialize and De-serialize a given BT """

import Queue

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#def serializeTree(root, tlist):
#    if root is None:
#        tlist.append(-1)
#        return
#
#    tlist.append(root.val)
#    serializeTree(root.left, tlist)
#    serializeTree(root.right, tlist)
#
#def deserialize(root1, tlist):
#    if len(tlist) == 0:
#        return None
#    elif tlist[0] == -1:
#        tlist.pop(0)
#        return None
#
#    root1 = Node(tlist.pop(0))
#    root1.left = deserialize(root1.left, tlist)
#    root1.right = deserialize(root1.right, tlist)
#    return root1

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
        return self.arr
        

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
