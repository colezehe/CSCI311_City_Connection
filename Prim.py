#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:35:51 2021

@author: krl010
Reviewed by tst008
"""

# A Python program for Prims's MST for
# adjacency list representation of graph
# code modified from https://cppsecrets.com/users/1032115979910410511011497115116111103105505149484957575564103109971051084699111109/Python-Implementation-of-Prims-Minimum-Spanning-Tree.php

from Graph import Graph
from PriorityQueue import PQBinaryHeap
from AdjacencyList import createAdjList
from HashSet import HashSet

def createAdjMatrix(V, G):
    
    V = G.numVertices
    adjMatrix = [[0 for j in range(V)] for i in range(V)]
    #create N x N matrix filled with 0 edge weights between all vertices
#     for i in range(0, V):
#         adjMatrix.append([])
#         for j in range(0, V):
#             adjMatrix[i].append(0)
    #populate adjacency matrix with correct edge weights
    for i in range(0, len(G.graph)):
        adjMatrix[G.graph[i][0]][G.graph[i][1]] = G.graph[i][2]
        adjMatrix[G.graph[i][1]][G.graph[i][0]] = G.graph[i][2]
    return adjMatrix


# def prim(G):
    
#     V = G.numVertices
#   # create adj matrix from graph
#     adjMatrix = createAdjMatrix(V, G)
#     #arbitrarily choose initial vertex from graph
#     vertex = 0
#     #initialize empty edges array and empty MST
#     MST = Graph()
#     edges = []
#     visited = []
#     minEdge = [None,None,float('inf')]
#     #run prims algorithm until we create an MST
#     #that contains every vertex from the graph
#     while len(MST.graph) != V-1:
#         if (len(MST.graph) % 100 == 0):
#             print(f'{len(MST.graph)}/{V}')
#         print(".", end="")
#         #mark this vertex as visited
#         visited.append(vertex)
#         #add each edge to list of potential edges
#         for r in range(0, V):
#             if adjMatrix[vertex][r] != 0:
#                 edges.append([vertex,r,adjMatrix[vertex][r]])
#      #find edge with the smallest weight to a vertex
#         #that has not yet been visited
#         for e in range(0, len(edges)):
#             if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
#                 minEdge = edges[e]
#      #remove min weight edge from list of edges
#         edges.remove(minEdge)
#         #push min edge to MST
#         MST.addEdge(*minEdge)
#         #start at new vertex and reset min edge
#         vertex = minEdge[1]
#         minEdge = [None,None,float('inf')]
#     return MST

def prim(G):
    
    V = G.numVertices
    #arbitrarily choose initial vertex from graph
    vertex = 0
    #initialize empty edges array and empty MST
    MST = Graph()
    pq = PQBinaryHeap(lambda x,y: x[2] < y[2]) # Compare distance
    visited = [False for x in range(V)]
    for i in range(len(G.graph)):
        if G.graph[i][0] == 0:
            pq.push(G.graph[i]) 
        else:
            break
    visited[0] = True
    totalWeight = 0
    #run prims algorithm until we create an MST
    #that contains every vertex from the graph
    while len(MST.graph) != V - 1:
        if (len(MST.graph) % 100 == 0):
            print(f'{len(MST.graph)}/{V}')
        #get minimum edge
        print(pq)
        edge = pq.pop() 
        
        #check if visited
        if visited[edge[0]] and visited[edge[1]]:
            continue
        elif visited[edge[0]]:
            vertex = edge[1]
        elif visited[edge[1]]:
            vertex = edge[0]
                
        visited[vertex] = True
        MST.addEdge(*edge)
        totalWeight += edge[2]
#         print(edge)
#         print(visited)
#         print(vertex)
        
        # Find edges going out from vertex
        # Can reduce further from n to log n + num_edge_per_vertex
        for i in range(len(G.graph)):
            u, v, w = G.graph[i]
#             if u > vertex:
#                 break
            if u != vertex and v != vertex:
                continue
            if v == vertex: # So u is always the vertex
                u, v = v, u
            if visited[v]:
                continue
            else:
                pq.push(G.graph[i])
    print("Total weight:", totalWeight)    
    return MST


def prim(G):
    
    V = G.numVertices
    #arbitrarily choose initial vertex from graph
    vertex = 0
    #initialize empty edges array and empty MST
    adjList = createAdjList(V, G)
    MST = Graph()
    pq = PQBinaryHeap(lambda x,y: x[2] < y[2]) # Compare distance
    visited = [False for x in range(V)]
    for i in range(len(G.graph)):
        if G.graph[i][0] == 0:
            pq.push(G.graph[i]) 
        else:
            break
    visited[0] = True
    totalWeight = 0
    #run prims algorithm until we create an MST
    #that contains every vertex from the graph
    while len(MST.graph) != V - 1:
#         if (len(MST.graph) % 100 == 0):
#             print(f'{len(MST.graph)}/{V}')
        #get minimum edge
#         print(pq)
        edge = pq.pop() 
        
        #check if visited
        if visited[edge[0]] and visited[edge[1]]:
            continue
        elif visited[edge[0]]:
            vertex = edge[1]
        elif visited[edge[1]]:
            vertex = edge[0]
                
        visited[vertex] = True
        MST.addEdge(*edge)
        totalWeight += edge[2]
        
        # Find edges going out from vertex
        node = adjList[vertex]
        while node.next != None:
            if not visited[node.next.val]:
                pq.push([vertex, node.next.val, node.next.weight])
            node = node.next
    print("Total weight:", totalWeight)    
    return MST
