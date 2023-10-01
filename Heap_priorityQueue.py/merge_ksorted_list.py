# solve by using priority queue  complexity is O(n*k)
import heapq
#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MergeKsortedList:
    def mergeKLists(self, lists):
        if not lists:
            return 
        pq=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))
        root =ListNode(0)
        curr = root
        while len(pq)>0:
            _, idx, node = heapq.heappop(pq)
            curr.next = node
            curr=curr.next
            if node.next != None:
                heapq.heappush(pq,(node.next.val,idx,node.next))
        return root.next
            
        
        