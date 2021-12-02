"""
KRUSKAL'S ALGORITHM
Project: CSCI 311 City Connection
Description: Represents Kruskal's algorithm for finding Minimum Spanning Tree.
Resources: geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

Input - g = Graph
Output - Resulting MST
"""

from Graph import Graph

def Kruskal(g):
    # The output MST
    mst = Graph()
    # Variables used for sorting
    i = 0
    e = 0

    # Sort all the edges in non-decreasing order
    g.graph = sorted(g.graph, key=lambda item: item[2])

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(g.numVertices):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < g.numVertices - 1:

        # Smallest edge, then increment for next step
        u, v, w = g.graph[i]
        i = i + 1

        try:
            x = g.find(parent, u)
            y = g.find(parent, v)
        except:        
            print(f"parent length: {g.numVertices}, edge:({u},{v})")
            raise

        # If there won't be a cycle, include it
        if x != y:
            e = e + 1
            mst.addEdge(u, v, w)
            g.union(parent, rank, x, y)
        # Else discard the edge
        else:
            pass

    return mst
   
