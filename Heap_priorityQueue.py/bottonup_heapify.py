import math
class HeapImplementation:
    def build_heapify(self,arr):
        n = len(arr)
        if n==0:
            return arr
        for i in range(len(arr)):
            self.bottomup_heapify(arr,n,i)
        return arr
    
    
    def bottomup_heapify(self,arr,n,i):
        parent = math.ceil((i-1)/2)
        if parent>=0:
            if arr[parent]<arr[i]:
                self.swap(arr,i,parent)
                self.bottomup_heapify(arr,n,parent)
            
    def swap(self,arr,n1,n2):
        arr[n1],arr[n2] = arr[n2],arr[n1]
        
        
        
build_heap = HeapImplementation()
arr=[1,3,4,2,11,10,20]
print(build_heap.build_heapify(arr))