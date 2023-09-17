def generate_next_greater(number):
    arr = [int(x) for x in str(number)]  
    n = len(arr)-1
    is_swap = False
    while n >=0:
        if arr[n-1] < arr[n] and (n-1)>=0:
            is_swap = True
            small_number = n-1
            break
        n-=1
    if not is_swap:
        return -1
    else:
        while n > small_number:
            if arr[n] > arr[small_number]:
                swap(arr,n,small_number)
                break
            n-=1
        concatarray=''
        for i in range(0,small_number+1):
            concatarray+=str(arr[i])
        for j in range(len(arr)-1,small_number,-1):
            concatarray+=str(arr[j])
    return concatarray
def swap(arr,n,small_number):
    arr[n] = arr[n]+arr[small_number]
    arr[small_number] = arr[n]-arr[small_number]
    arr[n] = arr[n]-arr[small_number]
   
        
number = 765       
print(generate_next_greater(number))