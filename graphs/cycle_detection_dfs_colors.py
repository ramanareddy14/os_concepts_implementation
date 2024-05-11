
"""
Detecting cycle in a undirected graph: using colors
    Depth first search can be used to detect cycles in a graph
    
WHITE : 
    Vertex is not processed yet. Initially, all vertices are WHITE.
GRAY: 
    Vertex is being processed (DFS for this vertex has started, 
    but not finished which means that all descendants (in DFS tree) of this vertex are not processed yet 
    (or this vertex is in the function call stack)
BLACK : 
    Vertex and all its descendants are processed. While doing DFS, if an edge is encountered from current vertex to a GRAY vertex, 
    then this edge is back edge and hence there is a cycle. 
    
    
Algorithm:  

1. Create a recursive function that takes the edge and color array (this can be also kept as a global variable)
2. Mark the current node as GREY.
3. Traverse all the adjacent nodes and if any node is marked GREY then return true as a loop is bound to exist.
4. If any adjacent vertex is WHITE then call the recursive function for that node. If the function returns true. Return true.
5. If no adjacent node is grey or has not returned true then mark the current Node as BLACK and return false.

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity :O(V). 
Since an extra color array is needed of size V.
"""


class Graph:
    def __init__(self):
        self.graph = {}
    
    def print(self):
        print(self.graph)
        
    def addEdge(self,v1,v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        
        self.graph[v1].append(v2)
        
    def DFSutil(self,idx,color):
        '''
        we are beginning processing this idx so color it grey 
        processing this vertex has started and not ended(or this vertex is still in function stack)
        '''
        color[idx] = 'grey'
        
        for neighbour in self.graph[idx]:
            
            if color[neighbour] == 'grey':
                print('cycle exists between {} and {}'.format(idx,neighbour))
                return True
            if color[neighbour] == 'white' and self.DFSutil(neighbour, color) == True:
                return True
            
        color[idx] = 'black'
        return False
            
        
    
    def isCyclic(self):
        color = ['white']*len(self.graph)
        '''
        all nodes are colored white initially since they are not processed
        then 
        '''
        iscyclic = False
        for i in self.graph:
            if color[i] == 'white':
                if self.DFSutil(i,color) == True:
                    iscyclic = True
        return True if iscyclic else False
    
    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
    

g.print()
print ("Graph contains cycle" if g.isCyclic() == True else "Graph doesn't contain cycle")