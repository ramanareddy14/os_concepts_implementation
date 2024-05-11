# -*- coding: utf-8 -*-
"""
Binary search tree basic operations  
"""

# Generic tree node
class newnode():
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
#AVL tree to support avl balancing BST insertion
class avl_balancing(object):
    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree
    def insert(self, root, data):
        # Step 1 perform normal BST
        if root is None:
            return newnode(data)
        if root.data == data:
            print("The data:{} alrady exists in the tree".format(data))
        if root.data > data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
            
        # Step 2 Update height of current node(ancestor of inserted node)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # Step 3 get the balance factor of current node
        balance = self.getbalance(root)
        
        # Step 4 if left height is more than 1 left/left-right case
        if balance > 1:
            #case 1 left rotate
            if data < root.left.data:
                return self.rightrotate(root)
            
            # case 3 left-right rotation
            if data > root.right.data:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)
            
        if balance < -1:
            # case 2 right rotate
            if data > root.right.data:
                return self.leftrotate(root)
            
            # case 4 right left rotate
            if data < root.right.data:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)
            
        return root
            
        # implementing rotations
    def leftrotate(self, z):
            y = z.right
            T2 = y.left
     
            # Perform rotation
            y.left = z
            z.right = T2
     
            # Update heights
            z.height = 1 + max(self.getHeight(z.left),
                             self.getHeight(z.right))
            y.height = 1 + max(self.getHeight(y.left),
                             self.getHeight(y.right))
     
            # Return the new root
            return y
        
    def rightrotate(self,z):
            y = z.left
            T = y.right
            
            #perform rotation
            y.right = z
            z.left = T
            
            # Update heights
            z.height = 1 + max(self.getHeight(z.left),
                             self.getHeight(z.right))
            y.height = 1 + max(self.getHeight(y.left),
                             self.getHeight(y.right))
            return y
        
    def preorder(self,root):
            if root:
                print(" {} ".format(root.data),end='',flush=True)
                self.preorder(root.left)
                self.preorder(root.right)
                 
        
        #defining utilities 
    def getHeight(self,root):
            if root is None:
                return 0
            return root.height
        

    
    def getbalance(self, root):
            rightheight = self.getHeight(root.right)
            leftheight  = self.getHeight(root.left)
            print(root.data," left: {}, right: {}".format(rightheight,leftheight))
            return leftheight - rightheight
        
# Create None tree and insert using AVL class operations


# Driver program to test above function
myTree = avl_balancing()
root = None
 
root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)
 
"""The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""
 
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.preorder(root)
print()

