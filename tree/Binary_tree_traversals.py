"""
Binary tree
"""

class newnode():
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
def inorder(node):
    if  node is None:
        return
    inorder(node.left)
    print("{} ".format(node.data),end='',flush= True)
    inorder(node.right)
    print("")
    
def preorder(node):
    if node is None:
        return
    print("{} ".format(node.data,end='',flush= True))
    preorder(node.left)
    preorder(node.right)
    print("")

root = newnode(2)
root.left = newnode(4)
root.right = newnode(3)
root.left.right = newnode(6)
root.left.left= newnode(5)
inorder(root)
preorder(root)
    
