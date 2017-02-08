from BuildDGraph import BuildDGraph
from BreadthFirstPaths import BreadthFirstPaths
from DepthFirstPaths import DepthFirstPaths

'''
Test Client for Graph Processing
'''

inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildDGraph(inputfilepath)
G = bg.buildDGraph() # returns a graph object


# test methods on G
print (G.graphToString())
G.del_node('2')
print (G.graphToString())

'''
# test BFS methods
s = '6'
bfs = BreadthFirstPaths(G, s)
print (bfs.hasPathTo('3'))
print (bfs.pathTo('3'))
print (bfs.shortestDistance('3'))
'''
'''
# test DFS methods
s = '2'
dfs = DepthFirstPaths(G, s)
print (dfs.hasPathTo('3'))
print (dfs.pathTo('3'))
'''
