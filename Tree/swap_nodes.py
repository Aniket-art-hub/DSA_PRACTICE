from queue import Queue
class Node:
    def __init__(self,val):
        self.info=val
        self.left=None
        self.right=None


def swapNodes(indexes, queries):
    # Write your code here
    def createTree(root,indexes):
        q=Queue()
        q.put(root)
        for left,right in indexes:
            temp = q.get()
            if left != -1:
                temp.left = Node(left)
                q.put(temp.left)
            if right != -1:
                temp.right = Node(right)
                q.put(temp.right)
        return root
    def swap(root,k,level,array):
        if root:
            if level%k==0:
                root.left,root.right = root.right,root.left
            swap(root.left,k,level+1,array)
            array.append(root.info)
            swap(root.right,k,level+1,array)
    root=Node(1) 
    root = createTree(root,indexes)
    result=[]
    for k in queries:
        l=[]
        swap(root,k,1,l)
        result.append(l)
    return result