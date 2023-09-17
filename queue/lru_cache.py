
class Node:     
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache(object):

    def __init__(self,capacity):
        self.hash = {}
        self.capacity=capacity
        self.head=None
        self.tail=None

    def get(self,key):
        if key in self.hash:
            new_node=self.hash[key]
            self.movetohead(new_node)
            return new_node.val
        return -1
        
    def put(self,key,val):
        if key in self.hash:
            new_node=self.hash[key]
            self.movetohead(new_node)
            new_node.val=val
        else:
            if len(self.hash)>=self.capacity:
                self.removetail()
            new_node = Node(key,val)
            self.addHead(new_node)
            self.hash[key]=new_node
            
    def movetohead(self,temp):
        if temp == self.head:
            return
        elif(temp==self.tail):
            self.tail=self.tail.prev
            self.tail.next=None
            self.addHead(temp) 
        else:
            temp.prev.next=temp.next
            temp.next.prev = temp.prev
            self.addHead(temp) 
                      
    def addHead(self,temp):
        if self.head==None:
            self.head=self.tail=temp
        else:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
            
    def removetail(self):
        if self.tail and self.tail.prev:
            self.tail.next = None
        else:
            self.head=None
        if self.tail:
            self.hash.pop(self.tail.key)
            self.tail = self.tail.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)