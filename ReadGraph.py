"""
READ GRAPH
Project: CSCI 311 City Connection
Description: 

Input - f = Data File Name
Output - Graph (of class found in Graph.py)
"""

from Graph import *

def ReadGraph(f):
    # Turn txt file into readable string
    data = open(f, 'r').read()

    # Split into list of edge data lines
    data = data.split("\n")

    # Find total number of vertices (not sure if correct)
    lastEdge = data[len(data)-2].split(" ")
    numVertices = lastEdge[0]

    # Graph initialized
    g = Graph(numVertices)

    # Loop thru each edge
    for line in data:
        # Get individual edge's data
        edge = line.split(" ")

        # Add edge from line data into graph
        if len(edge) >= 4:
            g.addEdge(edge[1], edge[2], edge[3])

    # Return the final graph
    return g