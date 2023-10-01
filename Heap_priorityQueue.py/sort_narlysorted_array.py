# By using priority queue  complexity is :---      O(n*logk)
import heapq
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        if n==0:
            return
        pq=[]
        for i in range(n):
            heapq.heappush(pq,(a[i]))
        for i in range(n):
            a[i] = heapq.heappop(pq)
        return a
        