################# O(2^N) AND SPACE IS o(N) ##################################
class SubSet:
    def find_subset(cls,arr,target):
        subset_result = []
        cls.traverse_arr(arr,subset_result,target,0)
        
    def traverse_arr(cls,arr,subset_result,target,current_index):
        if target==0:
            print(subset_result)
            return
        if current_index == len(arr):
            return
        #in case of not select value
        cls.traverse_arr(arr,subset_result,target,current_index+1)
        
        #in case of select data
        subset_result.append(arr[current_index])
        cls.traverse_arr(arr,subset_result,target-arr[current_index],current_index+1)
        subset_result.remove(arr[current_index])
        
        
SubSet_obj = SubSet()
arr = [2,3,5]
target = 7
print(SubSet_obj.find_subset(arr,target))