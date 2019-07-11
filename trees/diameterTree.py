# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:16:05 2017

@author: arnab
"""

"""
Diameter of a general tree
diameter = length of the longest path between any 2 nodes in the tree

Why does the longest path between any 2 nodes in the tree pass through the 
min height node?

consider the tree rooted at the min height node. The longest path possible is
<= 2*h, h = height of tree. All other paths that do not pass through the min height
node are strictly less than the longest path through the min node < 2*h. Therefore the longest
path which is <= 2*h will pass through the min height node.
"""

from collections import Counter
import Queue

def findDiameterTree(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n <= 2:
        return n-1
    degree = Counter()
    graph = Counter()
    # build the graph and the degree map
    for u,v in edges:
        degree[u] += 1
        degree[v] += 1
        graph[u] = graph.get(u,[])+[v]
        graph[v] = graph.get(v,[])+[u]
    
    # put the leaves in the queue
    q = Queue.Queue()
    for node in graph.keys():
        if degree[node] == 1:
            q.put(node)
    
    diameter = 0
    while n > 2:
        diameter += 1
        # prune the current batch of leaves
        for i in xrange(q.qsize()):
            v = q.get()
            n -= 1
            for w in graph.get(v, []):
                degree[w] -= 1
                if degree[w] == 1:
                    q.put(w)
    diameter *= 2
    if n == 2:
        return diameter + 1
    return diameter



"""
quick way to find the neighbors of a tree
reference: https://leetcode.com/problems/diameter-of-binary-tree/
"""
from collections import deque
from collections import Counter

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.q = deque()
        self.n = 0
        if root.left is None or root.right is None:
            self.q.append(root)
        degree = Counter()
        def dfs(root, par=None):
            self.n += 1
            if root.left is None and root.right is None:
                self.q.append((root))
            root.par = par
            if root.left:
                degree[root] += 1
                degree[root.left] += 1
                dfs(root.left, root)
            if root.right:
                degree[root] += 1
                degree[root.right] += 1
                dfs(root.right, root)
        dfs(root)
        ans = 0
        while self.n > 2:
            ans += 1
            for _ in range(len(self.q)):
                node = self.q.popleft()
                self.n -= 1
                for nei in (node.par, node.left, node.right):
                    if nei:
                        degree[nei] -= 1
                        if degree[nei] == 1:
                            self.q.append(nei)
        ans *= 2
        if self.n == 2:
            ans += 1
        return ans



"""
recursive approach
"""
from collections import Counter
class Solution(object):    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if node is None:
                return -1
            lh = dfs(node.left)
            rh = dfs(node.right)
            self.ans = max(self.ans, lh + rh + 2)
            return max(lh,rh) + 1
        dfs(root)
        return self.ans

