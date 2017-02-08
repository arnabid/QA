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

def serializeTree(root, tlist):
    if root is None:
        tlist.append(-1)
        return

    tlist.append(root.val)
    serializeTree(root.left, tlist)
    serializeTree(root.right, tlist)

def deserialize(root1, tlist):
    if len(tlist) == 0:
        return None
    elif tlist[0] == -1:
        tlist.pop(0)
        return None

    root1 = Node(tlist.pop(0))
    root1.left = deserialize(root1.left, tlist)
    root1.right = deserialize(root1.right, tlist)
    return root1
           
#def serializeTree(root):
#    if root is None:
#        return ""
#
#    s = ""
#    q = Queue.Queue()
#    q.put(root)
#    
#    while not q.empty():
#        root = q.get()
#        if root != '$':
#            s += str(root.val)
#        else:
#            s += '$'
#            continue
#
#        if root.left is not None:
#            q.put(root.left)
#        else:
#            q.put('$')
#
#        if root.right is not None:
#            q.put(root.right)
#        else:
#            q.put('$')
#    return s

def printlevelOrder(root):
    if root is None:
        return []
    
    a = []
    q = Queue.Queue()
    q.put(root)
    
    while not q.empty():
        root = q.get()
        a.append(root.val)
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    
    print (a)

#def buildTree(s):
#    # returns the root of the tree
#    n = len(s)
#    
#    # empty string
#    if n == 0:
#        return None
#    
#    root = Node(s[0])
#    troot = root
#    q = Queue.Queue()
#    q.put(root)
#    
#    i = 0
#    while not q.empty():
#        root = q.get()
#        if root is None:
#            i += 1
#            continue
#        else:
#            if 2*i+1 < n and s[2*i+1] != '$':
#                root.left = Node(s[2*i+1])
#            else:
#                root.left = None
#            q.put(root.left)
#
#            if 2*i+2 < n and s[2*i+2] != '$':
#                root.right = Node(s[2*i+2])
#            else:
#                root.right = None
#            q.put(root.right)
#            i += 1
#    
#    return troot

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.left = Node(6)
    root.right.right.right = Node(7)
    
    tlist = []
    serializeTree(root, tlist)
    print (tlist)
    
    root1 = None
    root1 = deserialize(root1,tlist)
    #print (root)
    
    
    
    #s = serializeTree(root)
    #print (s)
    #s = "123$$45$$$$6$7"
    #root = buildTree(s)
    #print (root.right.left.val)
    #print (root.left.left is None)
    printlevelOrder(root1)
