# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:32:44 2016

@author: arnab
"""

import Queue
from collections import Counter

# Study Morris traversals - binary threaded trees

# A class that represents an individual node in a Binary Tree
class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

"""
reference: https://leetcode.com/problems/merge-two-binary-trees/#/description
"""
def mergeTrees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    root = Node(t1.val + t2.val)
    root.left = mergeTrees(t1.left, t2.left)
    root.right = mergeTrees(t1.right, t2.right)
    return root


def calculateHorzDistance(node, val, dmap, mn, mx):
    if node:
        mn[0], mx[0] = min(mn[0], val), max(mx[0], val)
        if val in dmap:
            dmap[val].append(node.val)
        else:
            dmap[val] = [node.val]
        calculateHorzDistance(node.left, val-1, dmap, mn, mx)
        calculateHorzDistance(node.right, val+1, dmap, mn, mx)

"""
Binary Tree Vertical Order Traversal
reference: http://www.geeksforgeeks.org/print-binary-tree-vertical-order/

mn, mx = [float('inf')], [-float('inf')]
dmap = Counter()
calculateHorzDistance(root, 0, dmap, mn, mx)
for i in xrange(mn, mx+1):
    print (dmap[i])
"""


"""
prints the values of the boundary nodes if a tree
in the anti-clockwise direction
"""
def addInOrder(root, res):
    if root:
        addInOrder(root.left, res)
        if root.left is None and root.right is None:
            res.append(root.val)
        addInOrder(root.right, res)

def printBoundary(root):
    if root is None:
        return []
    
    t, res = root.left, []
    # add the left boundary top-down
    while t and t.left:
        res.append(t.val)
        t = t.left
    
    # add the leaf nodes left-right
    addInOrder(root, res)
    
    t, rightnodes = root.right, []
    # add the right boundary bottom-up
    while t and t.right:
        rightnodes.append(t.val)
        t = t.right
    res += rightnodes[::-1]
    
    # append the root node
    res.append(root.val)
    return (res)


def heightA(v, ans):
    if v is None:
        return -1
    lh = heightA(v.left, ans)
    rh = heightA(v.right, ans)
    ans[0] = max(ans[0], lh + rh + 2)
    return (max(lh, rh) + 1)

def diameterOfBinaryTree(root):
    if root is None:
        return 0
    ans = [0]
    heightA(root, ans)
    return ans[0]

"""
check if a binary tree is a subtree of another tree
reference:
http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
"""
def isSubtree(r1, r2):
    if r2 is None:
        return True
    if r1 is None:
        return False
    
    if isIdentical(r1, r2):
        return True
    
    return isSubtree(r1.left, r2) or isSubtree(r1.right, r2)

"""
check if 2 trees are identical
"""
def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    return root1.val == root2.val and \
    isIdentical(root1.left, root2.left) and \
    isIdentical(root1.right, root2.right)

"""
returns the list of nodes in path from root to node
node.val = x
DFS iteration
"""
def findPathDFSIter(root, x):
    stack = [root]
    parent = Counter()
    v = None
    while stack:
        v = stack.pop()
        if v.val == x:
            break
        for w in getChildren(v):
            stack.append(w)
            parent[w] = v
    
    path = []
    while v != root:
        path.append(v)
        v = parent[v]
    path.append(root)
    return path[::-1]


"""
returns the list of nodes in path from root to node
node.val = x
DFS recursion
"""
def findPathDFS(root, x):
    if root is None:
        return []
    path = []
    findPath(root, x, path)
    return path
    
def findPath(v, x, path):
    path.append(v)
    if v.val == x:
        return True
    for w in getChildren(v):
        if findPath(w, x, path):
            return True
    path.pop()
    return False

"""
returns the list of nodes in path from root to node
node.val = x
BFS
"""
def findPathBFS(root, x):
    # using BFS
    if root is None:
        return []
    
    parent = Counter()
    q = Queue.Queue()
    q.put(root)
    
    v = None
    while not q.empty():
        v = q.get()
        if v.val == x:
            break
        
        for w in getChildren(v):
            q.put(w)
            parent[w] = v
    
    path = []
    while v != root:
        path.append(v)
        v = parent[v]
    path.append(root)
    
    return path[::-1]

"""
find the lca of 2 nodes with values x, y
"""

def findLCA(root, x, y):
    if root is None:
        return None
    
    # find path of root to x
    pathx = findPathBFS(root, x)
    
    # find path of root to y
    pathy = findPathBFS(root, y)
    
    i, j = 0, 0
    lx, ly = len(pathx), len(pathy)
    while i < lx and j < ly and pathx[i].val == pathy[j].val:
        i += 1
        j += 1
    
    return pathx[i-1]

"""
clone a binary tree
"""
def clone(root):
    if root is None:
        return None
    r = Node(root.val)
    r.left = clone(root.left)
    r.right = clone(root.right)
    return r

        
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
    
    maxw = 0
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        maxw = max(maxw, q.qsize())
        for _ in xrange(q.qsize()):
            v = q.get()
            if v.left:
                q.put(v.left)
            if v.right:
                q.put(v.right)
    return maxw


def widthVER2(root):
    if root is None:
        return 0
    
    cl, maxw = [root], 0
    while cl:
        maxw = max(maxw, len(cl))
        nl = []
        for node in cl:
            if node.left:
                nl.append(node.left)
            if node.right:
                nl.append(node.right)
        cl = nl
    return maxw


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


def isMirror(root1, root2):
    # returns True if trees at root1 and root2 are mirror images
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    return root1.val == root2.val and \
    isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

def isSymmetric(root):
    # returns True if the given binary tree is symmetric
    # A tree is symmetric if its left sub-tree is a mirror image of its
    # right sub-tree
    if root is None:
        return True
    return isMirror(root.left, root.right)


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


"""
level order traversal of a binary tree
reference: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    q = Queue.Queue()
    q.put(root)
    res = []
    while not q.empty():
        level = []
        for _ in xrange(q.qsize()):
            v = q.get()
            if v.left:
                q.put(v.left)
            if v.right:
                q.put(v.right)
            level.append(v.val)
        res.append(level)
    return res


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


# Driver code
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


