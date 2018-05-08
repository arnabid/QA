# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:32:44 2016

@author: arnab
"""

import queue
from collections import Counter


# A class that represents an individual node in a Binary Tree
class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

"""
Find the second minimum element in a binary heap
reference: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
"""
def dfs(self, node, min1, ans):
    if node:
        # since we want the second minimum element; if we find a element greater than
        # min1 we dont need to traverse the sub-trees(all values will be equal or greater)
        if min1 < node.val < ans[0]:
            ans[0] = node.val
        elif node.val == min1:
            self.dfs(node.left, min1, ans)
            self.dfs(node.right, min1, ans)

def findSecondMinimumValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return -1
    ans, min1 = [float('inf')], root.val
    self.dfs(root, min1, ans)

    if ans[0] < float('inf'):
        return ans[0]
    return -1

"""
Merge 2 BTs
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


"""
Count Univalue Subtrees
reference: leetcode.com - premium account question
"""
class CountUnivalueSolution:
    def __init__(self):
        self.count = 0

    def countUtility(self, root):
        if root is None:
            return True

        # check if the left sub-tree is a univalue tree
        l = self.countUtility(root.left)
        
        # check if the right sub-tree is a univalue tree
        r = self.countUtility(root.right)
        
        # if both left and right sub-trees are univalue trees, compare with
        # current node value
        if l and r:
            # for a leaf node which is always univalue tree,  make
            # left child node value and right child node value equal to the 
            # leaf node value
            lv, rv = root.val, root.val
            if root.left:
                lv = root.left.val
            if root.right:
                rv = root.right.val
            if root.val == lv and root.val == rv:
                self.count += 1
                return True
        return False

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.countUtility(root)
        return self.count


def calculateHorzDistance(node, val, dmap, mn, mx):
    if node:
        mn[0], mx[0] = min(mn[0], val), max(mx[0], val)
        dmap[val] = dmap.get(val,[]) + [node.val]
        calculateHorzDistance(node.left, val-1, dmap, mn, mx)
        calculateHorzDistance(node.right, val+1, dmap, mn, mx)

"""
Binary Tree Vertical Order Traversal
reference: http://www.geeksforgeeks.org/print-binary-tree-vertical-order/
"""
def verticalOrder(root):
    if root is None:
        return 
    mn, mx = [float('inf')], [-float('inf')]
    dmap = Counter()
    calculateHorzDistance(root, 0, dmap, mn, mx)
    for i in range(mn[0], mx[0]+1):
        print (dmap[i])


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


def helper(v, ans):
    if v is None:
        return -1
    lh = helper(v.left, ans)
    rh = helper(v.right, ans)
    ans[0] = max(ans[0], lh + rh + 2)
    return (max(lh, rh) + 1)

"""
The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.
"""
def diameterOfBinaryTree(root):
    if root is None:
        return 0
    ans = [0]
    helper(root, ans)
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
returns the list of nodes in path from root to node using BFS
"""
def findPathBFS(root, node):
    if root is None:
        return []
    
    parent = Counter()
    q = queue.Queue()
    q.put(root)
    
    v = None
    while not q.empty():
        v = q.get()
        if v == node:
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
returns the list of nodes in path from root to node
DFS recursion
"""
def findPathDFS(root, x, path):
    if root:
        path.append(root)
        if root == x:
            return True
        if findPathDFS(root.left, x, path):
            return True
        if findPathDFS(root.right, x, path):
            return True
        path.pop()
    return False


