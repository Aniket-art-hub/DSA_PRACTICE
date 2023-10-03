# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
# '''

class Solution:
    def inorder_traversal(self,root,array_list): # LDR (LEFT->DATA->RIGHT)
        if root==None:
            return None
        self.inorder_traversal(root.left,array_list)
        array_list.append(root.data)
        self.inorder_traversal(root.right,array_list)
        
    
    def postOrder_traversal(self,root,array_list): # LRD (LEFT->RIGHT->RIGHT)
        if root==None:
            return None
        self.postOrder_traversal(root.left,array_list)
        self.postOrder_traversal(root.right,array_list)
        root.data = array_list[self.index]
        array_list.append(root.data)
        self.index+=1
        
    def convertToMaxHeapUtil(self, root):
        array_list = []
        self.inorder_traversal(root,array_list)
        self.index = 0
        self.postOrder_traversal(root,array_list)
        return array_list