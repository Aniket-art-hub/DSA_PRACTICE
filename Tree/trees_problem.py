from Tree.basic_operation import Node
class TreesProblem:
    def check_identical(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
        x =  self.isIdentical(root1.left, root2.left) 
        y = self.isIdentical(root1.right, root2.right)
        return x and y
    
    def max_depth(self,root):  ######## brute_force level_order traversal and keep count
        if root == None:
            return 0
        from queue import Queue
        max_depth_queue = Queue()
        max_depth_queue.put(root)
        count = 0
        while max_depth_queue.qsize()>0:
            size = max_depth_queue.qsize()
            while size>0:
                curr = max_depth_queue.get()
                if curr.left:
                    max_depth_queue.put(curr.left)
                if curr.right:
                    max_depth_queue.put(curr.right)
                size-=1
            count+=1
        return count
    
    def max_depth_recursive(self,root): ############## bY RECURSIVE USE
        if root == None:
            return 0
        leftheight = self.maxDepth(root.left)
        rightheight = self.maxDepth(root.right)
        return max(leftheight,rightheight)+1
    
    
    def zigzag_traverse(self,root):
        s1=[]
        s2=[]
        array_list=[]
        if root==None:
            return array_list
        s1.append(root)
        while len(s1)>0 or len(s2)>0:
            temp_list=[]
            while len(s1)>0:
                curr=s1.pop()
                if curr.left:
                    s2.append(curr.left)
                if curr.right:
                    s2.append(curr.right)
                temp_list.append(curr.val)
            if temp_list:
                array_list.append(temp_list)
            temp_list=[]
            while len(s2)>0:
                curr=s2.pop()
                if curr.right:
                    s1.append(curr.right)
                if curr.left:
                    s1.append(curr.left)
                temp_list.append(curr.val)
            if temp_list:
                array_list.append(temp_list)
        return array_list
    
    #################  zigzag variation ############################
    def zigzag_variation_after_two(self,root):
        s1=[]
        s2=[]
        array_list=[]
        if root==None:
            return array_list
        s1.append(root)
        level=0
        while len(s1)>0 or len(s2)>0:
            level+=1
            temp_list=[]
            while len(s1)>0:
                curr=s1.pop()
                if curr.left:
                    s2.append(curr.left)
                if curr.right:
                    s2.append(curr.right)
                temp_list.append(curr.val)
            if level==2:
                temp_list.reverse()
                level=0
            if temp_list:
                array_list.append(temp_list)
            temp_list=[]
            while len(s2)>0:
                curr=s2.pop()
                if curr.right:
                    s1.append(curr.right)
                if curr.left:
                    s1.append(curr.left)
                temp_list.append(curr.val)
            if temp_list:
                array_list.append(temp_list)
        return array_list
              
    def isBalanced(self, root):
        height = self.treeheight(root)
        if height==-1:
            return False
        return True

    def treeheight(self,root):
        if root == None:
            return 0
        left = self.treeheight(root.left)
        right = self.treeheight(root.right)
        if (left==-1 or right==-1 or abs(left-right)>1):
            return -1
        return max(left,right)+1
    
    def find_key(self,root,key):
        from queue import Queue
        q=Queue()
        if root==None:
            return 0
        q.put(root)
        level=1
        while q.qsize()>0:
            queue_size=q.qsize()
            while queue_size>0:
                curr=q.get()
                if curr.data == key:
                    return level
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                queue_size-=1
            level+=1
        return 0
    
    def invert_tree(self,root):
        if root==None:
            return root
        self.swap(root)
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
        
    def swap(self,root):
        temp=root.right
        root.right=root.left
        root.left=temp
            
    def k_distance_node(self,root,k):
        if root==None:
            return root
        from queue import Queue
        q=Queue()
        result=[]
        q.put(root)
        level=1
        while q.qsize()>0:
            queue_size=q.qsize()
            if level == k:
                while queue_size>0:
                    curr = q.get()
                    result.append(curr.data)
                    queue_size-=1
                return result
            while queue_size>0:
                curr=q.get()
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                queue_size-=1
            level+=1
        return 0
    
    def k_diff_node_recursive(self,root,k):
        if root==None:
            return root
        if k==0:
            return root.data
        else:
            self.k_diff_node_recursive(root.left,k-1)
            self.k_diff_node_recursive(root.right,k-1)
            
    ########################## vertical traverse ####################################      
    def vertical_traversal_tree(self,root):
        if root==None:
            return root
        from collections import defaultdict
        dict=defaultdict(list)
        self.getTraversalTree(root,0,0,dict)
        result=[]
        for data in sorted(dict.keys()):
            data_list=dict[data]
            #to sort on the basis of level
            sorted_data = sorted(data_list,key=lambda x:(x[1],x[0]))
            temp=[]
            for i in sorted_data:
                temp.append(i[0])
            result.append(temp)
        return result
            
        
        
    def getTraversalTree(self,root,traversalindex,level,dict):
        if root==None:
            return root
        dict[traversalindex].append(root.val,level)
        self.getTraversalTree(root.left,traversalindex-1,level+1,dict)
        self.getTraversalTree(root.right,traversalindex+1,level+1,dict)
    
    
    
    ###################### max sum path ###############################
    import sys
    max_sum=-sys.maxsize-1
    def max_sum_path(self,root):
        if root == None:
            return 0
        left_node = self.max_sum_path(root.left)        
        right_node = self.max_sum_path(root.right)  
        
        maximum_sum = max(root.data,max(left_node,right_node)+root.data)   
        TreesProblem.max_sum = max(TreesProblem.max_sum,max(maximum_sum,left_node+right_node+root.data))
        return maximum_sum
    
    def get_max_sum_path(self,root):
        self.max_sum_path(root)
        return TreesProblem.max_sum  
    
    
    ########################## path to a given node ###############################
    def pathgiven_node(self, root, key):
        result=[]
        self.path_given_node(root,key,result)
        return result
    def path_given_node(self,root,key,result):
        if root==None:
            return False
        if root.val==key:
            result.append(root.val)
            return True
        result.append(root.val)
        if self.path_given_node(root.left,key,result) or self.path_given_node(root.right,key,result):
            return True
        result.pop()
        
        
    ############### lowest common ancesstor###########################
    def lowest_common_ancesstor(self,root,a,b):
        if root == None:
            return None
        if left==a or right==b:
            return root 
        left = self.lowest_common_ancesstor(root.left,a,b)
        right = self.lowest_common_ancesstor(root.right,a,b)
        
        if left != None and right != None:
            return root
        if left != None:
            return right
        else:
            return left
        
    ##################### flatten a binary tree in linkedlist ###########################
    
    def flatten_binaryTree(self,root):
        if root==None:
            return root
        while root !=None:
            if root.left!=None:
                curr=root
                tempTree = curr.right
                curr.right = curr.left
                curr.left=None
                while curr.right!=None:
                    curr=curr.right
                curr.right = tempTree
            root = root.right
        return curr.right
    
    ######################## is cousins or not ###################################
    def is_cousins(self,root,a,b):
        if root==None:
            return False
        levela = self.get_level(root,a)
        levelb = self.get_level(root,b)
        if levela==0 or levelb==0:
            return False
        return (levela==levelb) and (not self.issibling(root,a,b))
       
    def issibling(self,root,a,b):
        if root==None:
            return False
        if (root.left != None and root.right != None) and ((root.left.data==a and root.right.data==b) or (root.right.data==a and root.left.data==b)):
            return True
        return (self.issibling(root.left,a,b) or self.issibling(root.right,a,b)) 
    def get_level(self,root,key):
        if root==None:
            return root
        from queue import Queue
        q=Queue()
        q.put(root)
        level = 1
        while q.qsize()>0:
            qsize = q.qsize()
            while qsize>0:
                curr=q.get()
                if curr.data == key:
                    return level
                if curr.left:
                    q.put(curr.right)
                if curr.right:
                    q.put(curr.right)
            level +=1

        return 0
    
    
    ########################### construct binary tree by reorder and inorder ########################
    
    def buildTree(self, preorder, inorder):
        self.index=0
        return self.constructBinaryTree(preorder,inorder,0,len(inorder)-1)


    def constructBinaryTree(self,preorder,inorder,start,end):
        if start>end:
            return None

        newTreeNode = Node(preorder[self.index])
        self.index+=1
        if start==end:
            return newTreeNode
        get_index = self.search(inorder,start,end,newTreeNode.val)
        newTreeNode.left = self.constructBinaryTree(preorder,inorder,start,get_index-1)
        newTreeNode.right = self.constructBinaryTree(preorder,inorder,get_index+1,end)
        return newTreeNode
    

    def search(self,inorder,start,end,key):
        for i in range(start,end+1):
            if inorder[i]==key:
                return i
        return -1
    
    
    ################## Diameter of binary tree ######################
    def diameter_binaryTree(self,root):
        self.diameter=0
        if root==None:
            return 0
        self.get_diameter(root)
        return self.diameter
    
    def get_diameter(self,root):
        if root==None:
            return 0
        left_height = self.get_diameter(root.left)
        right_height = self.get_diameter(root.right)
        self.diameter = max(self.diameter,left_height+right_height)
        return max(left_height,right_height)+1

        
    #################### varitaion of vertical traverse Top view ####################
    def top_view(self,root):
        if root==None:
            return None
        from collections import defaultdict
        dict=defaultdict(list)
        self.get_top_view(root,0,0,dict)
        result = []
        for data in sorted(dict.keys()):
            result.append(dict[data][0])
        return result
            
            
            
        
    def get_top_view(self,root,index,level,dict):
        if root==None:
            return 0
        if index not in dict:
            dict[index] = [root.data,level]
        elif dict[index][1]>level:
            dict[index] = [root.data,level]
        self.get_top_view(root.left,index-1,level+1,dict)
        self.get_top_view(root.right,index+1,level+1,dict)
        
    ################## by levelorder traverse get top view ##########################
    def level_order_top_view(self,root):
        if root == None:
            return root
        list=[]
        dict={}
        hd=0
        root.hd=0
        list.append(root)

        while len(list)>0:
            data=list[0]
            hd=data.hd
            if hd not in dict:
                dict[hd]=root.data
                
            if data.left:
                data.left.hd=hd-1
                list.append(data.data)
            if data.right:
                data.right.hd=hd+1
                list.append(data.right)
            list.pop(0)
        result=[]
        for i in sorted(dict):
            result.append(dict[i])
        return result
    
    ######################### left view of binary tree ##########################
    def left_view(self,root):
        if root==None:
            return None
        dict={}
        self.get_left_view(root,0,dict)
        result=[]
        for level,data in dict.items():
            result.append(dict[level])
        return result
            
    def get_left_view(self,root,level,dict):
        if root==None:
            return 0
        if level not in dict:
            dict[level] = root.data
        self.get_left_view(root.left,level+1,dict)
        self.get_left_view(root.right,level+1,dict)
    
    
    ####################### right view of binary tree #####################################
    def right_view(self,root):
        if root==None:
            return None
        dict={}
        self.get_right_view(root,0,dict)
        result=[]
        for level,data in dict.items():
            result.append(dict[level])
        return result
            
    def get_right_view(self,root,level,dict):
        if root==None:
            return 0
        if level not in dict:
            dict[level] = root.data
        self.get_right_view(root.right,level+1,dict)
        self.get_right_view(root.left,level+1,dict)
        
        
    ################ bottom view of binary tree ############################################
    def bottom_view(self,root):
        if root==None:
            return None
        dict={}
        self.get_bottom_view(root,0,dict)
        result=[]
        if dict:
            for data in sorted(dict.keys()):
                result.append(dict[data])
        return result
            
        
    def get_bottom_view(self,root,index,dict):
        if root==None:
            return None
        dict[index] = [root.data]
        self.get_bottom_view(root.left,index-1,dict)
        self.get_bottom_view(root.right,index+1,dict)
        
    # ------------------------------------------> level order get botton view
#     def bottom_view(self,root):
#         if root==None:
#             return root
#         from queue import Queue
#         q=Queue()
#         q.put(Pair(root,0))
#         dict={}
#         while q.qsize()>0:
#             curr=q.get()
#             hd = curr.hd      
#             if hd not in dict:
#                 dict[hd] = curr.data   #(getting some issue to get data)
#             if curr.left:
#                 q.put(Pair(root.left,curr.hd-1))
#             if curr.right:
#                 q.put(Pair(root.right,curr.hd+1))
#         return dict
# class Pair:
#     def __init__(self,root,hd) -> None:
#         self.root=root
        # self.hd = hd
        
        from queue import Queue
        max_depth_queue = Queue()
        max_depth_queue.put(root)
        count = 0
        while max_depth_queue.qsize()>0:
            size = max_depth_queue.qsize()
            while size>0:
                curr = max_depth_queue.get()
                if curr.left:
                    max_depth_queue.put(curr.left)
                if curr.right:
                    max_depth_queue.put(curr.right)
                size-=1
            count+=1
        return count
            