"""
find the lca of 2 nodes x, y
method1
"""
def findLCA(root, x, y):
    """
    :type root: TreeNode
    :type x: TreeNode
    :type y: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    
    # find path of root to x
    pathx = findPathBFS(root, x)
    
    # find path of root to y
    pathy = findPathBFS(root, y)
    
    i, j = 0, 0
    lx, ly = len(pathx), len(pathy)
    while i < lx and j < ly and pathx[i] == pathy[j]:
        i += 1
        j += 1
    
    return pathx[i-1]

"""
find the lca of 2 nodes p, q
method2
"""
def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    if root == p or root == q:
        return root
    lLCA = lowestCommonAncestor(root.left, p, q)
    rLCA = lowestCommonAncestor(root.right, p, q)
    
    if lLCA and rLCA:
        return root
    elif lLCA:
        return lLCA
    else:
        return rLCA


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


"""
traverse a BT in a spiral fashion
"""        
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


"""
Find the maximal sum from the root to a leaf
"""
def maxSumRecursive(root):
    if root is None:
        return 0
    lSum = maxSumRecursive(root.left)
    rSum = maxSumRecursive(root.right)
    return max(lSum, rSum) + root.val


def maxSumIterative(root):
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


"""
LeetCode 124 - Binary Tree Maximum Path Sum
"""
class MaxPathSumSolution(object):
    def __init__(self):
        self.ans = -float('inf')

    def maxPathSumUtil(self, root):
        if root is None:
            return 0
        lv = max(self.maxPathSumUtil(root.left), 0)
        rv = max(self.maxPathSumUtil(root.right), 0)
        
        self.ans = max(self.ans, root.val + lv + rv)
        return max(lv, rv) + root.val

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.maxPathSumUtil(root)
        return self.ans


# returns the children of a node; returns empty list if node is a leaf node
def getChildren(node):
    if node is None:
        return None

    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    return children


"""
4 different ways to find the height/depth of a tree
"""

# normal recursion
def heightRecursive(root):
    # returns the height of the tree rooted at root
    if root is None:
        return 0

    # leaf node
    if root.left is None and root.right is None:
        return 0

    lh = heightRecursive(root.left)
    rh = heightRecursive(root.right)
    
    return max(lh,rh) + 1


# recursive DFS
def depthUtil(root):
    if root is None:
        return 0

    maxd = [0]
    def depth(v, ch):
        if v.left is None and v.right is None:
            maxd[0] = max(maxd[0], ch)
        else:
            for child in getChildren(v):
                depth(child, ch+1)

    depth(root, 0)
    return maxd[0]


# iterative DFS
def depth(root):
    if root is None:
        return 0
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


# BFS
def height(root):
    if root is None:
        return -1
    
    nodes = queue.Queue()
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


"""
Find the width of a tree = maximum number of nodes at any level of the tree
"""
def width(root):
    if root is None:
        return 0
    
    maxw = 0
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        maxw = max(maxw, q.qsize())
        for _ in range(q.qsize()):
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


"""
check if 2 BTs are mirror images
"""
def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    return root1.val == root2.val and \
    isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)


"""
check if a BT is symmetric
"""
def isSymmetric(root):
    # returns True if the given binary tree is symmetric
    # A tree is symmetric if its left sub-tree is a mirror image of its
    # right sub-tree
    if root is None:
        return True
    return isMirror(root.left, root.right)


"""
postorder tree traversal w/o recursion
"""
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
    q = queue.Queue()
    q.put(root)
    res = []
    while not q.empty():
        level = []
        for _ in range(q.qsize()):
            v = q.get()
            if v.left:
                q.put(v.left)
            if v.right:
                q.put(v.right)
            level.append(v.val)
        res.append(level)
    return res


"""
levelorder tree traversal 
"""
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


"""
LeetCode 687 - Longest Univalue Path
"""
class LongestUnivaluePathSolution:
    def __init__(self):
        self.ans = 0

    def findLongestUniValuePathUtil(self, root):
        if root is None:
            return 0

        lv, rv = 0, 0

        res = 0
        if root.left:
            lv = self.findLongestUniValuePathUtil(root.left)
            if root.val == root.left.val:
                self.ans = max(self.ans, lv + 1)
                res = max(res, lv + 1)
        if root.right:
            rv = self.findLongestUniValuePathUtil(root.right)
            if root.val == root.right.val:
                self.ans = max(self.ans, rv + 1)
                res = max(res, rv + 1)
        if root.left and root.right:
            if root.val == root.left.val and root.val == root.right.val:
                self.ans = max(self.ans, lv + rv + 2)
                res = max(res, max(lv,rv) + 1)
        return res

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findLongestUniValuePathUtil(root)
        return self.ans


"""
LeetCode 652 - Find duplicate subtrees
"""
class FindDuplicateSubtreesSolution:
    def __init__(self):
        self.hm = {}
        self.ans = []
    
    def findDuplicateSubtreesUtil(self, root):
        if root is None:
            return "#"
        
        lv = self.findDuplicateSubtreesUtil(root.left)
        rv = self.findDuplicateSubtreesUtil(root.right)
        
        s = str(root.val) + lv + rv
        if s in self.hm:
            if self.hm[s][1] == 1:
                self.hm[s][1] = 2
                self.ans.append(root)            
        else:
            self.hm[s] = [root, 1]
        return s
        

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root is None:
            return []
        """
        The entire tree cannot have a duplicate, suffices to search for duplicate
        subtrees in the left and right subtrees of root node.
        Every subtree is represented as a unique string.
        """
        self.findDuplicateSubtreesUtil(root.left)
        self.findDuplicateSubtreesUtil(root.right)
        return self.ans



"""
LeetCode 742 - Closest leaf in a Binary tree
"""
class FindClosestLeafSolution():
    def __init__(self):
        self.visited = []
        self.closestLeaf = {}

    def findClosestLeafUtil(self, root):
        if root.left is None and root.right is None:
            self.closestLeaf[root] = 0
            return 0
        lv, rv = float('inf'), float('inf')
        if root.left:
            lv = self.findClosestLeafUtil(root.left)
        if root.right:
            rv = self.findClosestLeafUtil(root.right)
        self.closestLeaf[root] = min(lv,rv) + 1
        return self.closestLeaf[root]

    def findPath(self, root, x):
        if root is None:
            return False
        self.visited.append(root)
        if root == x:
            return True
        if self.findPath(root.left, x):
            return True
        if self.findPath(root.right, x):
            return True
        self.visited.pop()
        return False

    def findClosestLeaf(self, root, x):
        if root is None or x is None:
            return None

        # find the distance to the closest leaf for each node in the tree
        # store that info in self.closestLeaf
        self.findClosestLeafUtil(root)
        
        # find the path from the root to x; store that info in self.visited
        self.findPath(root, x)
        
        # find the min distance to a leaf from each node on the path from root to x
        ans = float('inf')
        hops = len(self.visited) - 1
        for node in self.visited:
            ans = min(ans, self.closestLeaf[node] + hops)
            hops -= 1
        return ans


"""
LeetCode 663 - Equal Tree Partition
"""
class EqualTreePartitionSolution():
    def checkEqualTree(self, root):
        sums = []

        def dfs(v):
            if v is None:
                return 0
            val = dfs(root.left) + dfs(root.right) + root.val
            sums.append(val)
            return val

        total = dfs(root)
        sums.pop()
        return total // 2 in sums


"""
check if a tree is foldable

