"""
READ GRAPH
Project: CSCI 311 City Connection
Description: 

Input - f = Data File Name
Output - Graph (of class found in Graph.py)
"""

from Graph import *

def ReadGraph(f):
    # Graph initialized
    g = Graph()

    # Turn txt file into readable string
    data = open(f, 'r').read()

    # Split into list of edge data lines
    data = data.split("\n")

    # Loop thru each edge
    for line in data:
        # Get individual edge's data
        edge = line.split(" ")

        # Add edge from data into graph
        if len(edge) >= 4:
            g.addEdge(edge[1], edge[2], edge[3])

    # Return the final graph
    return g