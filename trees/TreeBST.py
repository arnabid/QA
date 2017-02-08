# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:04:24 2016

@author: arnab
"""

""" Program to check if a given binary tree is a BST 
Do inorder traversal and check if the nodes are visited in non-decreasing order """


class Node(object):
    def __init__(self, key = None):
        self.val = key
        self.left = None
        self.right = None

def validateBST(root):
    if root is None:
        return False
    maxv = [-float('inf')]
    return validateBSTUtil(root, maxv)

def validateBSTUtil(root, maxv):
    if root is None:
        return True
    
    flag = True
    flag = validateBSTUtil(root.left, maxv)
    if not flag:
        return False
    if root.val < maxv[0]:
        return False
    else:
        maxv[0] = root.val
    flag = validateBSTUtil(root.right, maxv)
    return flag


# Method 2; uses an auxillary array to store the nodes in inorder
def checkBST(node, mylist):
    if node:
        checkBST(node.left, mylist)
        
        mylist.append(node.val)
        
        checkBST(node.right, mylist)

def isBST(root, minval, maxval):
    if root is None:
        return True
    if root.val < minval or root.val > maxval:
        return False
    
    ltreeOK, rtreeOK = True, True
    if root.left:
        ltreeOK = isBST(root.left, minval, root.val)
    if root.right:
        rtreeOK = isBST(root.right, root.val+1, maxval)
    return ltreeOK and rtreeOK


if __name__ == '__main__':
    root = Node(4)
    
    root.left = Node(2)
    root.right = Node(5)
    
    root.left.left = Node(1)
    root.left.right = Node(1)
    
    # Method 3 - without the auxillary array
    print (validateBST(root))
    
    # Method 1
    #print (isBST(root, -float('inf'), float('inf')))
    
#    # Method 2
#    mylist = []
#    checkBST(root, mylist)
#    
#    flag = True
#    for i in xrange(1,len(mylist)):
#        if mylist[i] < mylist[i-1]:
#            flag = False
#            break
#    if flag:
#        print ("BST")
#    else:
#        print ("Not a BST")

            