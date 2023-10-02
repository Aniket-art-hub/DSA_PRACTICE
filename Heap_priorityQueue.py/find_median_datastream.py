import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        if len(self.max_heap)==0 or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap,(-heapq.heappop(self.min_heap))) 

    def findMedian(self) -> float:
        if len(self.max_heap)==0:
            return -1
        if len(self.max_heap)==len(self.min_heap):
            # print(heapq.heappop(self.max_heap)[1])
            # print(heapq.heappop(self.min_heap))
            return ((-self.max_heap[0])+self.min_heap[0])/2
        elif len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]

        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


########### hackerrank sol

max_heap = []
min_heap = []
median = []

def runningMedian(a):
    # Write your code here
    for i in range(len(a)):
        if not max_heap or a[i] <= -max_heap[0]:
            heapq.heappush(max_heap,-a[i])
        else:
            heapq.heappush(min_heap,a[i])
        if len(max_heap) - len(min_heap) > 1:
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        elif len(min_heap) - len(max_heap) > 1:
            heapq.heappush(max_heap,-heapq.heappop(min_heap)) 
        if len(max_heap)==0:
            return -1
        if len(max_heap)==len(min_heap):
            # print(heapq.heappop(self.max_heap)[1])
            # print(heapq.heappop(self.min_heap))
            ans = ((-max_heap[0])+min_heap[0])/2
        elif len(max_heap)>len(min_heap):
            ans = float(-max_heap[0])
        else:
            ans = float(min_heap[0])
        median.append(ans)
    return median
    