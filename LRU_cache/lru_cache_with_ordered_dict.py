"""
LRU cache is caching the recent accesed(requested) page at the top of list
and when the pages are full when a new page is requested the older page gets ommited
to keep the pages we need a Double linked list / 
to access the pages in linked list faster we keep the indexes of the pages in a hash table
--->when there is a request for a page, lookup in the hash table
         if present move it to top of list and update hash table
         if not present 
                if capacity is full delete the lru and add the new one to top and update hash table
                if capacity is not full add to top and update hash table
                
choice of algos
    for DDL:  use the power of OrderedDict from collections module which keep order of insertion of keys and we can change that order if required
    for hashtable: 
    -here Ordered Dict does the job of Hashing and also keeping the order of pages 
        
"""
from collections import OrderedDict

class lru_cache():
    
    # initializing capacity
    def __init__(self,capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def accesspage(self,page:int):
        if page in self.cache:
            self.cache.move_to_end(page,True)
            self.printc()
            return -1
        if len(self.cache) == self.capacity:
            self.cache.popitem(False)
        self.cache[page]=page
        self.printc()


    def printc(self):
        print("printing  cache : ",end='')
        print(self.cache)
            
    
        
        
LRU_cache = lru_cache(6)

LRU_cache.accesspage(3)
LRU_cache.accesspage(4)
LRU_cache.accesspage(4)
LRU_cache.accesspage(3)
LRU_cache.accesspage(6)
LRU_cache.accesspage(3)
LRU_cache.accesspage(5)
LRU_cache.accesspage(7)
LRU_cache.accesspage(8)
LRU_cache.accesspage(1)
LRU_cache.accesspage(5)

        
        
        
        
        
        
        
        
        
        
        
        
        
    