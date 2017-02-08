from DGraph import DGraph

class BuildDGraph(object):

    def __init__(self, inputfilepath):
        self.inputfilepath = inputfilepath
    
    def buildDGraph(self):
        # Builds a graph from a given input file
        graph_file = open(self.inputfilepath, 'r')
        # get the number of nodes and edges, first 2 lines in input file
        nnodes = int(graph_file.readline().strip())
        nedges = int(graph_file.readline().strip())
        
        G = DGraph(nnodes, nedges)
        for line in graph_file:
            line = line.strip()
            u, v, wt = line.split()
            # add the edge to G
            G.add_edge((u,v), int(wt))
        graph_file.close()
        return G
