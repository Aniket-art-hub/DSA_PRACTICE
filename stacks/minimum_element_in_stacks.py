class MinElementStack:  ############ approach  1 complexity is O(1) and space is O(n)
    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]
        
    def push(self,x):
        self.main_stack.append[x]
        if not self.min_stack or x<self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        if self.main_stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.main_stack.pop()
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else -1
    
    
#####################  APPROACH 2 USING ONE STACK COMPLEXITY IS O(1) ################
class Solution:
    def __init__(self):
        self.s=[]
        self.minEle=None
    def push(self,x):
        #CODE HERE
        if not self.s:
            self.s.append(x)
            self.minEle = x
        else:
            if x <= self.minEle:
                push_data = 2*x-self.minEle
                self.s.append(push_data)
                self.minEle=x
            else:
                self.s.append(x)

    def pop(self):
        #CODE HERE
        val = -1
        if self.s:
            val  = self.s[-1]
            if (val<self.minEle):
                val = self.minEle
                self.minEle = 2*self.minEle-self.s[-1]
            self.s.pop()
        if not self.s:
            self.minEle = None
        return val
        

    def getMin(self):
        #CODE HERE
        return self.minEle        
        
        
        
MinElementStack_obj = MinElementStack()
arr=[4,2,1,12,3,6]
x =8
print(MinElementStack_obj.push(x))
x =2
print(MinElementStack_obj.push(x))
x=9
print(MinElementStack_obj.push(x))
x=6
print(MinElementStack_obj.push(x))
print(MinElementStack_obj.pop())
print(MinElementStack_obj.get_min())