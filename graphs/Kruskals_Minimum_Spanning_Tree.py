# -*- coding: utf-8 -*-

""" This is a simple algorithm
Krushkal minimum spanning tree: this is a greedy algorithm which make use DisJoint Set

Steps:
    1. Given edges list(as representation of graph), sort all the edges in Non-decreasing(ascending) order of the weight
    2. continue until v-1 edges are formed
        a. pick the smallest edge
        b. check if the new edge forms a cycle in our spanning tree being formed(DSUF) -- disjoint set union find 
        c. if cycle is not formed --> include edge, else --> discard the edge
    
    
    TIme complexity : sorting edges according to weight + for each edge check if it causes a cycle
                        ElogE                           + E log V
                    O(ElogE + E logV)
                    
                    

DSUF: Disjoint set or Union Find to Detect cycle in Undirected Graph

Node        0     1      2
Parent  	-1	 -1	  -1


"""
class Graph_UF:
    
    def __init__(self,vertices):
        self.V = vertices
        self.graph = {}
        
    def addEdge(self,u,v):
        
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
    # A utility function to find the subset of an element i
    def find_parent(self,parent, i):
        if parent[i] == -1:
            # this node is itself a set
            return i
        
        if parent[i]!= -1:
            return self.find_parent(parent,parent[i])
        
     # A utility function to do union of two subsets
    def union(self, parent,x, y):
        parent[x] = y
        
    # DSUF method to find whether a given graph contains a cycle or not
    def isCyclic(self):
        
        #allocate memory for creating V subsets and 
        #Initialize all subsets as single element sets
        parent = [-1]*self.V
        
        
        # iterate through all edges of graph, find subset of both vertices of every single edge
        # if both subsets are same, then there is a cycle in graph
        for i in self.graph:
            for j in self.graph[i]:
                # for each edge
                x = self.find_parent(parent,i)
                y = self.find_parent(parent,j)
                
                
                if x == y:
                    return True
                
                self.union(parent,x,y)
                
                
                
        
# Create a graph given in the above diagram
g = Graph_UF(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 2)
 
if g.isCyclic():
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")         
                
                
        
        
class Krushkal:
    
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [] # list to store edges and it's weight
        
        # for Union find only
        # initially every vertex is a set itself 
        self.parent = [-1]* self.vertices
        
        # for DSUF with union by rank and path compression
        # in addiion to parent array we need to have a rank array
        self.rank   = [0]*self.vertices
        
    def addEdge(self,u,v,weight):
        self.graph.append([u,v, weight])
        
    
    
    def find(self,node):
        if self.parent[node] == -1:
            return node
        return self.find(self.parent[node])
    
    
    def union(self, u,v):
        # assign one of u.v as parent as another
        self.parent[u] = v
        
    def union_rank(self,x,y):
        print('union rank is used')
        xroot = self.find( x)
        yroot = self.find( y)
  
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
  
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
    
    def KruskalMST(self):
        
        
        # this will store the edges of graph if they are not forming a cycle
        result = []
        
        
        # Step 1 : sort the edges in ascending order of weights
        self.graph = sorted(self.graph, key = lambda item : item[2])
        
        
        # step 2: for each edge if the new edge doesn't form a cycle 
        # add it to result else discard it
        # continue this step until we have V-1 edges
        e  = 0
        i=0
        while e < self.vertices-1:
            
            u,v,w = self.graph[i]
            
            
            x = self.find(u)
            y = self.find(v)
            
            # if u and v belong to same set then there is cycle
            # so we shouldn't include that edge which forms a cycle
            
            if x == y:
                pass
            else:
                e +=1
                result.append(self.graph[i])
                # only change from Union find and rank&path compression
                # Is usage of union with rank
                #self.union(u, v)
                self.union_rank(u,v)
            
            i+=1
        
        
        min_cost = 0
        print("Edges in the MST constrcted by Krushal using UF")
        for u,v,weight in result:
            min_cost += weight
            print("{}--{}    {}".format(u,v,weight)) 
                  
        print(" minimum cost is {}".format(min_cost))
    
    
# Driver code
g = Krushkal(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
  
# Function call
g.KruskalMST()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

