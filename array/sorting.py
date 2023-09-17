############################################# bubble sort O(n^2) ###########################################

def swapping(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


def bubble_sort(arr):
    for i in range(len(arr)):
        is_swap = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                is_swap = True
                swapping(arr,i,j)
        if not is_swap:
            break
    return arr
arr = [3,7,4,10,11,20,13]
# print(bubble_sort(arr))

#####################################  selection sort O(n^2) ####################################################################

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        swapping(arr,i,min_index)
    return arr

arr = [3,7,4,10,11,20,13]
# print(selection_sort(arr))

###############################  insertion sort O(n^2) ########################################################################

def insertion_sort(arr):
    for i in range(1,len(arr)):
        hole = i-1
        value=arr[i]
        while (hole>=0 and arr[hole] >= value):
            arr[hole+1] = arr[hole]
            hole-=1
        arr[hole+1] = value
    return arr

arr = [3,7,4,10,11,20,13]

# print(insertion_sort(arr))


###################################  merge sort O(nlogn) space height of recrusive call #######################################################################

def merge_sort(arr):
    return splitandmerge(arr,0,len(arr)-1)
    
    
def splitandmerge(arr,l,r):
    if l<r:
        mid = int(l+((r-l)/2))
        splitandmerge(arr,l,mid)
        splitandmerge(arr,mid+1,r)
        mergearray(arr,l,mid,r)
    return arr
        
        
def mergearray(arr,l,mid,r):
    n1 = mid-l+1
    n2 = r-mid
    right = [0 for i in range(n1)]
    left = [0 for i in range(n2)]
    for i in range(n1):
        left[i] = arr[i+l]
    for i in range(n2):
        right[i] = arr[i+mid+1]
    i,j=0,0
    k=l 
    while i<n1 and j<n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    
    while i<n1:
        arr[k] = left[i]
        k+=1
        i+=1
    while j<n2:
        arr[k] = right[j]
        k+=1
        j+=1
    return arr
        
arr=[3,7,4,10,11,2,20,13]
# print(merge_sort(arr))


#########################################  QUICK SORT average comlexity O(nlogn) worst case O(n^2) ###################################################

def quick_sort(arr):
    return partitionandsort(arr,0,len(arr)-1)

def partitionandsort(arr,l,r):
    if l < r:
        pivotIndex = getpivot(arr,l,r)
        partitionandsort(arr,l,pivotIndex-1)
        partitionandsort(arr,pivotIndex+1,r)
    return arr
    

def getpivot(arr,l,r): 
    pivot = arr[r]
    i=l
    j=l-1
    while i<r:
        if arr[i]<pivot:
            j+=1
            swapping(arr,i,j)
        i+=1
    swapping(arr,i,j+1)
    return j+1
        

          
arr=[3,7,4,10,11,2,20,13]
print(quick_sort(arr))         
        


    
    

        
    
