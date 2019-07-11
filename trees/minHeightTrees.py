# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 08:11:03 2017

@author: arnab
"""

"""
Minimum height trees
reference: https://leetcode.com/problems/minimum-height-trees/description/

Notes:
There can be only 1 or 2 nodes with minimum height trees.

These nodes are the critical nodes in the sense that maximum distance and total distance to
reach a node (or all nodes) in the network will be minimum. Any sort of message propagation
will be most efficient from these node(s).


Runtime analysis:
build the degree map: O(E)
every node gets added and removed from the queue only once.
when the node is in the front of the queue, its edges are examined. 
so total time: O(E)

linear time algorithm: O(E) + O(E)
"""

from collections import Counter
import queue

def findMinHeightTrees(graph):
    n = len(graph)
    degree = Counter()
    q = queue.Queue()
    # build the degree map and put the leaves in the queue
    for node in graph:
        degree[node] = len(graph[node])
        if degree[node] == 1:
        	q.put(node)

    while n > 2:
        # prune the batch of leaves present in the queue
        for i in range(q.qsize()):
            v = q.get()
            n -= 1
            for w in graph.get(v, []):
                degree[w] -= 1
                if degree[w] == 1:
                    q.put(w)
    res = []
    while not q.empty():
        res.append(q.get())
    return res


from collections import deque
from collections import Counter
def diameter(self, root):
    self.q = deque()
    label = Counter()
    degree = Counter()
    def dfs(root, par=None):
        if root.left is None and root.right is None:
            self.q.append((root))
            label[root] = 1
        root.par = par
        if root.left:
            degree[root] += 1
            degree[root.left] += 1
            dfs(root.left)
        if root.right:
            degree[root] += 1
            degree[root.right] += 1
            dfs(root.right)
    dfs(root)
    ans = 0
    while n > 2:
        for _ in range(len(q)):
            node = q.popleft()
            n -= 1
            for nei in (node.par, node.left, node.right):
                if nei:
                    ans = max(ans, label[node] + label[nei] + 1)
                    if label[node] > label[nei]:
                        label[nei] = label[node] + 1
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
    if n == 2:
        return ans + 1
    return ans


