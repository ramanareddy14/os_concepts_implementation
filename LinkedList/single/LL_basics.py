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
        
    # newnode = self.head, self.head = newnode
    def addfront(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    
    #node and node.next is not null
    #node.next = search then newnode.next = node.next, node.next = newnode
    def addafter(self,search,add):
        if self.head is None or search is None:
            return
        #1. Create a node
        newnode = Node(add)
        
        # 2. if head is search
        if self.head.data is search:
            newnode.next = self.head.next
            self.head.next = newnode
            
        # 3. Searching for search
        temp = self.head
        while temp.next != None and temp.next.data != search :
            temp = temp.next
        
        
        # now either search is found or not found
        if temp.next != None and temp.next.data is search:
            newnode = Node(add)
            newnode.next = temp.next.next
            temp.next.next = newnode
        
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
        
            
    def delete(self, data):
        if self.head is None:
            print("LList is null and cannot delete element from it")
            return
        
        #1. if data is at head
        # temp = self.head
        #self.head = self.head.next
        todelete = None
        if self.head.data == data:
            todelete = self.head
            self.head = self.head.next
            
            
        #2 if data is in middle unlink it
        temp = self.head
        while temp.next != None and temp.next.data != data:
            temp = temp.next
        
        # we either reached end or the data to delete
        if temp.next != None:
            todelete = temp.next
            temp.next = temp.next.next
        
        #3 data is at the end 
        # this is already handled in number 2
        
        # how to clean todelete
        
    def deleteat_pos(self, pos):
        print("To implement delete at a position in a Linked List")
        
        
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second;
    second.next = third;
    
    llist.append(5)
    llist.addafter(1, 6)
    llist.print()
        
    llist.delete(5)
    llist.print()

