class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class QueueLLImplementation:
    def __init__(self):
        self.head=None
        
    def enque(self,data):
        new_node=Node(data)
        if not self.head:
            new_node.next=None
            self.head=new_node
        else:
            curr = self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new_node
            new_node.next=None
    
   
    
    def dequeue(self):
        curr=self.head
        self.head=curr.next
        curr.next=None
        return "dequeue data is " + str(curr.data)
    
    def iterate(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next
            
    def front(self):
        return "front data is " + str(self.head.data) if self.head else None
    
    def rear(self):
        if self.head:
            curr = self.head
            while curr.next!=None:
                curr = curr.next
            return "rear data is "+str(curr.data)
        else:
            return None
        
    def is_empty(self):
        return self.head==None
    
    def size(self):
        count=0
        if self.head:
            curr=self.head
            while curr != None:
                count+=1
                curr=curr.next
        return count
        
    
    
QueueLLImplementation = QueueLLImplementation()
print(QueueLLImplementation.enque(10))    
print(QueueLLImplementation.enque(12))    
print(QueueLLImplementation.enque(13))    
print(QueueLLImplementation.enque(13))    
print(QueueLLImplementation.enque(13))    
print(QueueLLImplementation.enque(15))    
print(QueueLLImplementation.dequeue())    
print(QueueLLImplementation.iterate())  
print(QueueLLImplementation.dequeue())      
print(QueueLLImplementation.front())    
print(QueueLLImplementation.rear())    
print(QueueLLImplementation.is_empty())    
print(QueueLLImplementation.size())    
        
    
