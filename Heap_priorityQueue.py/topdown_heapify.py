class HeapImplementation:
    def build_heapify(self,arr):
        n = len(arr)
        if n==0:
            return arr
        for i in range(int((n-1)/2),-1,-1):
            self.topdown_heapify(arr,n,i)
        return arr
    
    
    def topdown_heapify(self,arr,n,i):
        left,right,largest = 2*i+1,2*i+2,i
        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest>i:
            self.swap(arr,i,largest)
            self.topdown_heapify(arr,n,largest)
            
    def swap(self,arr,n1,n2):
        arr[n1],arr[n2] = arr[n2],arr[n1]
        
        
        
build_heap = HeapImplementation()
arr=[1,3,4,2,11,10,20]
print(build_heap.build_heapify(arr))