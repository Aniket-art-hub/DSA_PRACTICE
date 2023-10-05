import heapq
class JessieAndCookies:

    def cookies(k, A):
        # Write your code here
        n=len(A)
        if n<=0:
            return -1
        heap=[]
        for i in range(n):
            heapq.heappush(heap,A[i])
        count=0
        while heap[0]<=k and len(heap)>1:
            first_data=heapq.heappop(heap)
            second_data=heapq.heappop(heap)
            heapq.heappush(heap,first_data+(2*second_data))
            count+=1
        if heap[0]>=k:
            return count
        return -1
            
        
    