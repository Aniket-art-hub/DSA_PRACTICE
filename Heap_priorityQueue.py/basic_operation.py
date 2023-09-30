class BasicOperation:
    def insert_heapify(self,arr,value):   ####### O(n*logn)
        arr.append(value)
        n=len(arr)

        for i in range(int((n-1)/2),-1,-1):
            self.topdown_heapify(arr,n,i)
        return arr
        
    def topdown_heapify(self,arr,n,i):
        left,right,largest = 2*i+1,2*i+2,i
        if left<n and arr[left]>arr[largest]:
            largest=left
        if right<n and arr[right]>arr[largest]:
            largest = right
        
        if largest != i:
            self.swap(arr,i,largest)
            self.topdown_heapify(arr,n,largest)
            
    def swap(self,arr,n1,n2):
        temp = arr[n1]
        arr[n1]=arr[n2]
        arr[n2]=temp
        
        
        
        
        
        
        
        
        
arr=[20, 11, 10, 2, 3, 1, 4]
BasicOperation = BasicOperation()
print(BasicOperation.insert_heapify(arr,5))