# -*- coding: utf-8 -*-
"""
Binary search tree basic operations  
"""

class newnode():
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(root):
    if root:
        inorder(root.left)
        print("{0} ".format(root.data),end='',flush = False)
        inorder(root.right)
        
def insertbst(node,data):
    if node is None:
        print("root is none")
        return  newnode(data)
    if node.data == data:
        print("The {} alrady exists in the binary tree".format(str(data)))
        
    if node.data < data:
        node.right = insertbst(node.right, data)  
    if node.data > data:
        node.left = insertbst(node.left, data)
    return node
        
root = newnode(20)
root.left = newnode(16)
root.right = newnode(30)
root.left.left = newnode(13)
root.left.right = newnode(17)

root = insertbst(root,17)


inorder(root)




