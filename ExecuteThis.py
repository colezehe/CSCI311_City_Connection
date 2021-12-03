"""
EXECUTE THIS
Main program For testing our algorithms
"""

from OutputGraph import *
from Graph import *
from Kruskal import *
from Prim import prim
import sys
import os.path

# Default files
inputFile = "SanJoaquin.txt"
outputFile = "output.txt"

# Handle standard interface's input
if len(sys.argv) >= 2:
    # Check if input file exists
    if os.path.isfile(sys.argv[1]):
        inputFile = sys.argv[1]
    else:
        print(f"Given input file does not exist! Using default: {inputFile}")
if len(sys.argv) >= 3:
    # Assign output file name
    outputFile = sys.argv[2]
name, extension = outputFile.split(".")
outputFileKruskal = ".".join([name+"Kruskal", extension])
outputFilePrim = ".".join([name+"Prim", extension])
    

# Using Kruskal
g = Graph(inputFile)
g = Kruskal(g)
OutputGraph(outputFileKruskal, g)
print(f"Successfully ran Kruskal and wrote output to {outputFileKruskal}")

# Using prim's
g = Graph(inputFile)
g = prim(g)
OutputGraph(outputFilePrim, g)
print(f"Successfully ran Prims and wrote output to {outputFilePrim}")

# DEFUNCT CODE BELOW

# File name of in/output txt files
#inputFile = input("Where are the edges located?\n")
#inputFile = inputFile if inputFile.strip() != "" else DEFAULT_INPUT
#outputFile = input("Where will the output file located?\n")
#outputFile = outputFile if outputFile.strip() != "" else DEFAULT_OUTPUT
