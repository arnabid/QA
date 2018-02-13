# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:44:17 2016

@author: arnab
"""

""" Binary Search Tree questions"""

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

"""
trim BST
reference: https://leetcode.com/problems/trim-a-binary-search-tree/description/
"""

def trimBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    if root is None:
        return None
    if root.val > R:
        return self.trimBST(root.left, L, R)
    if root.val < L:
        return self.trimBST(root.right, L, R)
    root.left = self.trimBST(root.left, L, R)
    root.right = self.trimBST(root.right, L, R)
    return root


def search(root, key):
    # returns the node with val equal to key in the BST rooted at root
    # else returns None if the key is not found
    if root is None:
        return None
    
    if root.val == key:
        return root
    elif key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

def searchIter(root, key):
    # iterative search procedure
    while root:
        if root.val == key:
            return root
        elif key < root.val:
            root = root.left
        else:
            root = root.right
    
    return root


def findMax(root):
    # returns the node with max key in the BST rooted at root
    if root is None:
        return None
    
    while root.right:
        root = root.right
    
    return root
    
def findMin(root):
    # returns the node with min key in the BST rooted at root
    if root is None:
        return root
    
    while root.left:
        root = root.left
    
    return root

def successor(root, key):
    # returns the successor of key in the BST rooted at root
    # the successor is the smallest key in the BST greater than key
    if root is None:
        return None
    
    sc = None
    while root:
        if root.val <= key:
            root = root.right
        else:
            sc = root.val
            root = root.left
    return sc

    
def predecessor(root, key):
    # returns the predecessor of key in the BST rooted at root
    # the predecessor is the largest key in the BST less than key
    if root is None:
        return None
    
    p = None
    while root:
        if root.val >= key:
            root = root.left
        else:
            p = root.val
            root = root.right
    return p


"""
inserts a node in a BST
"""
def insert(root, node):
    # inserts node in the BST rooted at root
    if root is None:
        root = node
        return root
    p, current = None, root
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


"""
deletes a node in a BST
"""
def delete(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
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


"""
check if a BT is a BST
good example of top-down recursion
"""
# approach1
def isBST(root, minval, maxval):
    if root is None:
        return True
    if root.val < minval or root.val > maxval:
        return False
    
    ltreeOK = isBST(root.left, minval, root.val)
    if ltreeOK is False:
        return False
    rtreeOK = isBST(root.right, root.val+1, maxval)
    return rtreeOK

# approach 2 - inorder traversal while updating previous seen value
# initially called with prev = [-float('inf')]
def check(self, root, prev):
    if root:
        if not self.check(root.left, prev):
            return False
        if root.val <= prev[0]:
            return False
        prev[0] = root.val
        if not self.check(root.right, prev):
            return False
    return True


"""
constructs a BST from a sorted array
"""
def sortedArrayToBST(arr, start, end):
    # builds a balanced BST from sorted array arr
    if start > end:
        return None
    
    mid = (start+end)/2
    node = Node(arr[mid])
    
    node.left = sortedArrayToBST(arr, start, mid-1)
    node.right = sortedArrayToBST(arr, mid+1, end)
    return node


"""
modify each node val = sum of all nodes >= itself
"""
def sumGreater(root, count):
    if root:
        sumGreater(root.right, count)
        count[0] += root.val
        root.val = count[0]
        sumGreater(root.left, count)


"""
finds the lowest common ancestor of keys n1 and n2
"""
def lca(root, n1, n2):
    if root is None:
        return None

    if n1 < root.val and n2 < root.val:
        return lca(root.left, n1, n2)
    elif n1 > root.val and n2 > root.val:
        return lca(root.right, n1, n2)
    return root


# A function to return the node with the Kth smallest key in a BST rooted at root
def findKthSmallest(root, k):
    
    if root is None:
        return None

    # recur on left child
    temp = findKthSmallest(root.left, k)
    if temp:
        return temp

    # Is this the last node to be visited?
    k[0] -= 1
    if k[0] == 0:
        return root
    
    # recur on right child
    temp = findKthSmallest(root.right, k)
    if temp:
        return temp
    
    return None

def findKthLargest(root, k):
    
    if root is None:
        return None
    
    # recur on the right child
    temp = findKthLargest(root.right, k)
    if temp:
        return temp

    k[0] -= 1
    if k[0] == 0: # no more nodes left to visit
        return root
    
    # recur on the left child
    temp = findKthLargest(root.left, k)
    if temp:
        return temp
    
    return None
    

def findAllKeys(root, mink, maxk, a):
    if root is None:
        return
    
    stack = []
    while True:
        while root:
            if root.val >= mink and root.val <= maxk:
                stack.append(root)
                root = root.left
            elif root.val > maxk:
                root = root.left
            else:
                root = None
        if stack:
            root = stack.pop()
            a.append(root.val)
        else:
            break
        root = root.right

def findKeys(root, mink, maxk, a):
    # finds the keys in a BST in a given range; does not return duplicate keys
    if root is None:
        return
    # if the root key < mink; search only in right sub-tree
    if root.val < mink:
        findKeys(root.right, mink, maxk, a)
    # if the root key > maxk; search only in the left sub-tree
    elif root.val > maxk:
        findKeys(root.left, mink, maxk, a)
    else:
        findKeys(root.left, mink, maxk, a)
        a.append(root.val)
        findKeys(root.right, mink, maxk, a)

def find2ndSmallest(root):
    # returns the second smallest key in BST
    if root is None:
        return None

    p = None
    while root.left:
        p = root
        root = root.left
    if p:
        return p
    else:
        return findMin(root.right)

def find2ndLargest(root):
    # returns the 2nd largest key in BST
    if root is None:
        return None
    
    p = None
    while root.right:
        p = root
        root = root.right
    if p:
        return p
    else:
        return findMax(root.left)

def findNodeInBetween(root, a, b):
    # returns the first node it discovers between [a,b], OW returns None
    if root is None:
        return None
    if root.val < a:
        return findNodeInBetween(root.right, a, b)
    elif root.val > b:
        return findNodeInBetween(root.left, a, b)
    else:
        return root

def convertBSTDoubleLL(root):
    # converts a BST to a double linked list of nodes in order
    if root is None:
        return

    first, last = None, None
    tmp = root
    while tmp.left:
        tmp = tmp.left
    first = tmp # smallest node

    tmp = root
    while tmp.right:
        tmp = tmp.right
    last = tmp # biggest node

    prev, stack = None, []
    while True:
        while root:
            stack.append(root)
            root = root.left

        if stack:
            root = stack.pop()
            if prev:
                prev.right = root
                root.left = prev
            prev = root
            root = root.right
        else:
            break

    first.left = last
    last.right = first

    return first, last


def convertBSTSortedLL(root, prev):
    if root is None:
        return
    convertBSTSortedLL(root.right, prev)
    root.right = prev[0]
    temp = root.left
    root.left = None
    prev[0] = root
    convertBSTSortedLL(temp, prev)

def distance(start, endval):
    """
    returns the number of hops between start node and 
    node with val = endval. It is guaranteed that start is an
    ancestor of node with val = endval
    """
    d = 0
    while start and start.val != endval:
        if endval > start.val:
            start = start.right
        else:
            start = start.left
        d += 1
    return d


"""
find the closest value in a BST to a given value k
"""
def findclosestValueBST(node, k):
    if node is None:
        return None
    
    p, s = None, None
    while node:
        if node.val == k:
            return k
        elif node.val < k:
            p = node.val
            node = node.right
        else:
            s = node.val
            node = node.left
    
    if s is None:
        return p
    
    if p is None:
        return s
    
    if k - p < s - k:
        return p
    else:
        return s


"""
find if 2 nodes in a BST sum to a target value
reference: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
"""
def traverseInOrder(root, arr):
    if root:
        traverseInOrder(root.left, arr)
        arr.append(root.val)
        traverseInOrder(root.right, arr)

def findTarget(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    if root is None:
        return False
    arr = []
    traverseInOrder(root, arr)
    
    n = len(arr)
    i, j = 0, n-1
    while i < j:
        s = arr[i] + arr[j]
        if s == k:
            return True
        elif s < k:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':
    root = insert(None, Node(3))
    root = insert(root, Node(1))
    root = insert(root, Node(2))
    root = insert(root, Node(4))
    root = insert(root, Node(3.5))
    root = insert(root, Node(6))
