#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:35:51 2021

@author: krl010
"""

# A Python program for Prims's MST for
# adjacency list representation of graph
# code modified from https://cppsecrets.com/users/1032115979910410511011497115116111103105505149484957575564103109971051084699111109/Python-Implementation-of-Prims-Minimum-Spanning-Tree.php

def createAdjMatrix(V, G):
    
    V = G.numVertices;
    
    adjMatrix = []
    #create N x N matrix filled with 0 edge weights between all vertices
    for i in range(0, V):
        adjMatrix.append([])
        for j in range(0, V):
            adjMatrix[i].append(0)
    #populate adjacency matrix with correct edge weights
    for i in range(0, len(G.graph)):
        adjMatrix[G.graph[i][0]][G.graph[i][1]] = G.graph[i][2]
        adjMatrix[G.graph[i][1]][G.graph[i][0]] = G.graph[i][2]
    return adjMatrix

def prims(G):
    
    V = G.numVertices
  # create adj matrix from graph
    adjMatrix = createAdjMatrix(V, G)
    #arbitrarily choose initial vertex from graph
    vertex = 0
    #initialize empty edges array and empty MST
    MST = []
    edges = []
    visited = []
    minEdge = [None,None,float('inf')]
    #run prims algorithm until we create an MST
    #that contains every vertex from the graph
    while len(MST) != V-1:
        #mark this vertex as visited
        visited.append(vertex)
        #add each edge to list of potential edges
        for r in range(0, V):
            if adjMatrix[vertex][r] != 0:
                edges.append([vertex,r,adjMatrix[vertex][r]])
     #find edge with the smallest weight to a vertex
        #that has not yet been visited
        for e in range(0, len(edges)):
            if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                minEdge = edges[e]
     #remove min weight edge from list of edges
        edges.remove(minEdge)
        #push min edge to MST
        MST.append(minEdge)
        #start at new vertex and reset min edge
        vertex = minEdge[1]
        minEdge = [None,None,float('inf')]
    return MST
