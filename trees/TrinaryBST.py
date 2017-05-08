# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:33:11 2017

@author: arnab
"""

"""
Implement insert and delete in a tri-nary tree. Much like a binary-tree
but with 3 child nodes for each parent instead of two --
with the left node being values < parent, the right node values > parent,
and the middle node values == parent.
"""

def findMin(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root

def insert(root, node):
    if root is None:
        root = node
        return root

    p = None
    c = root
    while c:
        p = c
        if node.val < c.val:
            c = c.left
        elif node.val == c.val:
            c = c.center
        else:
            c = c.right
    
    if node.val < p.val:
        p.left = node
    elif node.val == p.val:
        p.center = node
    else:
        p.right = node
    return root

def delete(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.center:
            root.center = root.center.center
            root.center.center = None
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                temp = findMin(root.right)
                root.val = temp.val
                root.right = delete(root.right, temp.val)
        return root
