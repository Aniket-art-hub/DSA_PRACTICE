class UsingStack: 
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def enque_using_two_stack(self,data):
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(data)
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        else:
            self.stack1.append(data)
        print(self.stack1)
        
        
    def dequeue_data(self):
        if len(self.stack1)==0:
            return -1
        else:
            x = self.stack1.pop()
            return x
        
    def queue_size(self):
        return 0 if len(self.stack1)==0 else len(self.stack1)
    
    def is_empty(self):
        return False if self.stack1 else True
        
        
    
    
    
    
UsingStack = UsingStack()
UsingStack.enque_using_two_stack(10) 
UsingStack.enque_using_two_stack(11) 
UsingStack.enque_using_two_stack(12) 
UsingStack.enque_using_two_stack(13)
print(UsingStack.dequeue_data()) 
UsingStack.enque_using_two_stack(14) 
UsingStack.enque_using_two_stack(15) 
UsingStack.enque_using_two_stack(16) 
print(UsingStack.dequeue_data()) 
UsingStack.enque_using_two_stack(17) 
UsingStack.enque_using_two_stack(18) 
print(UsingStack.queue_size())
print(UsingStack.is_empty())

        