class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        

def create_singly_ll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head

        
class linkelist:
    def delimiter(cls,head):
        if head != None:
            print("->")
        
    def iterative_traverse(cls,head):
        while head != None:
            print(head.data,end="->")
            head = head.next
            # cls.delimiter(head)
            
    def recursive_traverse(cls,head):
        if head == None:
            return
        print(head.data,end="->")
        cls.recursive_traverse(head.next)
        
    def insert_begning(cls,head,val):
        new_node = Node(val)
        new_node.next = head
        head = new_node
        return new_node
    
    def insert_end(cls,head,val):
        new_node = Node(val)
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node 
        new_node.next = None            
        return head 
        
    def insert_atsomepint(cls,head,val,insertat):
        new_node = Node(val)
        curr = head
        while curr != None:
            if curr.data == insertat:
                new_node.next = curr.next
                curr.next = new_node 
            curr = curr.next            
        return head
    
    def search_linkedlist(cls,head,target):
        while head != None:
            if head.data == target:
                return "found"
            head = head.next
        return "Not found"
        
        
    def delete_node(cls,head,target):
        curr = head
        prev = None
        if head != None and head.data == target:
            head = head.next
            return head
        while curr != None and curr.data !=target:
            prev=curr
            curr = curr.next
            
        if curr == None:
            return "not found"
        prev.next = curr.next
        return head
    
    def get_size(cls,head):
        counter = 1
        while head.next != None:
            counter+=1
            head = head.next
            
        return counter    
    
    def reverse_ll(cls,head):
        curr=head
        prev = None
        nxt = ''
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def recursion_reverse_ll(cls,head):
        
        return cls.recursion_reverse(head,None)
        
    def recursion_reverse(cls,curr,prev):
        if curr == None:
            return prev
        nxt = curr.next
        curr.next = prev
        return cls.recursion_reverse(nxt,curr) ############### tail recursive because last statement is recursion call"
        
         
            
        
linkelist_obj = linkelist()
arr=[1,3,8,4,10,9]
head = create_singly_ll(arr)
# inser_beg = linkelist_obj.insert_begning(head,6)
# inser_end = linkelist_obj.insert_end(head,60)
# inser_atsomepoint = linkelist_obj.insert_atsomepint(head,55,8)
# print(linkelist_obj.search_linkedlist(head,4))
# delete = linkelist_obj.delete_node(head,1)
# print(linkelist_obj.get_size(head))
# reversed = linkelist_obj.reverse_ll(head)
recursive_reversed = linkelist_obj.recursion_reverse_ll(head)



linkelist_obj.iterative_traverse(recursive_reversed)
# linkelist_obj.recursive_traverse(head)