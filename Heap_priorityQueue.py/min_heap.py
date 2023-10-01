class MinHeap:
    def build_min_heap(self,arr):
        n=len(arr)
        ## topdown heapify use this
        for i in range(int((n-1)/2),-1,-1):
            self.top_down_heapify(arr,n,i)
        ## bottom up heapify
        # for i in range(n):
        #     self.bottom_up_heapify(arr,n,i)
        return arr
    
    
    def top_down_heapify(self,arr,n,i):
        left=2*i+1
        right = 2*i+2
        smallest = i
        if left < n and arr[left]<arr[smallest]:
            smallest = left
        if right < n and arr[right]<arr[smallest]:
            smallest = right
            
        if smallest != i:
            self.swap(arr,i,smallest)
            self.top_down_heapify(arr,n,smallest)
    
    def bottom_up_heapify(self,arr,n,i):
        parent = int((i-1)/2)
        if parent >= 0:
            if arr[parent] > arr[i]:
                self.swap(arr,i,parent)
                self.bottom_up_heapify(arr,n, parent)
            
            
    def swap(self,arr,n1,n2):
        arr[n1],arr[n2] = arr[n2],arr[n1]
        
        
    def insert_min_heap(self,arr,data):
        arr.append(data)
        n=len(arr)
        return self.build_min_heap(arr)
    
    def delete(self,arr,index):
        if len(arr)==0 or index > len(arr):
            return 0
        arr[index] = arr[len(arr)-1]
        del arr[len(arr)-1]
        return self.build_min_heap(arr)
    
    def extract_top(self,arr):
        if len(arr)==0:
            return 0
        top=arr[0]
        self.delete(arr,0)
        return top
        
        
        
min_heap_obj = MinHeap()
arr=[1,3,4,2,11,10,20]
print(min_heap_obj.build_min_heap(arr))
print(min_heap_obj.insert_min_heap(arr,1))
print(min_heap_obj.delete(arr,2))
print(min_heap_obj.extract_top(arr))