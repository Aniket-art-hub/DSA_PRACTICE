class CircularQueue:
    def __init__(self):
        self.capacity=10
        self.front=0
        self.rear=-1
        self.queuesize=0
        self.queue_array=[None]*self.capacity

    def enqueue(self,data):
        if self.queuesize==self.capacity:
            return "queue is full"
        else:
            self.rear=(self.rear+1)%self.capacity
            self.queue_array[self.rear]=data
            self.queuesize+=1
    
    def dequeue(self):
        if self.queuesize is None:
            return "Queue is empty"
        else:
            x=self.queue_array[self.front]
            self.front = (self.front+1)%self.capacity
            self.queuesize-=1
            return "dequeue value is " + str(x)
    
    def get_front(self):
        if self.queue_array is None:
            return "empty queue"
        else:
            return "front data is " + str(self.queue_array[self.front])
        
    def get_rear(self):
        if self.queue_array is None:
            return "empty queue"
        else:
            return "rear data is " + str(self.queue_array[self.rear])
    
    def traverse(self):
        array_data=[]
        if self.queue_array:
            for i in self.queue_array:
                array_data.append(i)
        return array_data
    
    def get_size(self):
        return self.queuesize
    def is_empty(self):
        return self.queue_array==None
        
        
CircularQueue=CircularQueue()
CircularQueue.enqueue(12)
CircularQueue.enqueue(11)
print(CircularQueue.dequeue())
CircularQueue.enqueue(1)
CircularQueue.enqueue(10)
CircularQueue.enqueue(15)
print(CircularQueue.dequeue())

print(CircularQueue.traverse())
print(CircularQueue.get_front())
print(CircularQueue.get_rear())
print(CircularQueue.get_size())
print(CircularQueue.is_empty())
        
            
        