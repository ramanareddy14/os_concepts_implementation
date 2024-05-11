# -*- coding: utf-8 -*-
"""
Spanning Tree and minimum spanning tree

Spanning Tree: 
    which can Cover all vertices with min possible edges
    St is a subset of a graph ()
    St cannot be disconnected (disconnectd graph we can never able to cover all the vertices)
    Graph should be single-component
    
    No of vertices = V
    no of edges    = V-1  (no of vertices -1 always)
    
    we don't have any cycles in a ST
    All STs will have same number of edges
    A connected and undirected graph has atleast 1ST
    A complete undirected graph has N^(N-2) no of different ST's possible (N is number of vertices)
    A ST is minimally connected ie. removing 1 edge will disconnect the graph
    A ST is maximally Acyclic ie. adding 1 edge will form a cycle in graph
    
    
Minimum spanning Tree:
    A spnning tree with min cost in a weighted graph is called MST(cost = cost of all edges)
    There can be more than one MST
    
APPLICATIONS:
    Design network cable route for cities using minimum cable, hence minimizing cost
    Design water supply n/w, transportation n/w etc, read wiki

Popular Algos
    Prims
    Kushkal
"""

st2 = \
'''****************************************************************************
Prims : this is a greedy type MST finding algorithm
    Goal 1: cover all vertices
    Goal 2: cover with minimum cost
    
1. select min value option first

Steps:
    All node weights are inf except source , since we need to select source first
    1. Select Node with min-weight (start at source)
    2. include selected node in setMST
    3. Relax/compure all adjacent edges
    -----repeat  -->1-->2-->3-->  unless all vertices are included in MST
    
notes:
    We started from node 0 and we are expanding only adjacently and not randomly(like kruskals)
    
Requirements:
    We need to keep track of weight values for all nodes  : use array (size V)
    we nned to know what vertices are included in MST      : boor array (size V)
    We need to remember edges of MST to print finally     : parent array (size V)
        a. Pick a vertex u which is not there in mstSet and has a minimum key value. 
        b. Include u to mstSet. 
        c.Update key value of all adjacent vertices of u. To update the key values, 
            iterate through all adjacent vertices. For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value as the weight of u-v
    
                0   1     2     3     4    5
    dist    :   0  inf   inf   inf   inf  inf
    mstSET  :   F   F     F     F     F    F
    parent  :  -1
    
either use ADJ-list or ADJ-matrix

The Time Complexity of the above program is O(V^2). 
If the input graph is represented using adjacency list, then the time complexity of Prim’s algorithm can be reduced to 
O(E log V) with the help of a binary heap. 
  
'''
import sys

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
        
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
  
        # Initialize min value
        min = sys.maxsize
  
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
  
        return min_index
    
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print ("Edge \t\tWeight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][parent[i]])
        
    def primMST(self):
        
        # Key values used to pick minimum weight edge in cut
        # Make key 0 so that this vertex is picked as first vertex
        key = [sys.maxsize]*(self.V)
        key[0] = 0
        
        # Array to store constructed MST
        parent = [None] * self.V 
        parent[0] = -1 # First node is always the root of
        
        mstSet = [False] * self.V
        
        # form MST with V-1 edges
        for cout in range(self.V):
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed (not yet included in the shortest path tree). 
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
        
            # Put the minimum distance vertex in 
            # the shortest path tree
            mstSet[u] = True
            
            for v in range(self.V):
                
                if self.graph[u][v] != 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    
        self.printMST(parent)
            
        

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
  
g.primMST();