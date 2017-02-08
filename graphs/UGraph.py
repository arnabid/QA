class UGraph(object):
    """
    Undirected graph - adjacency list representation using dictionaries
    node_neighbors[node] = {}, the value pointed to by each node is also a dictionary.
    This 'value' dictionary represents a node's adjacent nodes along with the edge weights.
    Example: node_neighbors[u][v] = wt --> weight of edge (u,v) in the graph is wt.
    Each edge is represented as a tuple (u,v)

    ---Methods---
    Edge methods: E, has_edge, add_edge, del_edge, set_edge_weight, get_edge_weight
    Node methods: V, degree, adj, has_node, add_nodes, add_node, del_node
    General methods: max_degree, avg_degree, edges, nodes, countSelfLoops, graphToString, get_edges
    
    TODO: read a file with the graph input and build the graph
    build the class for a directed graph
    start building graph searching algos.
    """

    DEFAULT_WEIGHT = 1

    # node_neighbors is the adjacency list
    def __init__(self, nnodes, nedges):
        self.node_neighbors = {}
        self.nnodes = nnodes # number of nodes in G
        self.nedges = nedges # number of edges in G

    def graphToString(self):
        # String representation of the graph
        s = "%s vertices, %s edges\n" %(str(self.V()), str(self.E()))
        for node in self.nodes():
            s += str(node) + ": "
            for w in self.adj(node):
                s += "(%s, %s) " %(str(w), str(self.get_edge_weight((node,w))))
            s += "\n"
        return s

    def E(self):
        # returns the number of edges in G
        sum_degree = 0
        for node in self.nodes():
            sum_degree += self.degree(node)
        return sum_degree // 2

    def edges(self):
        # returns a list of edges in G
        edge_list = []
        for u in self.nodes():
            edges = [(u,v) for v in self.adj(u)]
            edge_list.extend(edges)
        return edge_list
    
    def countSelfLoops(self):
        # returns the count of self-loops in G
        count = 0
        for u in self.nodes():
            for v in self.adj(u):
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

    def degree(self, v):
        # returns degree of the node v
        adj_nodes = self.adj(v)
        deg = len(adj_nodes)
        # self-loop adds 2 to the degree of a vertex
        if v in adj_nodes:
            deg += 1
        return deg

    def max_degree(self):
        # returns the maximum degree of all nodes in G
        maxd = 0
        for v in self.nodes():
            maxd = max(maxd, self.degree(v))
        return maxd

    def avg_degree(self):
        # returns the average degree of nodes in G
        return 2 * self.E() / self.V()

    def adj(self, v):
        # returns a list of nodes adjacent to v in G
        if not self.has_node(v):
            raise Exception("Node %s not present in G" % str(v))
        return list(self.node_neighbors[v].keys())

    def add_edge(self, edge, wt=DEFAULT_WEIGHT):
        # adds the edge, here edge is a tuple (u,v)
        u, v = edge
        if self.has_edge(edge):
            raise Exception("Edge %s already present in G, parallel edges not allowed" % str(edge))
        if not self.has_node(u):
            self.add_node(u)
        self.node_neighbors[u][v] = wt
        if u != v:
            if not self.has_node(v):
                self.add_node(v)
            self.node_neighbors[v][u] = wt

    def add_nodes(self, nodes):
        # takes a list of nodes as input and adds them to G
        for node in nodes:
            self.add_node(node)

    def add_node(self, v):
        # adds the node v in G
        if self.has_node(v):
            raise Exception("Node %s already present in G" % str(v))
        self.node_neighbors[v] = {}

    # Delete methods
    def del_node(self, v):
        # deletes the node v from G
        if not self.has_node(v):
            raise Exception("Node %s not present in G" % str(v))
        for w in self.adj(v):
            if w != v:
                self.del_edge((w,v))
        del self.node_neighbors[v]

    def del_edge(self, edge):
        # deletes the edge from G
        u,v = edge
        if not self.has_edge(edge):
            raise Exception("Edge %s not present in G" % str(edge))
        del self.node_neighbors[u][v]

    # Methods to set properties of nodes and edges
    def set_edge_weight(self, edge, wt):
        # sets the weight of the edge
        u,v = edge
        if not self.has_edge(edge):
            raise Exception("Edge %s not present in G" % str(edge))
        self.node_neighbors[u][v] = wt
        if u != v:
            self.node_neighbors[v][u] = wt

    def get_edge_weight(self, edge):
        # returns the weight of the edge
        u,v = edge
        if not self.has_edge(edge):
            raise Exception("Edge %s not present in G" % str(edge))
        return self.node_neighbors[u][v]

    def get_edge_weights(self):
        # return a list of all edges with their weights
        edge_list = []
        unique_list = {}
        for u in self.nodes():
            for v in self.adj(u):
                # check if edge(v,u) has been added
                if u not in unique_list.get(v, set()):
                    edge_list.append((self.node_neighbors[u][v], (u, v)))
                    unique_list.setdefault(u, set()).add(v)
        return edge_list

    def get_edges(self):
        # return a list of all edges and their weights, ver 2
        edge_list = []
        unique_list = set()
        for u in self.nodes():
            for v in self.adj(u):
                if (u,v) not in unique_list:
                    edge_list.append((self.node_neighbors[u][v], (u, v)))
                    # add edges (u,v) and (v,u) to the set of edges
                    unique_list.add((u,v))
                    unique_list.add((v,u))
        return edge_list


'''
G = UGraph(3,6)
print (G.nnodes)
G.add_nodes(['a', 'b', 'c'])
G.add_edge(('d','e'), 3)
G.add_edge(('a','a'), 10)
G.add_edge(('a','c'), 5)
G.add_edge(('c','b'), 4)
G.add_edge(('b', 'b'), 10)
G.add_edge(('c', 'c'), 10)
print (G.E())
print (G.edges())
print (G.countSelfLoops())
print (G.V())
print (G.nodes())
print (G.degree('a'))
print (G.max_degree())
print (G.avg_degree())
print (G.adj('b'))
print (G.has_node('d'))
print (G.has_edge(('d','a')))
'''