eg: the tree below is foldable

       10
     /    \
    7      15
     \    /
      9  11

eg: the tree below is not foldable

        10
       /  \
      7   15
     /    /
    5   11
"""

def isFoldableUtil(r1, r2):
    if r1 is None and r2 is None:
        return True

    if r1 is None or r2 is None:
        return False

    return isFoldableUtil(r1.left, r2.right) and \
    isFoldableUtil(r1.right, r2.left)


def isFoldable(root):
    if root is None:
        return True

    return isFoldableUtil(root.left, root.right)


"""
trim all the leaf nodes in a tree
"""
def trimleaves(root):
    if root is None:
        return None

    # current node is a leaf
    if root.left is None and root.right is None:
        root = None
        return root

    root.left = trimleaves(root.left)
    root.right = trimleaves(root.right)
    return root


"""
delete a tree - in post order; delete children then parent
"""
def deleteTree(root):
    if root is None:
        return None
    root.left = deleteTree(root.left)
    root.right = deleteTree(root.right)
    root = None
    return root


"""
find if a node exists in a tree
"""
def find(root, x):
    """
    :type root: TreeNode
    :type x: TreeNode
    :rtype: boolean
    """
    if root is None:
        return False
    
    if root == x or find(root.left, x) or find(root.right, x):
        return True
    return False


"""
Leetcode 814 - Binary Tree Pruning
"""
def pruneTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if root.left is None and root.right is None and root.val == 0:
        return None
    return root

"""
Leetcode 226 - invert binary tree
"""
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root



# Driver code
if __name__ == '__main__':
    root = Node(-1)
    
    root.left = Node(0)
    root.left.left = Node(1)
    root.left.left.left = Node(2)
    
    root.left.left.right = Node(3)
    root.left.left.right.left = Node(4)
    root.left.left.right.left.left = Node(4)
    root.left.left.right.left.left.left = Node(6)
    x = root.left.left.right
    
    sol = FindClosestLeafSolution()
    print (sol.findClosestLeaf(root, x))