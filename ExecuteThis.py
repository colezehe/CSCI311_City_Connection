"""
EXECUTE THIS
Main program For testing our algorithms
"""

from OutputGraph import *
from Graph import *
from Kruskal import *


DEFAULT_INPUT = "SanJoaquin.txt"
DEFAULT_OUTPUT = "output.txt"


# File name of in/output txt files
inputFile = input("Where are the edges located?\n")
inputFile = inputFile if inputFile.strip() != "" else DEFAULT_INPUT
outputFile = input("Where will the output file located?\n")
outputFile = outputFile if outputFile.strip() != "" else DEFAULT_OUTPUT

# Read in graph from data file
g = Graph(inputFile)

# Get MST from Kruskal's Algorithm
g = Kruskal(g)

# Output Final Graph
OutputGraph(outputFile, g)
print(f"Successfully wrote graph to {outputFile}")

