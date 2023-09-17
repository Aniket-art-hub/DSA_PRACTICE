from pickle import NONE
from tkinter import NO
from turtle import clone


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Createll:
    def create_ll(cls,arr):
        head = Node(arr[0])
        curr = head
        for i in range(1,len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
        return head
    
class Problem:
    
    def kth_node(cls,head,kth):
        counter = 1
        curr = head
        while curr != None:
            if counter == kth:
                return curr.data
            curr = curr.next
            counter +=1

        return "not exists"
    
    def find_size(self,head):
        counter=1
        while head.next != None:
            counter+=1
            head = head.next
        return counter
    ##################### approach 1 O(n) ##############################
    def kth_node_from_last(cls,head,kth):
        total_size = cls.find_size(head)
        kth = abs(total_size-kth)+1
        counter = 1
        curr = head
        while curr != None:
            if counter == kth:
                return curr.data
            curr = curr.next
            counter +=1

        return "not exists"
    
    ####################### Approach2 two pointer ######################################
    def kth_node_twopointer(self,head,kth):
        fast = head
        slow = head
        total_size = self.find_size(head)
        if kth > total_size:
            return "exhaust"
        for i in range(0,kth):
            fast = fast.next
            
        while fast != None:
            slow = slow.next
            fast = fast.next
        return slow.data
    
    
    def find_middle(self,head):
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
            
            
    def detect_loop(cls,head):
        slow=head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                return True
        return False
    
    def reversed(cls,head):
        curr = head
        prev = None
        nxt = ''
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
        
    def is_palindrome(cls,head):
        mid = cls.find_middle(head)
        first_half = head
        second_half = cls.reversed(mid)
        while second_half!=None:
            if first_half.data != second_half.data:
                return False
            second_half = second_half.next
            first_half = first_half.next
        return True
    
    def reverse_doubly_ll(self,head):
        prev= None
        nxt = None
        curr = head
        while curr!=None:
            prev = curr
            nxt = curr.next
            curr.next = prev
            curr.prev = nxt
            curr = curr.prev
        return prev
    
    ######################################################by using hash map  complexity O(n) and space complexity is O(n)################################################
    def findFirstNode(self, head):
        curr = head
        hash_ll = {}
        while curr.next != None:
            if curr.next in hash_ll:
                return curr.next.data
            else:
                hash_ll[curr.next]=curr.data
            curr=curr.next
        return -1
        
    ############################################## by using another approach  complexity is O(n) and time complexity is O(1)_#############################################
    def findFirstNode(self, head):
        if self.detect_loop(head):
            curr = head
            while curr.next != None:
                prev = curr.next
                curr.next = None
                curr = prev
            return curr.data
        return -1
    
    ##################### intersect twolinkedlist  HASHMAP APPROACH O(N) AND TIME IS O(N)########################
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA = headA
        currA_hash = set()
        if headA == None or headB==None:
            return 0
        while currA != None:
            currA_hash.add(currA)
            currA = currA.next
        currB = headB
        while currB != None:
            if currB in currA_hash:
                return currB
            currB = currB.next
        return 0
    
    ##################### intersect twolinkedlist  APPROACH2  ########################
    def get_size(self,head):
        counter = 0
        while head != None:
            counter+=1
            head = head.next
        return counter
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA_size = self.get_size(headA)
        currB_size = self.get_size(headB)
        diff = abs(currA_size-currB_size)
        while diff>0:
            if currA_size>currB_size:
                headA = headA.next
            else:
                headB = headB.next 
            diff -=1
        while headA != None and headB != None:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    
    ################## alternatesplit ll #########################################
    def alternatingSplitList(head):
    #Your code here
        count = 1
        head1 = []
        head2 = []
        if head == None or head.next==None:
            return head
        while head != None:
            if count%2 != 0:
                head1.append(head.data)
            else:
                head2.append(head.data)
            count += 1
            head = head.next
        create_ll_obj = Createll()
        ll1 = create_ll_obj.create_ll(head1)
        ll2 = create_ll_obj.create_ll(head2)
        return ll1

    
    #########################   merge two sorted linkedlist ###############################
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2==None:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            list1 = head.next
        else:
            head = list2
            list2 = head.next
        curr = head
        while list1 != None and list2 != None:
            if list1.val<=list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        while list1 != None:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2 != None:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return head
    
    
    #################### next gretaer number right O(N) and space is also O(N) ################################
    def get_size(self,data):
        count = 0
        while data != None:
            count+=1
            data = data.next
        return count
    def convert_array(self,size,head):
        array_ll = []
        while head != None:
            next_data = head.val
            array_ll.append(next_data)
            head = head.next
        return array_ll
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        size = self.get_size(head)
        array_data = self.convert_array(size, head)
        stack = []
        nextgreater = [0]*size
        for i in range(size):
            while stack and (array_data[i] > array_data[stack[-1]]):
                nextgreater[stack[-1]] = array_data[i]
                stack.pop()
            stack.append(i)
        return nextgreater


    #####################  add two number #####################################
    def reverse(self,head):
        prev = None
        nxt = None
        curr=head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        head = None
        curr = None
        sum = val = carryover =  0
        while l1 != None and l2 != None:
            sum = l1.val+l2.val+carryover
            val = sum%10
            carryover = sum/10
            if head == None:
                head = Node(val)
                curr = head
            else:
                curr.next = Node(val)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            sum = l1.val + carryover
            val = sum % 10
            carryover = sum/10
            curr.next = Node(val)
            curr = curr.next
            l1 = l1.next

        while l2 != None:
            sum = l2.val + carryover
            val = sum % 10
            carryover = sum/10
            curr.next = Node(val)
            curr = curr.next
            l2 = l2.next

        if carryover != 0:
            curr.next = Node(carryover)
        return head
    
    ####################### merger sort linkedlist ##################
    def find_middle_revaamp(self,head):
        slow = fast = head
        while fast.next != None and fast.next.next!= None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeSort(self,head):
        curr = head
        if curr == None or curr.next==None:
            return curr
        get_middle = self.find_middle_revaamp(curr)
        midNext = get_middle.next
        get_middle.next = None
        first_half = self.mergeSort(curr)
        second_half = self.mergeSort(midNext)

        return self.merge_linkeslist(first_half,second_half)

    def merge_linkeslist(self, first_half, second_half):
        if first_half == None:
            return second_half
        if second_half == None:
            return first_half
        if first_half.data < second_half.data:
            head = first_half
            first_half = first_half.next
        else:
            head = second_half
            second_half = second_half.next
        curr=head
        while first_half != None and second_half != None:
            if first_half.data < second_half.data:
                curr.next = first_half
                first_half = first_half.next
            else:
                curr.next = second_half
                second_half = second_half.next
            curr = curr.next
        
        while first_half != None:
            curr.next = first_half
            first_half = first_half.next
            curr = curr.next
        while second_half != None:
            curr.next = second_half
            second_half = second_half.next
            curr = curr.next

        return head
    

    def deleteNode(self,llist, position):
        # Write your code here
        count = 0
        curr = llist
        if position==0:
            llist = llist.next
            return llist
        while curr != None and count<position:
            prev = curr
            curr = curr.next
            count+=1
        if count<position:
            return "position out of range"
        prev.next = curr.next
        return llist
    
    def even_odd_linkedlist(self,head):
        even_head = even = Node(None)
        odd_head = odd = Node(None)
        curr = head
        while curr != None:
            if curr.data %2 == 0:
                even.next = curr
                even = even.next
            else:
                odd.next = curr
                odd = odd.next 
            curr = curr.next
        even.next = odd_head.next
        odd.next = None
        return even_head.next 

    def RotateLL(self,head, k):
        # Write your code here
        if k==0 or start == None:
            return start
        counter = 1
        tempNode = start
        while tempNode != None and counter< k:
            tempNode = tempNode.next
            counter +=1
        curr = tempNode
        while curr.next != None:
            curr = curr.next
        
        curr.next = start
        start = tempNode.next
        tempNode.next = None
        return start 

    def ReverseKLL(self,start, k):  ########### 0(n) and space is O(n) due to recursive stack memory
        # Write your code here
        if start==None or k<=1:
            return start
        curr = start
        prev = None
        nxt = None
        counter = 1
        while curr!= None and counter<=k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            counter+=1

        start.next = self.ReverseKLL(curr,k)
        return prev         


    def removeDuplicates(self,llist): ##### O(n) and space is O(1)
        # Write your code here
        curr = llist
        while curr != None and curr.next != None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return llist 


    def flattering(self,head):
        curr = head
        flatten = None
        while curr != None:
            flatten = self.merge_flatten(flatten,curr)
            curr = curr.data
        return flatten
    
    def merge_flatten(self,head1,head2):
        if head1 == None:
            return head2
        if head2==None:
            return head1
        if head1.data<head2.data:
            head = head1
            head1 = head1.next
        if head2.data<head1.data:
            head = head2
            head2 = head2.next
        curr=head
        while head1!=None and head2!=None:
            if head1.data<head2.data:
                curr.next = head1
                head1=head1.next
            else:
                curr.next = head2
                head2=head2.next
            curr=curr.next

        while head1!=None:
            curr.next = head1
            head1 = head1.next
            curr = curr.next

        while head2 != None:
            curr.next = head2
            head2 = head2.next
            curr = curr.next

        return head
    ######################  flattened linkedlist comlexity is O(n) #############################
    def flatten(root):
        #Your code here
        curr = root
        flatten_ll = None
        while curr != None:
            flatten_ll = merge_sorted(flatten_ll,curr)
            curr = curr.next
        return root

    def merge_sorted(head1,head2):
        if head1 == None:
            return head2
        if head2==None:
            return head1
        if head1.data<=head2.data:
            head = head1
            head1 = head1.bottom
        else:
            head = head2
            head2 = head2.bottom
            
        curr = head
        while head1!=None and head2!=None:
            if head1.data<=head2.data:
                curr.bottom = head1
                head1 = head1.bottom
            else:
                curr.bottom = head2
                head2 = head2.bottom
            curr = curr.bottom
        
        while head1 != None:
            curr.bottom = head1
            head1 = head1.bottom
            curr = curr.bottom

            
        while head2 != None:
            curr.bottom = head2
            head2 = head2.bottom
            curr = curr.bottom

            
        return head


    ##################### APPROACH 1 cloning linkedlist  O(n) and extar space is O(n) for extar map ####################################
    def clone_linkedlist(self,head):
        map = {}
        clone_head = Node(head.data)
        clone_curr = clone_head
        curr = head
        curr = curr.next
        map[curr] = clone_curr
        while curr != None:
            temp= Node(curr.data)
            map[curr] = temp
            clone_curr.next = temp
            curr = curr.next
            clone_curr = clone_curr.next
        #update random pointer
        curr = head
        while curr != None:
            map.get(curr).random = map.get(curr.random)
            curr = curr.next
        return clone_head
    
    ################# APPROACH 2 without USING EXTRA SPACE O(n)###################################
    def cloning_with_random(self,head):
        curr = head
        temp = None
        while curr != None :
            temp = Node(curr.data)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        curr = head
        while curr != None:
            if curr.random != None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        clonehead = head.next
        clonecurr = clonehead
        while clonecurr!=None and clonecurr.next != None:
            curr.next = curr.next.next
            clonecurr.next = clonecurr.next.next
            clonecurr = clonecurr.next
            curr = curr.next
        curr.next = None
        clonecurr.next = None
        return clonehead


            
    


        


            


        
        

        
            
    
        
    
        
        
        
# arr=[7,10,11,12,76,32,76,90]
arr = [1,1,2,1]
create_ll_obj = Createll()
head = create_ll_obj.create_ll(arr)
problem_obj = Problem()
# print(problem_obj.kth_node(head,4))
# print(problem_obj.kth_node_twopointer(head,19))
# print(problem_obj.find_middle(head))
# print(problem_obj.is_palindrome(head))

print(problem_obj.delete_node(3,head))


        