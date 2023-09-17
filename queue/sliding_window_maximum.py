import collections

class SlidingWindow:
    def brute_force(self,arr,k):
        result_array=[]
        for i in range(len(arr)-k+1):
            max_window = arr[i]
            for j in range(i,i+k):
                max_window = max(max_window,arr[j])
            result_array.append(max_window)
        return result_array
    
    def maxslidingwindow(self,nums,k):
        n=len(nums)
        max_sliding_window=[]
        d=collections.deque()
        i=0
        while i<k:
            while d and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)
            i+=1
        while i<n:
            max_sliding_window.append(nums[d[0]])
            #out of window condition check
            if d and (i-d[0]>=k):
                d.popleft()
            
            # remove all the element which is smaller
            while d and (nums[d[-1]]<=nums[i]):
                d.pop()
            d.append(i)
            i+=1
        max_sliding_window.append(nums[d[0]])
        return max_sliding_window

        
    
    
nums = [-7,-8,7,5,7,1,6,0]
k=4
SlidingWindow=SlidingWindow()
# print(SlidingWindow.brute_force(nums,k))
print(SlidingWindow.maxslidingwindow(nums,k))
# SlidingWindow.maxslidingwindow(nums,k)