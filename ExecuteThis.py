"""
EXECUTE THIS
Main program For testing our algorithms
"""

from ReadGraph import *
from Kruskal import *

# Read in graph from data file
g = ReadGraph("SanJoaquin.txt")

# Get MST from Kruskal's Algorithm
Kruskal(g)

# Output Final MST