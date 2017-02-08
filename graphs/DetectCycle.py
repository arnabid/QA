from BuildGraph import BuildGraph

'''
Cycle detection in G using DFS
Assuming G is connected; if there are multiple connected components in G,
then start a DFS from every vertex of G that is not visited.
'''

class DetectCycle(object):
    def __init__(self, G):
        self.marked = {}
        self.edgeTo = {}
        self.cycle = []
        self.G = G
        # select a node arbitrarily to start a DFS
        v = list(self.G.nodes())[0]
        self.cycleExists = self.detectCycle(v)

    def detectCycle(self, v):
        # returns a boolean to indicate if a cycle exists in G
        # also finds an existing cycle in G if any.
        self.marked[v] = True
        
        for w in self.G.adj(v):
            if not self.marked.get(w, False):
                self.edgeTo[w] = v
                # avoid completing DFS on all adjacent nodes if cycle already found
                if self.detectCycle(w):
                    return True
            else:
                # w is already visited, if w is not parent, then cycle exists
                if w != self.edgeTo[v]:
                    # print the cycle as a list of nodes in self.cycle
                    # edge(w,v) is the closing edge, trace v back to w
                    self.cycle.extend([w, v])
                    while self.edgeTo[v] != w:
                        self.cycle.append(self.edgeTo[v])
                        v = self.edgeTo[v]
                    self.cycle.append(w)
                    return True
        return False

# testing
inputfilepath = input("Enter the input file path: ") # input file that describes G
bg = BuildGraph(inputfilepath)
G = bg.buildGraph() # returns a graph object

dcycle = DetectCycle(G)
print (dcycle.cycleExists)
print (dcycle.cycle)
