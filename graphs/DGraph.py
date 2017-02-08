class DGraph(object):
    """
    Directed graph - adjacency list representation using dictionaries
    node_neighbors[node] = {}, the value pointed to by each node is also a dictionary.
    This dictionary represents its adjacent nodes along with the edge weights.
    Example: node_neighbors[u][v] = wt --> weight of edge (u,v) in the graph is wt.
    Each edge is represented as a tuple (u,v)
    """

    DEFAULT_WEIGHT = 1

    # node_neighbors is the adjacency list
    def __init__(self, nnodes, nedges):
        self.node_neighbors = {}
        self.nnodes = nnodes # number of nodes in G, dummy variable (never used)
        self.nedges = nedges # number of edges in G, dummy variable (never used)

    def graphToString(self):
        # String representation of the graph
        s = str(self.V()) + " vertices, " + str(self.E()) + " edges\n"
        for node in self.nodes():
            s += str(node) + ": "
            for w in self.out_adj(node):
                s += "(%s, %s) " %(str(w), str(self.get_edge_weight((node,w))))
            s += "\n"
        return s

    def E(self):
        # returns the number of edges in G
        total_edges = 0
        for node in self.nodes():
            total_edges += self.out_degree(node)
        return total_edges

    def edges(self):
        # returns a list of edges in G
        edge_list = []
        for u in self.nodes():
            edges = [(u,v) for v in self.out_adj(u)]
            edge_list.extend(edges)
        return edge_list
    
    def countSelfLoops(self):
        # returns the count of self-loops in G
        count = 0
        for u in self.nodes():
            for v in self.out_adj(u):
                if u == v:
                    count += 1
        return count

    def has_edge(self, edge):
        # returns a boolean to indicate whether edge exists in G
        u,v = edge
        return v in self.node_neighbors.get(u, [])

    def V(self):
        # returns the number of nodes in G
        return len(self.node_neighbors)

    def nodes(self):
        # returns a list of nodes in G
        return list(self.node_neighbors.keys())

    def has_node(self, v):
        # returns a boolean to indicate whether v exists in G
        return v in self.node_neighbors

    def in_degree(self, v):
        # return the in-degree of the node v
        in_degree = 0
        for node in self.nodes():
            if v in self.out_adj(node):
                in_degree += 1
        return in_degree

    def out_degree(self, v):
        # returns out-degree of the node v
        return len(self.out_adj(v))

    def out_adj(self, v):
        # returns a list of nodes out adjacent to v in G
        if not self.has_node(v):
            raise Exception("Node %s not present in G" % str(v))
        return list(self.node_neighbors[v].keys())

    def in_adj(self, v):
        in_adj_list = []
        # returns a list of nodes in adjacent to v
        if not self.has_node(v):
            raise Exception("Node %s not present in G" % str(v))
        for node in self.nodes():
            if v in self.out_adj(node):
                in_adj_list.append(node)
        return in_adj_list
    
    def add_edge(self, edge, wt=DEFAULT_WEIGHT):
        # add the edge, here edge is a tuple (u,v)
        u, v = edge
        if self.has_edge(edge):
            raise Exception("Edge %s already present in G, parallel edges not allowed" % str(edge))

        # add the end-points of the edge and then the edge
        if not self.has_node(u):
            self.add_node(u)
        if not self.has_node(v):
            self.add_node(v)
        self.node_neighbors[u][v] = wt

    def add_nodes(self, nodes):
        # takes a list of nodes as input and adds them to G
        for node in nodes:
            self.add_node(node)

    def add_node(self, v):
        # add the node v in G
        if self.has_node(v):
            raise Exception("Node %s already present in G" % str(v))
        self.node_neighbors[v] = {}

    # Delete methods
    def del_node(self, v):
        # delete the node v from G
        if not self.has_node(v):
            raise Exception("Node %s not present in G" % str(v))
        # delete the out-going edges
        for w in self.out_adj(v):
            self.del_edge((v,w))
        # delete the in-coming edges
        for w in self.in_adj(v):
            self.del_edge((w,v))
        del self.node_neighbors[v]

    def del_edge(self, edge):
        # delete the edge from G
        u,v = edge
        if not self.has_edge(edge):
            raise Exception("Edge %s not present in G" % str(edge))
        del self.node_neighbors[u][v]

    # Methods to set properties of nodes and edges
    def set_edge_weight(self, edge, wt):
        # set the weight of the edge
        u,v = edge
        if not self.has_edge(edge):
            raise Exception("Edge %s not present in G" % str(edge))
        self.node_neighbors[u][v] = wt

    def get_edge_weight(self, edge):
        # return the weight of the edge
        u,v = edge
        if not self.has_edge(edge):
            raise Exception("Edge %s not present in G" % str(edge))
        return self.node_neighbors[u][v]

    def get_edges(self):
        # return a list of all edges and their weights, ver 2
        edge_list = []
        unique_list = set()
        for u in self.nodes():
            for v in self.out_adj(u):
                if (u,v) not in unique_list:
                    edge_list.append((self.node_neighbors[u][v], (u, v)))
                    # add edges (u,v) and (v,u) to the set of edges
                    unique_list.add((u,v))
        return edge_list

'''   
G = DGraph()
G.add_nodes(['a', 'b', 'c'])
G.add_edge(('a','b'), 3)
G.add_edge(('a','a'), 8)
G.add_edge(('a','c'), 5)
G.add_edge(('c','b'), 4)
#G.set_edge_weight(('c','b'), 10)
#G.del_node('a')
#print(G.graphToString())
#print (G.get_edge_weights())
#print (G.get_edges())
print (G.max_degree())
print (G.numberOfSelfLoops())
print (G.E())
'''
