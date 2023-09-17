from queue import Queue
class Node:
    def __init__(self,val=0):
        self.left = None
        self.right = None
        self.val = val
        
class BinarySerachTree:
    def __init__(self,root):
        self.root = Node(root)
        
    def level_order_traverse(self,root,list):
        if root == None:
            return root
        bst_queue = Queue()
        bst_queue.put(root)
        while bst_queue.qsize()>0:
            curr = bst_queue.get()
            if curr.left:
                bst_queue.put(curr.left)
            if curr.right:
                bst_queue.put(curr.right)
            list.append(curr.val)
        return list
    
    
    def bst_insertion(self,root,key):
        new_node = Node(key)
        if root == None:
            return root
        insert_queue = Queue()
        insert_queue.put(root)
        while insert_queue.qsize()>0:
            curr = insert_queue.get()
            if curr.val > key:
                if curr.left != None:
                    insert_queue.put(curr.left)
                else:
                    curr.left = new_node
                    break
            else:
                if curr.right != None:
                    insert_queue.put(curr.right)
                else:
                    curr.right = new_node
                    break
        return root
    
    def delete_from_bst(self,root,key):
        if root == None:
            return root
        if key<root.val:
            left_tree = self.delete_from_bst(root.left,key)
        elif key>root.val:
            right_tree = self.delete_from_bst(root.right,key)
        else:
            # case 1 ---> when no child
            if root.left == None and root.right==None:
                return None
            # case 2 ---> when 1 child
            elif root.left==None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                successor,successorParent = root.right, root
                while successor.left != None:
                    successorParent = successor
                    successor = successor.left
                if successorParent != root:
                    successorParent.left = successor.right
                else:
                    successorParent.right = successor.right
                root.val = successor.val
                return root
        return root
            
                
            
            
        
    
    
BSTTree = BinarySerachTree(7)
BSTTree.root.left = Node(2)
BSTTree.root.right = Node(8)
BSTTree.root.left.left = Node(4)
BSTTree.root.left.right = Node(6)
BSTTree.root.left.left.left = Node(5)
BSTTree.root.right.left = Node(13)
BSTTree.bst_insertion(BSTTree.root,3)
BSTTree.delete_from_bst(BSTTree.root,4)
print(BSTTree.level_order_traverse(BSTTree.root,[]))