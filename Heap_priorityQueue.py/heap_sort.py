class HeapSort:
    def heapSort(self,arr,n):
        heapify_arr = self.build_heapify(arr)
        while n>0:
            self.swap(arr,0,n-1)
            n-=1
            self.topdown_heapify(arr,n,0)
        return arr
        
    
    
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
        
        
        
heap_sort  = HeapSort()
arr=[3,4,2,1,11,10,20]
print(heap_sort.build_heapify(arr))
print(heap_sort.heapSort(arr,len(arr)))