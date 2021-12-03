#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:35:51 2021

@author: tst008
"""

# A Python program for Prims's MST for
# adjacency list representation of graph
# code modified from https://cppsecrets.com/users/1032115979910410511011497115116111103105505149484957575564103109971051084699111109/Python-Implementation-of-Prims-Minimum-Spanning-Tree.php

from Graph import Graph
from PriorityQueue import PQBinaryHeap

class Node:
    def __init__(self, val):
        self.val = val
        self.weight = None
        self.next = None 
        
    def __repr__(self):
        return f"{self.val}({self.weight})->" + str(self.next)

def createAdjList(V, G):
    
    V = G.numVertices
    adjList = [Node(u) for u in range(V)]
    for i in range(len(G.graph)):
        u, v, w = G.graph[i]
        
        node = Node(v)
        node.weight = w
        
        temp = adjList[u].next
        adjList[u].next = node
        node.next = temp
        
        node = Node(u)
        node.weight = w
        
        temp = adjList[v].next
        adjList[v].next = node
        node.next = temp
    return adjList


