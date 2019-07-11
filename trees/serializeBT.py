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

    def serializeBFS(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: List
        """
        # return empty list is root is None
        if root is None:
            return

        stack = [root]
        while stack:
            nlevel = []
            nlEmpty = True
            for node in stack:
                if node:
                    self.arr.append(node.val)
                    if node.left or node.right:
                        nlEmpty = False
                    nlevel.append(node.left)
                    nlevel.append(node.right)
                else:
                    self.arr.append(None)
            if not nlEmpty:
                stack = nlevel
            else:
                stack = []

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

# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.right.left = Node(6)

    codec = Codec()
    codec.serializeBFS(root)
    print (codec.arr)

