# Left side less right side more

def right_left_side(arr):
    n=len(arr)
    left_array = [None]*n
    left_array[0] = arr[0]
    for i in range(1,n):
        left_array[i] = max(left_array[i-1],arr[i-1])
    right_array=[None]*n
    right_array[n-1] = arr[n-1]
    for j in range(n-2,-1,-1):
        right_array[j]=min(right_array[j+1],arr[j])
        
    for i in range(1,n-1):
        if left_array[i-1] <= arr[i]  and arr[i]<=right_array[i+1]:
            return arr[i]
    return -1
    
   
    
arr = [4,3,2,1,5,9,8,7]
print(right_left_side(arr))