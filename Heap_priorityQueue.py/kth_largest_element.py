
import heapq
class Solution:
    
    ######## Approach 1 by sorting ##############
    ## comlexity will be O(nlogn)
    
    ##### Approach 2 by using max heap
    # complexity will be O(nlogn)
    # because first we create max heap and insert n element so complexity will be O(nlogn)
    
    
    
    ##### More optimise way by using min heap
    # complexity will be O(nlogk)
    def findKthLargest(self, nums, k) :
        if len(nums)==0:
            return 0
        pq=[]
        for i in range(len(nums)):
            heapq.heappush(pq,nums[i])
            if len(pq)>=k:
                heapq.heappop(pq)
        return heapq.heappop(pq)
        