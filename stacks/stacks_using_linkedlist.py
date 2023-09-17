from email import header


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Convertll:
    def convert_ll(self,arr):
        head = Node(arr[0])
        curr = head
        for i in range(1,len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
        return head

class UsingLinkedlist:
    head = None
    def push_element(self,data):
        new_node = Node(data)
        new_node.next=head
        head = new_node
        return head.data
    
    def pop_element(self):
        if UsingLinkedlist.head != None:
            curr = UsingLinkedlist.head
            data = curr.data
            head = curr.next
            curr.next = None
            return data
        
    def top__peek_element(self):
        if UsingLinkedlist.head != None:
            return UsingLinkedlist.head.data
        
    def is_empty(self):
        if UsingLinkedlist.head == None:
            return 'Yes'
        else:
            return 'No'
        
    def get_size(self):
        curr =  UsingLinkedlist.head
        counter = 0
        while curr != None:
            curr = curr.next
            counter+=1
        return counter


    


using_linkedlist_obj = UsingLinkedlist()
arr = [2,4,5,12,21,11,33,9]
convert_arr_to_linkedlist_obj = Convertll()
arr = convert_arr_to_linkedlist_obj.convert_ll(arr)
print(using_linkedlist_obj.push_element(arr))
        
