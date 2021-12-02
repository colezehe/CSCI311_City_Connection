# CSCI311_City_Connection
For the CSCI 311 (Design &amp; Analysis of Algorithms) City Connection Graph Project

Authors: Cole Zehe, Jake Etzler, Tung Tran, Kyle Light

### GitHub Repository
https://github.com/colezehe/CSCI311_City_Connection

### How to Run Our Code
In a command prompt, at directory "CSCI311_City_Connection":
> py ExecuteThis.py inputFile outputFile

For Example:
> py ExecuteThis.py NorthAmerica.txt output.txt

### How to Understand Our Programs

_ExecuteThis.py_
  - Main code for testing out our algorithms
  - Execute / modify this to test our code

_Graph.py_
  - Data Structure for storing a graph
  - init function takes an input file name
  - input file line format: Edge ID, Start Node ID, End Node ID, Length

_Kruskal.py_
  - Contains a version of Kruskal's algorithm
  - Outputs an MST of the input graph

_Prim.py_
  - Contains a version of Prim's algorithm
  - Outputs an MST of the input graph

_HashSet.py_
  - Data structure to represent a Hash set
  - Used for Prim's algorithm

_PriorityQueue.py_
  - Data structure to represent a Priority Queue
  - Used for Prim's algorithm

_OutputGraph.py_
  - Outputs a graph based upon an input graph
  - Format for each line: Edge ID, Start Node ID, End Node ID, Length
