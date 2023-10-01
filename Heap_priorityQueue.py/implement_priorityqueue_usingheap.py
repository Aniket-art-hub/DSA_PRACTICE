from typing import List

def pop(heap: List[int]) -> int:
    # Write your code here.
    n=len(heap)
    if n==0:
        return -1
    top = heap[0]
    heap[0]=heap[n-1]
    del heap[n-1]
    top_down_heapify(heap,0)
    return top

def top_down_heapify(arr,index):
    left = 2*index+1
    right = 2*index+2
    largest = index
    n=len(arr)
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right] > arr[largest]:
        largest = right
        
    if largest!=index:
        swap(arr,index,largest)
        top_down_heapify(arr,largest) 
        
def swap(arr,n1,n2):
    arr[n1],arr[n2] = arr[n2],arr[n1]
       
        