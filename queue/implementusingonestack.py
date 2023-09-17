class UsingOneStack:
    def __init__(self):
        self.stack = []
        
    def enqueue(self,data):
        self.stack.append(data)
        
    def stack_data(self):
        return self.stack
        
    def dequeue(self):
        if len(self.stack)==0:
            return None
        elif len(self.stack)==1:
            return self.stack.pop()
        else:
            pop_data=self.stack.pop()
            dequeue_data = self.dequeue()
            self.stack.append(pop_data)
            return dequeue_data
        
    def size(self):
        return 0 if len(self.stack)==0 else len(self.stack)
    
    def is_empty(self):
        return False if self.stack else True
    
            
        
    
    
    


UsingOneStack=UsingOneStack()
UsingOneStack.enqueue(11)
UsingOneStack.enqueue(12)
UsingOneStack.enqueue(13)
UsingOneStack.enqueue(18)
print(UsingOneStack.stack_data())
print(UsingOneStack.dequeue())

print(UsingOneStack.stack_data())