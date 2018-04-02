'''
make one pass through the query list and get all the starting nodes
of 1 and 2 queries, you need to find all the nodes visited for only these nodes(and the nodes
  on their traversal route) and
NOT the whole graph.
get all the 1 and 2 queries and get all the starting 
'''

from collections import Counter
from collections import defaultdict

paths = Counter()
label = Counter()
visited = set()
graph = defaultdict(set)

def findpath(s):
  visited.add(s)
  for w in graph[s]:
    if w not in visited:
      findpath(w)

def getAllPaths(graph):
  for node in graph:
    if node not in paths:
      path = findpath(node)
      for x, i in enumerate(path):
        if x not in paths:
          paths[x] = path[i:]


class Solution:
  def __init__(self, starterNodes, graph):
    self.starterNodes = starterNodes
    self.nodesVisited = defaultdict(set)
    self.graph = graph

  def findNodesVisited(self, root):
      stack = [(root,0)]
      visited = Counter()
      visited[root] = True
      
      while stack:
          v, index = stack[-1]
          if v in graph and index < len(graph[v]): # checking if any edge left to be explored
              w = graph[v][index]
              #print (v, w), - check # times each edge is traversed
              stack[-1] = (v, index+1)
              if not visited.get(w, False):
                  # visiting w for first time, next start DFS from w
                  # stack[] holds the ancestors of w at any point in time
                  for ancestor in stack:
                      nodesVisited[ancestor[0]].add(w)
                  # all nodes from w are already explored on a previous dfs from
                  # other node
                  #if w not in nodesVisited:
                  stack.append((w,0))
                  visited[w] = True

          else:
              # backtrack from v
              stack.pop()
              visited[v] = False


  def findSolution(self):
    for node in self.starterNodes:
      if node not in self.nodesVisited:
        self.findNodesVisited(node)
      self.nodesVisited[node].add(node)




if __name__ == '__main__':
  n, m, q = map(int, input().strip().split(" "))
  graph = defaultdict(list)
  for _ in range(m):
    u, v = map(int, input().strip().split(" "))
    graph[u].append(v)

  starterNodes = set()
  queries = []
  for _ in range(q):
    q = list(map(int, input().strip().split(" ")))
    queries.append(q)
    if q[0] != 3:
      starterNodes.add(arr[1])
  sol = Solution(starterNodes, graph)
  sol.findSolution()

  label = Counter()

  for q in queries:
    if q[0] == 3:
      print (label[q[1]])
    elif q[0] = 1:
      for node in sol.nodesVisited[q[1]]:
        label[q[1]] = q[2]
    else:
      for node in sol.nodesVisited[q[1]]:
        if q[2] > label[q[1]]:
          label[q[1]] = q[2]
