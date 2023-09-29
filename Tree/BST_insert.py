class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.level=None
        

class BstInsert:
    
    def insert(self, root,val):
        #Enter you code here.
        self.root = self.insert_bst(self.root,val)
        return self.root
    
    def insert_bst(self,root,value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.insert_bst(root.left,value)
        else:
            root.right = self.insert_bst(root.right,value)
        return root
            
    