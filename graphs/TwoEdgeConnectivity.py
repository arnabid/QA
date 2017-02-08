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
"""

from collections import Counter
treeEdges, bridgeEdges = Counter(), set()
visited, arr = {}, {}
time = 0

def ECUtil(graph):
    # pick a node and start a DFS
    start = graph.keys()[0]
    EC(start,None)
    
    # graph is 2 edge-connected if there are no bridge edges
    return len(bridgeEdges) == 0
    
def EC(v, pv):
   visited[v] = True
   global time
   arr[v] = time
   time += 1
   
   dbe = arr[v]
   for w in graph[v]:
       if not visited.get(w, False):
           treeEdges[(v,w)] = 0
           dbe = min(dbe, EC(w,v))
       else:
           if (w,v) not in treeEdges:
               dbe = min(dbe, arr[w])
           else:
               treeEdges[(w,v)] += 1
               if treeEdges[(w,v)] > 1:
                   dbe = min(dbe, arr[w])

   if arr[v] != 0 and dbe == arr[v]:
       bridgeEdges.add((pv,v))
   return dbe
    
    
if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split(" "))
    graph = Counter()
    
    for i in xrange(m):
        u, v = map(int, raw_input().strip().split(" "))
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    #print (graph)
    
    is2EC = ECUtil(graph)
    print (is2EC)
    print bridgeEdges
    print treeEdges.keys()
    