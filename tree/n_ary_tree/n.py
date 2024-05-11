# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:27:15 2022

@author: raman
"""

from queue import deque

class Node:
    def __init__(self, data, children = None):
        self.value  = data
        self.children = []
        if children != None:
            self.children = children

                
# print preorder traversal of N ary tree recurseively
def printtree(root):
    if root == None:
        return
    
    print(root.value,' ',end = '')
    for each in root.children:
        printtree(each)
        
# print preorder traversal iteratively
def printtree_itr(root):
    stack = [root]
    visited = set()
    while len(stack)>0:
        current = stack.pop()
        if current != None:
            if current in visited:
                print(current.value,' ',end='')
            else:
                
                for each in current.children[::-1]:
                    stack.append(each)
                visited.add(current)
                stack.append(current)
                    
#https://www.tutorialspoint.com/program-to-make-a-copy-of-a-n-ary-tree-in-python

node6 = Node(65)
node5 = Node(56)
node4 = Node(42, [node5, node6])
node3 = Node(32)
node2 = Node(27)
node1 = Node(14, [node2, node3, node4])
root = node1

#copynode = solve(root)
printtree_itr(root)
    
        
    