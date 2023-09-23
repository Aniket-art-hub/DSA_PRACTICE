####################################################      TRIPLET SUM    ###################################################

#three element their sum is equal to target

arr = [1,2,5,3,9,4]
target = 7
# approach 1 by naive approach complexity  O(n^3)

def sum(arr,target):
    result_arr = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == target:
                    result_arr.append(arr[i])
                    result_arr.append(arr[j])
                    result_arr.append(arr[k])
                    return result_arr
# print(sum(arr,target))

#approach 2 by two pointer O(n^2)

def triplet(arr,target):
    arr.sort() #nlogn
    for i in range(len(arr)):
        pair_sum = target-arr[i]
        l = i+1
        r =len(arr)-1
        while(l<r):
            sum = arr[l] + arr[r]
            if sum == pair_sum:
                return [arr[i],arr[l],arr[r]]
            elif sum > target:
                r-=1
            else:
                l+=1
                
# print(triplet(arr,target))

# approach 3 by hashmap time -> O(N^2) space -> O(N)

def by_hashmap(arr,target):
    for i in range(len(arr)):
        s = dict()
        triple_sum = target-arr[i]
        for j in range(i+1,len(arr)):
            check_element = triple_sum-arr[j]
            if check_element in s:
                return [i,j,s[check_element]]
            else:
                s[arr[j]] = j
            
# print(by_hashmap(arr,target))

# approach 4 by binary search O(n^2logn)
def binary_search(arr,l,single_sum):
    r = len(arr)-1
    while(l<=r):
        mid = int(l+(r-l)/2)
        if arr[mid] == single_sum:
            return arr[mid]
        elif arr[mid] > single_sum:
            r-=1
        else:
            l+=1
    return -1
def triplet_binary_search(arr,target):
    arr.sort()
    for i in range(len(arr)):
        sum = target-arr[i]
        for j in range(i+1,len(arr)):
            single_sum = sum-arr[j]
            value = binary_search(arr,i+1,single_sum)
            if value > 0:
                return [arr[i],arr[j],value]
    return -1

# print(triplet_binary_search(arr,target))


#################################      BITONIC POINT FIND    ######################################

arr = [3,5,7,9,15,12,9,5,4,2]

# aproach 1 By naive approach O(n)

def bitonic_point(arr):
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            return arr[i]
        
# print(bitonic_point(arr)) O(logn)

def find_bitonic(arr):
    l=0
    r = len(arr)-1
    while(l<=r):
        mid = int(l+(r-l)/2)
        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid]<arr[mid-1]:
            r -=1
        else:
            l+=1
# print(find_bitonic(arr))



################################      ROTATE ARRAY left side BY D TIME    ##################################

arr=[4,7,2,1,9,10,12]
d = 2
# output = [2,1,9,10,12,4,7]

# approach 1 naive approach 

def array_rotate(arr,d):
    temp = []
    for i in range(d,len(arr)):
        temp.append(arr[i])
    for i in range(d):
        temp.append(arr[i])
    return temp
    

# print(array_rotate(arr,2))

# approach2  by reverse array O(N) O(1)

def reverse_roatate(arr,d):
    d = d%len(arr)
    reverse_array(arr,0,d-1)
    reverse_array(arr,d,len(arr)-1)
    reverse_array(arr,0,len(arr)-1)
    return arr

def reverse_array(arr,l,h):
    while l<=h:
        temp = arr[l]
        arr[l] = arr[h]
        arr[h] = temp
        l+=1
        h-=1

# print(reverse_roatate(arr,d))


############################ search in rotated array  ####################################
arr = [4,9,10,12,2,3]
target = 4
# step 1 find pivot by binary search
def get_pivot(arr):
    l=0
    r=len(arr)-1
    while (l<r):
        mid = int(l+(r-l)/2)
        if arr[mid] >= arr[0]:
            l=mid+1
        else:
            r = mid
    return l

def search_rotated_array(arr,target):
    pivot = get_pivot(arr)
    if arr[pivot] <= target <= arr[len(arr)-1]:
        search_index = binary_search(arr,pivot,len(arr)-1,target)
    else:
        search_index = binary_search(arr,0,pivot-1,target)
    return search_index
        
def binary_search(arr,l,r,target):
    while (l<=r):
        mid = int(l+((r-l)/2))
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            r=mid-1
        else:
            l=mid+1
    return -1

# print(search_rotated_array(arr,target))

        
def trap_rain_water(arr):
    """
    :type height: List[int]
    :rtype: int
    """
    #approach1
     
    right_max[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        right_max[i] = max(arr[i],right_max[i+1])
    print(right_max)
    save_water=0
    for i in range(len(arr)):
        save_water += (min(left_max[i],right_max[i])-arr[i])
    return save_water

# approach2 by two pointer fail for [5,5,1,7,1,1,5,2,7,6]
    # n = len(arr)
    # l=0
    # r=n-1
    # left_max = arr[0]
    # right_max=arr[n-1]
    # save_water = 0
    # while l<r:
    #     if arr[l] <= right_max:
    #         if arr[l] < left_max:
    #             save_water += left_max - arr[l]
    #         else:
    #             left_max = arr[l]
    #         l+=1
    #     else:
    #         if arr[r] < right_max:
    #             save_water += right_max-arr[r]
    #         else:
    #             right_max = arr[r]
    #         r-=1
    # return save_water

arr =[0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
print(trap_rain_water(arr))


###################################   find subarray approach1 O(n^2)#########################################

def get_subarray(arr,target):
    for i in range(len(arr)):
        currentsum = arr[i]
        for j in range(i+1,len(arr)):
            currentsum += arr[j]
            if currentsum == target:
                return i,j

arr=[3,8,9,12,4,3,9]
target = 19 
# print(get_subarray(arr,target))

#################  approach 2 O(n)  ########################

def subarray(arr,target):
    i=0
    j=0
    sum = arr[0]
    while i<=j and j<len(arr):
        if sum == target:
            return i,j
        elif sum < target:
            j+=1
            sum += arr[j]
            
        else:
            sum -= arr[i]
            i+=1
           

arr=[3,8,9,12,4,3,9]
target = 29
print(subarray(arr,target))
        