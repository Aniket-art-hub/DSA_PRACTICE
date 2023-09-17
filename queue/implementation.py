class QueueImplementation:
    def __init__(self):
        self.queue_data =[]
        self.front = 0
        self.rear = -1
        self.queuesize = 0
    def simple_enqueue_by_array(self,data):
        self.rear +=1
        self.queue_data.append(data)
        self.queuesize+=1
        
    def simple_dequeue_in_array(self):
        if self.is_empty:
            self.queuesize-=1
            self.rear-=1
            return self.queue_data.pop(0)
        else:
            return "empty array"
    
    def get_rear_data(self):
        if self.is_empty:
            return self.queue_data[self.rear]
        else:
            return "empty array"
        
    def get_front_data(self):
        if self.queue_data:
            return self.queue_data.pop(0)
        else:
            return "empty array"
        
    def is_empty(self):
        return len(self.queue_data)==0
        
    def get_size(self):
        return self.queuesize-1
    
    def  get_all_element(self):
        return self.queue_data
        
    

QueueImplementation = QueueImplementation()
QueueImplementation.simple_enqueue_by_array(12)
QueueImplementation.simple_enqueue_by_array(22)
QueueImplementation.simple_enqueue_by_array(13)
QueueImplementation.simple_enqueue_by_array(15)
QueueImplementation.simple_enqueue_by_array(11)
QueueImplementation.simple_enqueue_by_array(10)
print(QueueImplementation.simple_dequeue_in_array())
print(QueueImplementation.get_rear_data())
print(QueueImplementation.get_front_data())
print(QueueImplementation.get_size())
print(QueueImplementation.is_empty())
print(QueueImplementation.get_all_element())
