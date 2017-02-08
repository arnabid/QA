# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:35:35 2016

@author: arnab
"""

"""
Iterative procedures for tree traversals
"""

from collections import Counter

class node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def getChildren(v):
    children = []
    if v.right:
        children.append(v.right)
    if v.left:
        children.append(v.left)
    return children

# returns the maximum sum of path from root to any leaf
def maxsum(root):
    visited = Counter()
    label = Counter()
    
    def dfs(v):
        visited[v] = True
        for w in getChildren(v):
            if not visited.get(w, False):
                dfs(w)
                label[v] = max(label[v], label[w])
        label[v] += v.val
    
    dfs(root)
    return label[root]


def inOrder(root):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            print (root.val),
            root = root.right
        else:
            break


def preOrder(root):
    if root is None:
        return
    
    stack = [root]
    while stack:
        v = stack.pop()
        print (v.val),
        for w in getChildren(v):
            stack.append(w)


def postOrder(root):
    if root is None:
        return
    
    stack, visited = [root], Counter()
    
    while stack:
        v = stack[-1]
        fav = True
        for w in getChildren(v):
            if not visited.get(w, False):
                stack.append(w)
                visited[w] = True
                fav = False
        if fav:
            print (stack.pop().val),

if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    
    root.left.left = node(4)
    root.left.right = node(5)
    
    root.right.left = node(6)
    root.right.left.right = node(-7)
    
    root.right.right = node(8)
    
    #postOrder(root)
    
    #preOrder(root)
    
    #inOrder(root)
    
    print (maxsum(root))
    
    
    
    
    
                