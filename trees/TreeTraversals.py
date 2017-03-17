# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:32:44 2016

@author: arnab
"""

import Queue
from collections import Counter

# Python program for tree traversals
# TODO: tree traversals w/o recursion and w/o explicit stacks
# Study Morris traversals - binary threaded trees

# A class that represents an individual node in a Binary Tree
class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def traverseSpiral(root):
    if root is None:
        return
    
    even, odd = [root], []
    
    while True:
        while even:
            node = even.pop()
            print (node.val),
            if node.right:
                odd.append(node.right)
            if node.left:
                odd.append(node.left)
        print ('')
        
        if not odd:
            break
        
        while odd:
            node = odd.pop()
            print (node.val),
            if node.left:
                even.append(node.left)
            if node.right:
                even.append(node.right)
        print ('')
        
        if not even:
            break

def maxSumRecursive(root):
    # returns the maximal sum from the root to a leaf
    if root is None:
        return 0
    lSum = maxSumRecursive(root.left)
    rSum = maxSumRecursive(root.right)
    return max(lSum, rSum) + root.val


def maxSumIterative(root):
    # returns the maximal sum from the root to a leaf
    if root is None:
        return 0
    nodes = [root]
    values = [root.val]
    mSum = 0

    while nodes:
        v = nodes.pop()
        val = values.pop()
        if v.left is None and v.right is None:
            mSum = max(mSum,val)
        else:
            for child in getChildren(v):
                nodes.append(child)
                values.append(child.val+val)
    return mSum

def heightRecursive(root):
    # returns the height of the tree rooted at root
    if root is None:
        return -1

    lh = heightRecursive(root.left)
    rh = heightRecursive(root.right)
    
    return max(lh,rh) + 1

def isTreeBalanced(root):
    """
    An empty tree is height balanced.
    A non-empty tree is balanced if:
    left subtree is height balanced
    right subtree is height balanced
    abs difference in the height of 2 subtrees is not more than 1 
    """
    if root is None:
        return 0, True
    
    lh, lb = isTreeBalanced(root.left)
    rh, rb = isTreeBalanced(root.right)
    
    isBalanced = lb and rb and abs(lh-rh) <= 1
    return max(lh, rh)+1, isBalanced
    
def getChildren(node):
    # returns the children of a node; returns empty list if node is a leaf node
    if node is None:
        return None

    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    return children

def depthUtil(root):
    if root is None:
        return -1

    maxd = [0]
    def depth(v, ch):
        if v.left is None and v.right is None:
            maxd[0] = max(maxd[0], ch)
        else:
            for child in getChildren(v):
                depth(child, ch+1)

    depth(root, 0)
    return maxd[0]

def depth(root):
    # returns the maximum depth of the tree rooted at root
    if root is None:
        return -1
    maxd = 0
    nodes = [(root,0)]
    while nodes:
        v,currDepth = nodes.pop()
        if v.left is None and v.right is None:
            maxd = max(maxd, currDepth)
        else:
            for child in getChildren(v):
                nodes.append((child,currDepth+1))
    return maxd

def width(root):
    # width of a tree = maximum number of nodes at any level of the tree
    if root is None:
        return 0
    
    nodes = Queue.Queue()
    nodeslevel = Counter() # map with key = level and value = # nodes @ level
    nodes.put((root,0))

    while not nodes.empty():
        v, vh = nodes.get() # v - current node, vh - height of v
        nodeslevel[vh] += 1
        for child in getChildren(v):
            nodes.put((child,vh+1))
    return max(nodeslevel.values())


def widthVER2(root):
    if root is None:
        return 0
    
    curr_level = [root]
    next_level = []
    maxw = 1
    
    while True:
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        if not next_level:
            break
        maxw = max(maxw, len(next_level))
        curr_level = next_level
        next_level = []


def height(root):
    if root is None:
        return -1
    
    nodes = Queue.Queue()
    nodes.put((root,0))
    
    maxh = 0
    while not nodes.empty():
        v, vh = nodes.get() # v - current node, vh - height of v
        if v.left is None and v.right is None:
            maxh = max(maxh, vh)
        else:
            for child in getChildren(v):
                nodes.put((child,vh+1))
    return maxh

# A function to do inorder tree traversal
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # Then print the data of node
        print(root.val),

        # Finally recur on right child
        printInorder(root.right)

def printInorderIterative(root):
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


# A function to do postorder tree traversal w/o recursion
def printPostorderIterative2(root):
    #postorder is reverse of preorder with (node right left)
    stack = []
    stack2 = []
    while True:
        while root:
            stack.append(root)
            stack2.append(root.val)
            root = root.right
        if stack:
            root = stack.pop()
        else:
            break
        root = root.left

    stack2.reverse()
    for item in stack2:
        print (item),

# A function to do postorder tree traversal w/o recursion

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def printPostorderIterative(root):
    stack = []
    while True:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            # If the popped item has a right child and the 
            # right child has not been processed yet, process
            # the right child before.
            if root.right and root.right == peek(stack):
                # pop the right child
                stack.pop()
                
                # push root back to stack
                stack.append(root)
                root = root.right
            else:
                print (root.val),
                root = None
        else:
            break

# A function to do postorder tree traversal
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # Then recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),

        
def printPreorderIterative(root):
    stack = []
    while True:
        while root:
            stack.append(root)
            print (root.val),
            root = root.left
        if stack:
            root = stack.pop()
        else:
            break
        root = root.right

# A function to do preorder tree traversal
def printPreorder(root):

    if root:

        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# A function to do levelorder tree traversal w/o recursion
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


# A function to do levelorder tree traversal 
def printLevelOrder(root):
    if root:
        level = [root]
        printLevelOrderRecurse(level)
    
def printLevelOrderRecurse(level):
    nextlevel = []
    for node in level:
        print (node.val),
        
        if node.left:
            nextlevel.append(node.left)
        if node.right:
            nextlevel.append(node.right)
    
    if nextlevel:
        print ("")
        printLevelOrderRecurse(nextlevel)

def isMirror(root1, root2):
    # returns True if the given binary tree is symmetric
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    return False

def isSymmetric(root):
    if root is None:
        return True
    return isMirror(root.left, root.right)


# Driver code
if __name__ == '__main__':
    root = Node(1)
    
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.right = Node(4)
    root.left.left = Node(9)
    root.right.left = Node(5)
    root.right.right = Node(5)
    
    root.left.right.left = Node(6)
    root.right.left.right = Node(7)
    
#    print "Preorder traversal of binary tree is"
#    printPreorder(root)
#
#    print "\nPreorder traversal of binary tree w/o recursion is"
#    printPreorderIterative(root)

#    print "\nInorder traversal of binary tree w/o recursion is"
#    printInorderIterative(root)
#    
#    print "\nInorder traversal of binary tree is"
#    printInorder(root)
    
#    print "\nPostorder traversal of binary tree is"
#    printPostorder(root)
#    
#    print "\nPostorder traversal of binary tree w/o recursion is"
#    printPostorderIterative(root)
#    
#    print "\nLevelorder traversal of binary tree is"
#    printLevelOrder(root)
#    
#    print "\nLevelorder traversal of binary tree w/o recursion is"
#    printLevelOrderIterative(root)
    
#    print ""
#    #print (heightRecursive(root))
    print ("Height of tree = ")
    #print (width(root))
    #traverseSpiral(root)
#    #print (getChildren(root))
    print (height(root))
    
#    print ("Level Order")
#    printLevelOrder(root)
    
    #print (isSymmetric(root))

