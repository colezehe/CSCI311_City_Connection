"""
GRAPH
Project: CSCI 311 City Connection
Description: Data Structure to represent a graph in our algorithms
Resources: geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""

class Graph:
    # Initializes a new graph
    def __init__(self, numV):
        self.graph = []
        self.numVertices = int(numV)
 
    # Adds an edge to the graph
    def addEdge(self, u, v, w):
        self.graph.append([int(u), int(v), float(w)])
 
    # Finds element i
    def find(self, parent, i):
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