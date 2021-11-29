"""
EXECUTE THIS
Main program For testing our algorithms
"""

from OutputGraph import *
from ReadGraph import *
from Kruskal import *

# CHANGE THIS EVENTUALLY
# File name of in/output txt files
inputFile = "SanJoaquin.txt"
outputFile = "output.txt"
# Read in graph from data file
g = ReadGraph(inputFile)

# Get MST from Kruskal's Algorithm
g = Kruskal(g)

# Output Final Graph
OutputGraph(outputFile, g)