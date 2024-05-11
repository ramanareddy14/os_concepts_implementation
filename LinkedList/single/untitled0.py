# -*- coding: utf-8 -*-
"""
Singly Linked list basics
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    
    #initializing the linked list
    def __init__(self):
        self.head = None
        
    def print(self):
        print("\nprinting linked list")
        if self.head is None:
            return
        temp = self.head
        while temp != None:
            print(temp.data,' ', end = '',flush = True)
            temp = temp.next
        
    def append(self, data):
        # Create a new node
        newnode = Node(data)
        
        #if LL is empty add as head
        if self.head is None:
            self.head = newnode
        
        #else get the last node
        last = self.head
        while (last.next):
            last = last.next
            
        # now we get a node whose .next is None append here
        last.next = newnode
        
    def delete_duplicates(self):
        temp = self.head
        while temp:
            prev = temp.data
            while temp.next != None and temp.next.data == prev:
                temp.next = temp.next.next
            temp = temp.next    
            

        
        
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)

    for i in [2,2,3,3,4,4,4,5,6]:
        llist.append(i)

    llist.print()
    llist.delete_duplicates()
    llist.print()
    

