class Array:
    
    def linear_serach(self,arr,target):
        n = len(arr)
        for i in range(0,n+1):
            if arr[i] == target:
                return i
        return -1
    
arr = [2,6,7,3,9]
target = 7
array = Array()
# print(array.linear_serach(arr,target))

def three_sum(n,arr,target):
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                sum = arr[i]+arr[j]+arr[k]
                if sum == target:
                    return arr[i],arr[j],arr[k]
    return 0
                
    
arr=[-1, 2, 1, -4]
target  = 1
# print(three_sum(len(arr),arr,target))

def three_sum_approach2(n,arr,target):
    arr.sort() 
    for i in range(n-1):
        l=0
        r=n-1
        new_target = target-arr[i]
        while l < r:
            sum = arr[l]+arr[r]
            if sum == new_target:
                return arr[l],arr[r],arr[i]
            if sum < new_target:
                l+=1
            else:
                r-=1
    return -1

arr=[-1, 2, 1, -4]
target  = 1
# print(three_sum_approach2(len(arr),arr,target))


def three_sum_approach3(n,arr,target):
    hash_data = set()
    for i in range(n-1):
        new_target = target-arr[i]
        for j in range(i+1,n):
            sum = new_target-arr[j]
            if sum in hash_data:
                return i,j,hash_data[sum]

            else:
                hash_data.add(arr[j])
    return 0

    
arr=[1, 4, 45, 6, 10, 8]
target  = 22
# print(three_sum_approach3(len(arr),arr,target))
import sys
def closest_sum_triplet(target,arr):
    arr.sort()
    closest_sum = sys.maxsize
    n = len(arr)
    for i in range(n-2):
        l=i+1
        r=len(arr)-1
        while l < r:
            sum = arr[i]+arr[l]+arr[r]
            if abs(target-sum)<abs(target-closest_sum):
                closest_sum = sum
            if sum>target:
                l+=1
            else:
                r-=1
    return closest_sum

arr=[-1,2,1,-4]
target=1
print(closest_sum_triplet(target,arr))
    


            