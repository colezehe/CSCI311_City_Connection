"""
OUTPUT GRAPH
Outputs a graph in specified format

Inputs - outputFile = file name for output to go
        g = graph to be sent as output
"""

from Graph import *

def OutputGraph(outputFile, g):
    # Open output file to be written to
    file = open(outputFile, "w")
    # Keep track of unique ID
    i = 0
    # Go thru each edge in the output graph
    for u, v, w in g.graph:
        # Add edge to output
        file.write('{} {} {} {}\n'.format(i,u,v,w))
        # Increment edge index
        i += 1