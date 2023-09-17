def permutation(arr):
    all_permutation=[]
    mark_visited = [-1]*len(arr)
    if len(arr)==1:
        return arr
    if len(arr)==0:
        return []
    all_possible_permutation(arr,all_permutation,mark_visited)
    print(all_permutation)
    
    
def all_possible_permutation(arr,all_permutation,mark_visited):
    for i in range(len(arr)):
        next_element =  arr[i]
        if check_isSafe(arr,i,mark_visited):
            mark_visited[i] = 1   
            all_permutation.append(next_element)        
            all_possible_permutation(arr,all_permutation,mark_visited)
            mark_visited[i] = -1
            
        
def check_isSafe(arr,current_index,mark_visited):
    if mark_visited[current_index] == 1:
        return False
    if current_index>0 and arr[current_index] == arr[current_index-1] and mark_visited[current_index-1]==-1:
        return False
    return True

    
arr=[1,2,3]
permutation(arr)