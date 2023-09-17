from queue import Queue
class Node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val
    
class Insertion:
    def __init__(self,root):
        self.root = Node(root)
        
        
    def insert_binarytree(self,root,key):
        new_node = Node(key)
        if root == None:
            return new_node
        insert_queue = Queue()
        insert_queue.put(root)
        while insert_queue.qsize()>0:
            curr = insert_queue.get()
            
            if curr.left != None:
                insert_queue.put(curr.left)
            else:
                curr.left = new_node
                break
            
            if curr.right!=None:
                insert_queue.put(curr.right)
            else:
                curr.right = new_node
                break
        return root
    
    def deletion_binary_tree(self,root,key):
        if root == None:
            return root
        delete_queue = Queue()
        delete_queue.put(root)
        keyNode = None
        curr = None
        while delete_queue.qsize()>0:
            curr = delete_queue.get()
            if curr.val == key:
                keyNode = curr
            if curr.left:
                delete_queue.put(curr.left)
            if curr.right:
                delete_queue.put(curr.right)
        if keyNode is None:
            return "key not present"
        else:
            keyNode.val = curr.val
        return self.delete_leaf(root,curr.data)
    
    def delete_leaf(self,root,data):
        delete_leaf = Queue()
        delete_leaf.put(root)
        while delete_leaf.qsize()>0:
            curr = delete_leaf.get()
            if curr == data:
                curr = None
                return root
            if curr.left != None:
                if curr.left==data:
                    curr.left = None
                    return root
                delete_leaf.put(curr.left) 
            
            if curr.right != None:
                if curr.right==data:
                    curr.right = None
                    return root
                delete_leaf.put(curr.right) 
        return root   
        

    def level_order_traversal(self,root,list):
        if root == None:
            return 0
        from queue import Queue
        tree_queue = Queue()
        tree_queue.put(root)
        while tree_queue.qsize()>0:
            data = tree_queue.get()
            if data.left:
                tree_queue.put(data.left)
            if data.right:
                tree_queue.put(data.right)
            list.append(data.val)
        return list
    
    
    
    
tree=Insertion(10)
tree.root.left = Node(11)
tree.root.right = Node(9)
tree.root.left.left = Node(7)
tree.root.right.left = Node(15)
tree.root.right.right = Node(8)
print(tree.insert_binarytree(tree.root,12))
print(tree.level_order_traversal(tree.root,[]))


    