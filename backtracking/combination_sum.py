def combination_sum(arr,n,target):
    possible_combination = []
    get_all_combinations(arr,target,0,possible_combination)
    
    
def get_all_combinations(arr,target,index,possible_combination):
    if target==0:
        print(possible_combination)
        return 
    if index == len(arr):
        return
    ## ignore case
    get_all_combinations(arr,target,index+1,possible_combination)
    ## in accept case
    possible_combination.append(arr[index])
    get_all_combinations(arr,target-arr[index],index+1,possible_combination)
    possible_combination.pop()





arr=[10, 1, 2, 7, 6, 1, 5]
target=8
n = len(arr)
combination_sum(arr,n,target)