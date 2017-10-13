# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:12:42 2016

@author: arnab
"""
"""
Notes:
A bridge edge will be an edge in the set of tree edges, it will
not be a back edge. A bridge edge will always be discovered in the 
DFS tree. 

A bridge edge is the only edge that joins two components in a graph. Therefore, 
when starting a DFS from a node in one component, the nodes in the other component
will be discovered through the bridge edge. Hence, a bridge edge has to be a tree edge.

Another thought: Back edges are between a node and its ancestors. There is already a path from
every ancestor to this node. Therefore the back edge cannot be a tree edge.
"""

from collections import defaultdict
from collections import Counter

treeEdges, bridgeEdges = Counter(), set()
visited, arr = {}, {}
time = [0]

"""
returns if a graph is 2 edge connected 
"""
def ECUtil(graph):
    # pick a node and start a DFS
    start = graph.keys()[0]
    EC(start)
    
    # graph is 2 edge-connected if there are no bridge edges
    return len(bridgeEdges) == 0
    
def EC(v, pv = None):
   visited[v] = True
   arr[v] = time[0]
   time[0] += 1
   
   dbe = arr[v]
   for w in graph[v]:
       if not visited.get(w, False):
           treeEdges[(v,w)] = 0
           dbe = min(dbe, EC(w,v))
       else:
           if (w,v) not in treeEdges:
               dbe = min(dbe, arr[w])
           else:
               # takes into account parallel edges between v and w in a multigraph
               treeEdges[(w,v)] += 1
               if treeEdges[(w,v)] > 1:
                   dbe = min(dbe, arr[w])

   if arr[v] != 0 and dbe == arr[v]:
       bridgeEdges.add((pv,v))
   return dbe
    
    
if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split(" "))
    graph = defaultdict(list)
    
    # input the edges in the graph
    for i in xrange(m):
        u, v = map(int, raw_input().strip().split(" "))
        graph[u].append(v)
        graph[v].append(u)
    
    is2EC = ECUtil(graph)
    print (is2EC)
    print bridgeEdges
    print treeEdges.keys()
    