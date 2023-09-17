#find target 10 by O(n^2) complexity
nums = [2,5,1,7,4,9,8]
target = 10
def get_target(nums,target):
    index = []
    for i in range(0,len(nums)-1):
        if index:
            break
        for j in range(0,len(nums)-1):
            target_data = nums[i] + nums[j+1]
            if target_data==target:
                index.append(i)
                index.append(j+1)
                break
    if not index:
        return False
    else:
        return index

print(get_target(nums,target))

#find target 10 by O(n) complexity by two pointer approach

nums = [2,5,1,7,4,9,8]
target = 10
def get_target(nums,target):
    index = []
    nums.sort()
    l = 0
    r = len(nums)-1
    for i in range(0, len(nums)-1):
        target_data = nums[l]+nums[r]
        if target_data > target:
            r-=1
        elif target_data < target:
            l+=1
        else:
            break
    index.append(l)
    index.append(r)
    return index
        

print(get_target(nums,target))

