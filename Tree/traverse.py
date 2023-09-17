class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

class TreeTraverse:
    def __init__(self,root):
        self.root = Node(root)
        
################################  DFS TRAVERSAL #####################################
    def in_order(self,root,list):
        if root==None:
            return 
        self.in_order(root.left,list)
        list.append(root.data)
        self.in_order(root.right,list)
        return list
        
    def pre_order(self,root,list):
        if root==None:
            return 
        list.append(root.data)
        self.pre_order(root.left,list)
        self.pre_order(root.right,list)
        return list
    
    def post_order(self,root,list):
        if root==None:
            return
        self.post_order(root.left,list)
        self.post_order(root.right,list)
        list.append(root.data)
        return list
    
    
    
    ############################ BFS LEVEL ORDER TRAVERSAL ##################################
    def level_order_traversal(self,root,list):
        from queue import Queue
        my_queue = Queue()
        my_queue.put(root)
        while my_queue.qsize()>0:
            data = my_queue.get()
            if data.left:
                my_queue.put(data.left)
            if data.right:
                my_queue.put(data.right)
            list.append(data.data)
        return list
    
tree = TreeTraverse(1)
tree.root.right = Node(3)
tree.root.left = Node(4)
tree.root.left.left = Node(9)
tree.root.left.right = Node(19)
tree.root.left.left.left = Node(14)
tree.root.left.right.right = Node(13)
print(tree.pre_order(tree.root,[]))
print(tree.in_order(tree.root,[]))
print(tree.post_order(tree.root,[]))
print(tree.level_order_traversal(tree.root,[]))