# -*- coding: utf-8 -*-
"""
The process of rearranging the heap by comparing each parent with its children recursively is known as heapify
"""


def max_heapify(List, i = 0):
    """
    Limitations of this heapify:
        1. This will only heapify current element when it is smaller than children
            - in this case 0,1,3 ( 0 > 1,3  heapify stops without finding largest in rest of array
                                  and there could exist nodes 4,5,6 > 0 after heapify)
        2. We can heapify index i only if all elements in both left and right subtrees are following heap property
    
    
    Bounderies:
        1. When current element is greater than it's children it will stop
        2. When the node is leaf node, it won't pass the child check and Largest remains i and stops
        
    Time Complexity  : O(Log N)
    Space Complexity : O(log N)  since we are using recursion for childs
        
    """
    Left  = i*2 +1
    Right = i*2 +2
    Largest = i
    
    # comparing with left child, right child and current element
    # swap the largest of the three(parent, L_child, R_child) 
    if Left < len(List) and List[Left] > List[i]:
        Largest = Left
    elif Right < len(List) and List[Right] > List[Largest]:
        Largest = Right
        
    
    if Largest != i:
        List[i], List[Largest] = List[Largest], List[i]
        max_heapify(List, Largest)
        
    
def max_heapify_itr(List,i=0):
    
    Left = i*2+1
    Right = i*2+2
    Largest = i
    """
    Stop when base conditions:
        1. current node is leaf node
        2. current node is greater than child nodes
        
    Time Complexity  : O(Log N)
    Space Complexity : O(1)  Greatly reduced for iterative method than recursive method
    """
    
    while Left < len(List):
        """ for complete B.Tree checking left tree is sufficient to make sure it is not leaf node """
        if Left < len(List) and List[Left] > List[i]:
            Largest = Left
        elif Right < len(List) and List[Right] > List[Largest]:
            Largest = Right
            
        
        if Largest != i:
            List[i], List[Largest] = List[Largest], List[i]
            i = Largest
            Left = i*2+1
            Right = i*2+2
            
        else:
            # met second base condition so breaking out of loop and stopping
            break
        
def build_max_heap(List):
    """
    PreReq:
        Heapify Algo
    If given an array, we want to build a max heap:
        Leaf node will always follow the heap property(max/min), 
        So only nodes we need to take care of are internal nodes ( 0 to [N/2]-1)
        
        If we need to apply heapify at index i , it's left and right subtrees should already be a heap
        so We should start heapifying from last internal node till 0th node
        
    Time Complexity :  
            in worst case we are moving from node to root which is LogN
            and we are doing for all nodes (N/2)
            
            O(N) 
    """
    for i in range((len(List)//2 -1), -1, -1):
        max_heapify_itr(List,i)
    
    
"""
Extract max: Remove the max element and get it
    Save the max val --> arr[0]
    remove last element (bottom left most in tree) (last node in array representation) and place at the root
    heap_size -= 1
    max_heapify root
    
    Note : we can keep on extracting, we will get elements in descending order
    Time : O(LogN)
    Space:   recursive - O(LogN), iterative - O(1)
    
Increase Key: On increasing a node value in a max_heap, node may move up to maintain max_heap property
    1. Update node value, this node value may increase more than parent
    2. compare with parent and swap if needed, continue unil node < parent or node becomes root(i==0)
    applyin percolare up algorithm
    
    Time : O(Log N), in worst case we will move from leaf to root node with h = LogN for complete B.Tree

Decrease Key:
    if we decrease value of a key in max_heap, this node may move down to maintain max_heap property
    1. Decrease the node
    2. so simply apply max_heapify this node
    
Insert element:
    1. in a complete B.Tree insert elements at last level from left to right (last index in array representation)
    2. Percolate up fill , same as increase key algo
    

-------------------------
HEAP_PUSH: Inserting element:
    Capacity, Size 
    if size < capacity  follow insert_element algorithm
        insert element at the end and do percolare up algorithm
        
HEAP_POP: same as extracting max:
    size -= 1
    



"""
    
    
    
arr = [18, 11, 13, 5, 6, 7]

build_max_heap(arr)

print(arr)