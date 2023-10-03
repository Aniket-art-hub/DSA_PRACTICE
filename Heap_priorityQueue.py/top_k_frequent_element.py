import heapq
class Solution:
    def topKFrequent(self, nums, k):
        hash_map={}
        for i in range(len(nums)):
            if hash_map and nums[i] in hash_map:
                hash_map[nums[i]] +=1
            else:
                hash_map[nums[i]]=1
        frequent_element = []
        for key , count in hash_map.items():
            heapq.heappush(frequent_element,(-count,key))
        result=[]
        for i in range(k):
            freq,num = heapq.heappop(frequent_element)
            result.append(num)
        return result
    
    
Solution=Solution()
arr = [5,3,1,1,1,3,73,1]
print(Solution.topKFrequent(arr,2))
            
                
        