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
            
            
    def vertical_traversal_tree(self,root):
        if root==None:
            return root
        dict={}
        result=[]
        self.getTraversalTree(root,0,0,dict)
        for key,data in enumerate(sorted(dict)):
            result.append(sorted(dict[data]))
        return result
            
        
        
    def getTraversalTree(self,root,traversalindex,level,dict):
        if root==None:
            return root
        if (traversalindex in dict) and (level in dict[traversalindex]):
            dict[traversalindex][level].append(root.val)
        else:
            dict[traversalindex] = {}
            dict[traversalindex][level] = [root.val]
        self.getTraversalTree(root.left,traversalindex-1,level+1,dict)
        self.getTraversalTree(root.right,traversalindex+1,level+1,dict)
        
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
        
        
        
            
        
        
            
        
            