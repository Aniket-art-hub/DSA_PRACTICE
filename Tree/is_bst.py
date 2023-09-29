class IsBst:
    def check_binary_search_tree_(self, root):
        if root==None:
            return True
        return self.check_bst(root,float('-inf'),float('inf'))
    
    def check_bst(self,root,min_val,max_val):
        if root==None:
            return True
        if root.data<=min_val or root.data>=max_val:
            return False
        return self.check_bst(root.left,min_val,root.data) and self.check_bst(root.right,root.data,max_val)
    
        
