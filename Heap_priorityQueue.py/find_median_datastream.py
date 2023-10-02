import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        if len(self.max_heap)==0 or num < self.max_heap[0][1]:
            heapq.heappush(self.max_heap,(-num,num))
        else:
            heapq.heappush(self.min_heap,num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap,heapq.heappop(self.max_heap)[1])
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap,(-heapq.heappop(self.min_heap),heapq.heappop(self.min_heap))) 

    def findMedian(self) -> float:
        if len(self.max_heap)==0:
            return -1
        if len(self.max_heap)==len(self.min_heap):
            # print(heapq.heappop(self.max_heap)[1])
            # print(heapq.heappop(self.min_heap))
            return (self.max_heap[0][1]+self.min_heap[0])/2
        elif len(self.max_heap)>len(self.min_heap):
            return self.max_heap[0][1]
        else:
            return self.min_heap[0]
