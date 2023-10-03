import heapq
# initialize variable
heap=[]
delset = set()
for i in range(int(input())):
    split_input = list(map(int,input().split()))
    
    if split_input[0]==1:
        heapq.heappush(heap,split_input[1])
        delset.add(split_input[1])
    elif split_input[0]==2:
        delset.discard(split_input[1])
    else:
        while heap[0] not in delset:
            heapq.heappop(heap)
        print(heap[0])