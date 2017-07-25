# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:41:26 2017

@author: arnab
"""

class TreeNode(object):
    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.val = key

"""
returns key if key is present in BST; else returns predecessor to key in BST
"""
def searchPD(root, key):
    if root is None:
        return None
    pd = None
    while root:
        if root.val == key:
            return key
        elif root.val < key:
            pd = root.val
            root = root.right
        else:
            root = root.left
    return pd


"""
returns key if key is present in BST; else returns successor to key in BST
"""
def searchSC(root, key):
    if root is None:
        return None
    
    sc = None
    while root:
        if root.val == key:
            return key
        elif root.val < key:
            root = root.right
        else:
            sc = root.val
            root = root.left
    return sc

"""
inserts node in BST rooted at root
"""
def insert(root, node):
    if root is None:
        root = node
        return root
    p = None
    current = root
    while current:
        p = current
        if node.val <= current.val:
            current = current.left
        else:
            current = current.right
    if node.val <= p.val:
        p.left = node
    else:
        p.right = node
    return root


if __name__ == '__main__':
    arr = [2,2,4,5,6]

    root = None
    for item in arr:
        root = insert(root, TreeNode(item))

    print (searchPD(root, 9))
