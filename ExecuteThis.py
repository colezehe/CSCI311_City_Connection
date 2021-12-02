"""
EXECUTE THIS
Main program For testing our algorithms
"""

from OutputGraph import *
from Graph import *
from Kruskal import *
import sys
import os.path

# Default files
inputFile = "SanJoaquin.txt"
outputFile = "output.txt"

# Handle standard interface's input
if len(sys.argv) >= 3:
    # Check if input file exists
    if os.path.isfile(sys.argv[1]):
        inputFile = sys.argv[1]
    else:
        print(f"Given input file does not exist! Using default: {inputFile}")
    # Assign output file name
    outputFile = sys.argv[2]

# Read in graph from data file
g = Graph(inputFile)

# Get MST from Kruskal's Algorithm
g = Kruskal(g)

# Output Final Graph
OutputGraph(outputFile, g)
print(f"Successfully wrote graph to {outputFile}")


# DEFUNCT CODE BELOW

# File name of in/output txt files
#inputFile = input("Where are the edges located?\n")
#inputFile = inputFile if inputFile.strip() != "" else DEFAULT_INPUT
#outputFile = input("Where will the output file located?\n")
#outputFile = outputFile if outputFile.strip() != "" else DEFAULT_OUTPUT