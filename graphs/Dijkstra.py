# -*- coding: utf-8 -*-
"""
Dijkstra algorithm: This is for a directed graph
    Given a graph, find shortest path from a Source to all other vertices
    
Single Source Shortest path Graph (SSSPG)

Algorithm
	• Maintain a set of processed nodes ()
	• Assign all nodes with distance inf except source node (0)
	• Repeat following (Unless all vertices are included) (this also contains only V-1 edges)
		○ Update all the adjacent node distances which is not already processed(visited)
			§ If new dist < old distance update distance 
		○ Pick min value vertex which is not already processed
		○ Include this selected node in processed set    
        
IMPLEMENTATION:
	We need to keep track of visited and not visited  (array for sequential vertices 0-n) or use a set
	To maintain distance of nodes we can use an array (if sequential )  if not sequential use a map
	To remenber SPG we need to store edges in parent-child relationship,; parent[v] = u
	

"""



class dijkstra:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
        
        '''
        since the vertices are sequential we could use array's to store parent, it's value
        if we have non suquential nodes we could use set or map
        '''
        # after finding the shortest path to every node we can update the parent of that node
        self.parent = [-1]*self.vertices
        
        # initially every node is assigned distance inf, except the source node which will be 0
        self.value = [float('inf')]*self.vertices
        
        # we need to keep track of which nodes are already processed
        self.visited = [False]*self.vertices
    
    
    
    def dijkstra(self, source):
        
        # mark this source vertex as distance 0 since we begin from this node
        self.value[source] = 0
        
        # for all the neighbours of source node
        for nei in range(self.vertices):
            # if this is a neighbour which is not processed
            if source != nei and self.graph[source][nei] != 0 and self.visited[nei] == False:
                # update the neighbours shortest path distance and include the min node
                    
            
    
    




# Driver program
g = dijkstra(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
g.dijkstra(0);