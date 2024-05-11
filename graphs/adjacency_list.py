"""
     DFS                                                                                                        

    a ---> c                                 a ---> c                                                                    
    |      |                                 |      |                                                                  
    ↓      ↓                                 ↓      ↓                                                                     
    b <-- e                                  b <-- e                                                                    
    |                                        |                                                            
    ↓                                        ↓                                                            
    d <-- f                                  d <-- f                                                                  
    
 a, b, d                                    a, b, c 
 
 Explore one direction                     Explore all of immediate neighbours
 as fas as possible                        Then for each neighbour expolore it's neighbours
 before switching direction
 
 USES: Stack                                 QUEUE

"""

"""
Graph with adjacency list is represented by usinga graph
with nodes as keys and the connected nodes to it as value list
"""

# directed map 
graph = {
    'a' : ['c', 'b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : [] 
    }

graph2  = {
    
    
    
    }

def depthfirstsearch(graph,current):
    """
    """
    stack = []
    stack.append(current)
    visited = set()
    
    print('Depth first traversal of graph: ',end='')
    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
             print(current,' ',end='')
             visited.add(current)
             
        path_list = graph[current]
        for each in path_list:
            if each not in visited:
                stack.append(each)
            
    print('')
    
def breadthfirstsearch(graph, current):
    queue = []
    queue.append(current)
    visited=set()
    
    print("Breadt first traversal of graph ", end='')
    while len(queue) >0:
        current = queue.pop(0)
        if current not in visited:
            print(current,'',end='')
            visited.add(current)
        
            path_list = graph[current]
            for each in path_list:
                if each not in visited:
                    queue.append(each)
    print('')
    

def depthfirstsearch_recursive(graph, vertex):
    
    print(vertex, end=' ')
    for connected in graph[vertex]:
        depthfirstsearch_recursive(graph, connected)
        

"""
E- edges, worst cast E= N^2
n- nodes
Time  : O(E)
SPACE : O(n)
"""
def find_two_vertices_are_connected(graph,v1,v2):
    
    pass

depthfirstsearch(graph,'a')  # acebdf
breadthfirstsearch(graph,'a') # acbedf
depthfirstsearch_recursive(graph, 'a')


# ---------------------------------------------------------------------------
print("\n\n","Given only edges".center(60,'*'))
"""
given edges list, convert into adjacency list 

define an empty graph to represent adjacent list
for every edge check if the two vertices are present in graph else add these vertices to graph
and if edge is not present append to the vertice value
"""

"""
    l<--k-->i-->j
        ↑
        m

   o -- >n        

This graph is unconnected graph 
to traverse such graph we need to start from every vertex and keep track of visited nodes
"""
edges = [     ['i','j'], ['k','i'], ['m','k'], ['k','l'], ['o','n']    ]

edges_adl = {}

def convert_edges_to_graph(graph, edges, undirected = False):
    
    for edge in edges:
        v1,v2 = edge
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
            
        if v2 not in graph[v2]:
            graph[v1].append(v2)
        
        # for undirected graph a -- b, can be travelled from both directions
        if undirected == True :
            graph[v2].append(v1)


def breadthfirstsearch_unconnected(graph):
    
    visited = set()
    stack = []
    islands = 0
    max_area = 0
    min_area = float('inf')
    print('\nDepth first traversal of unconnected graph: ',end='')
    
    for vertex in graph:
        if vertex not in visited:
            stack.append(vertex)
            this_island_area = 0
            
            print('\n\t\t',end='') # this is a separater for each unconnected graph
            islands +=1
            while len(stack) > 0:
                current = stack.pop()
                
                this_island_area+=1
                max_area = max(max_area, this_island_area)
                
                if current not in visited:
                     print(current,' ',end='')
                     visited.add(current)
                     
                path_list = graph[current]
                for each in path_list:
                    if each not in visited:
                        stack.append(each)
            min_area = min(min_area, this_island_area)
                    
    print("\nnumber of islands in the graph are : {} and island with max area : {}, island with min area : {}".format(islands, max_area, min_area))


convert_edges_to_graph(edges_adl, edges, True)
print(edges_adl)
breadthfirstsearch_unconnected(edges_adl)


# ---------------------------------------------------------------------------
print('\n\n',"Shortest Path".center(60,'*'))
"""
        w --  x --  y -- z
        \               /
            v
path between w and x

DFS :   
    Depth first foreces to look forwared in one direction as fas as possible, 
    DFS could be unlucky in maze traversal and end up traversing in wrong path and traverse all the paths
    
BFS:
    it will explore all directions evenly
    It will explore all nodes at each level away  
    
    Implementations:
        using queue, not only node also store the directions
        so we know a node is at what distance from given node
        
    Timecomplexity
"""
edges_2 = [  ['w','x'], ['x','y'],['y','z'], ['z','y'], ['z','v'],['w','v']]
graph3 = {}

def find_min_distance(graph, origin, destination):
    # using queue and BFS 
    visited = set()
    queue  = []
    
    queue.append([origin,0])
    
    while len(queue) >0:
        node, dist  = queue.pop(0)
        if (node == destination):
            print("the node is found at a minimum distance of {}".format(dist))
            return
        
        if node not in visited:
            visited.add(node)
            
            for neighbour in graph[node]:
                queue.append([neighbour, dist+1])
                
    return -1


convert_edges_to_graph(graph3,edges_2,undirected=True)
find_min_distance(graph3, 'w','z')

