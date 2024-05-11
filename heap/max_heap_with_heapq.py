# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:40:09 2022

@author: raman
"""

import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements

"""
We will be using a heapq(minheap) invert the elements and use this as a maxheap
Operations: 
    1. Init data with a list negate these elements and heapify
    2. retrieve the max element (arr[0])
    3. heappop
    4. heap replace
    5. heap push
    6. print_K_max_elements
"""

class max_heap:
    def __init__(self, data_list = []):
        data_list = [x*(-1) for x in data_list]
        self.data = data_list
        heapq.heapify(self.data)
        
        
    def top(self):
        if len(self.data) != 0:
            return self.data[0]*(-1)
        else:
            return -1
        
    def pop(self):
        top = self.top()
        heapq.heappop(self.data)
        return top
        
    def replace(self,element):
        heapq.heappop(self.data,element)
        
    def push(self,element):
        heapq.heappush(self.data,element)
        
    def print_K_max_elements(self, k):
        print("The first K largest elements are (not necessarily in sorted order) : ", end = '')
        for i in range(k):
            if i < len(self.data):
                print(self.data[i]*-1,' ', end = '')
                

max_h = max_heap(H)

print("top of max_heap :",max_h.top())
max_h.print_K_max_elements(4)

