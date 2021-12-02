"""
GRAPH
Project: CSCI 311 City Connection
Description: Data Structure to represent a graph in our algorithms
Resources: geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""

class Graph:
    # Initializes a new graph
    # input f = input file name
    def __init__(self, f=None):
        self.graph = []
        if f:
            self.read_graph(f)

    def read_graph(self, f):
        # Turn txt file into readable string
        data = open(f, 'r').read()
        # Split into list of edge data lines
        data = data.split("\n")
        # Keep track of largest vertex ID
        numVertices = 0
        # Loop thru each edge
        for line in data:
            # Get individual edge's data
            edge = line.split(" ")
            # Add edge from line data into graph
            if len(edge) <= 1:
               continue
            elif len(edge) >= 4:
                self.addEdge(edge[1], edge[2], edge[3]) 
                # Update the highest vertex ID / total num vertices
                if int(edge[1]) > numVertices:
                    numVertices = int(edge[1])
                if int(edge[2]) > numVertices:
                    numVertices = int(edge[2])
            else:
                raise Exception(f"Edge case: {edge}")
        self.numVertices = numVertices + 1 # Id counts from zero?
 
    # Adds an edge to the graph
    def addEdge(self, u, v, w):
        self.graph.append([int(u), int(v), float(w)])
 
    # Finds element i
    def find(self, parent, i):
        assert i < len(parent), f"Finding nonexistent index {i} "+\
                                f"in parent of size {len(parent)}"
            
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # Unions two sets
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
 
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
 
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
