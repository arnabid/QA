# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:04:56 2016

@author: arnab
"""

"""
Given a binary tree, flip the tree along the vertical axis
through the root
At each level go through the nodes and swap the lc and rc of each node.
"""
import Queue

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printLevelOrderIterative(root):
    if root is None:
        return

    q = Queue.Queue()
    q.put(root)
    
    while not q.empty():
        v = q.get()
        print (v.val),

        # put the children of v in the queue
        if v.left:
            q.put(v.left)
        if v.right:
            q.put(v.right)

def flipTreeBFS(root):
    # traverse the tree using BFS
    q = Queue.Queue()
    q.put(root)
    
    while not q.empty():
        v = q.get()
        if v.left:
            q.put(v.left)
        if v.right:
            q.put(v.right)
        v.left, v.right = v.right, v.left

def flipTreeDFS(root):
    # traverse the tree using DFS
    if root is None:
        return
    
    def flipTree(v):
        # v.left, v.right = v.right, v.left - this also works :)
        if v.left:
            flipTree(v.left)
        if v.right:
            flipTree(v.right)
        v.left, v.right = v.right, v.left
    
    flipTree(root)

if __name__ == '__main__':
    root = Node(1)
    
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.right = Node(4)
    root.left.left = Node(9)
    root.right.left = Node(5)
    root.right.right = Node(8)
    
    root.left.right.left = Node(6)
    root.right.left.right = Node(7)
    
    printLevelOrderIterative(root)
    print ("")
    
    # flip the tree
    #flipTreeBFS(root)
    flipTreeDFS(root)
    
    printLevelOrderIterative(root)
    