"""
Minimum height trees
Reference: https://leetcode.com/problems/minimum-height-trees/
insight: the longest path between any two nodes in an undirected tree has
to pass through the nodes in a the minimum height tree.
"""

from collections import defaultdict

def findMinHeightTrees(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    # create a graph
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # create a set with all nodes
    s = set(range(n))
    len_longest_path = 0
    while len(s) > 2:
        # get the current batch of leaves
        leaves = set(i for i in s if len(graph[i]) == 1)

        # remove the current batch of leaves from the set of nodes
        s -= leaves

        # prune each leaf, discard the edge
        for i in leaves:
            for j in graph[i]:
                graph[j].remove(i)
        
        # increment the longest_path by 2
        len_longest_path += 2
    if len(s) == 2:
        len_longest_path += 1
    print(f"Length of the longest path in the tree is {len_longest_path}")
    print(f"The root(s) of the minimum height tree is {list(s)}")
