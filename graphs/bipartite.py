"""
All questions related to a bipartite graph
Is a graph bipartite?
Find the 2 set of nodes in the bipartite graph
Support the operation given 2 nodes returns True if they are in the same set.
"""

class Solution:
    def __init__(self):
        self.visited = {}

    # returns True if nodes x and y are in the same set; Note: this is not a unique solution
    # in case the graph is not connected.
    def isSameSet(self, x, y):
        return self.visited[x] == self.visited[y]

    # returns the 2 sets of nodes in a bipartite graph
    def find2Sets(self):
        s1, s2 = set(), set()
        for key in self.visited:
            if self.visited[key]:
                s1.add(key)
            else:
                s2.add(key)
        return s1, s2


    def dfs(self, graph, v, state):
        self.visited[v] = state
        for w in graph[v]:
            if w not in self.visited:
                if not self.dfs(graph, w, not state):
                    return False
            else:
                if self.visited[w] == state:
                    return False
        return True
        
        
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        sol = Solution()
        for node in range(n):
            if node not in sol.visited:
                # avoid traversing the whole graph if it is not bipartite
                if not sol.dfs(graph, node, True):
                    return False
        return True