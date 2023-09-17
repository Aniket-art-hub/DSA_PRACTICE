class BitManipulation:
    def get_ith_bit(self,n,i):
        if ((n & (1<<(i-1)))==0):
            return 0
        return 1
    
    def set_ith_bit(self,n,i):
        return (n | (1<<(i-1)))
    
    def clear_ith_bit(self,n,i):
        return (n & (~(1<<(i-1))))
    
    
 
bit = BitManipulation()
# print(bit.get_ith_bit(5,2))  # output 0 but with (i) get incorrect output is 1 
# print(bit.set_ith_bit(5,2)) # output 7  but without (i) get output is 5
# print(bit.clear_ith_bit(5,3)) #output 1 but without (i) get output is 5




class BitManipulationAssignment:
    
    def getithbit(self,num,i):
        if num !=0 and (num & (1<<(i-1)) == 0):
            return 0
        return 1
    
    def setithbit(self,num,i):
        return (num | (1<<(i-1)))
    
    def clearithbit(self,num,i):
        return (num & ~(1<<(i-1)))
    
    
# bitassignment = BitManipulationAssignment()
# print(bitassignment.getithbit(70,3))
# print(bitassignment.setithbit(70,3))
# print(bitassignment.clearithbit(70,3))


class BitManipulationAssignment2:
    
    def ithbit(self,num,i):
        if num !=0 and (num & (1<<(i-1)) == 0):
            return 0
        return 1
    
    def setith(self,num,i):
        return (num | (1<<(i-1)))
    
    def clearith(self,num,i):
        return (num & ~(1<<(i-1)))
    
    
# assignment2 = BitManipulationAssignment2()
# print(assignment2.ithbit(8,1))
# print(assignment2.setith(8,1))
# print(assignment2.clearith(8,1))


def hackerrank_assignment(arr,l,h):
    if len(arr)==0:
        return 0
    if arr[0] != arr[1]:
        return arr[0]
    if arr[len(arr)-1] != arr[len(arr)-2]:
        return arr[len(arr)-1]
    mid = int(l+(h-l)/2)
    if l==h:
        return arr[l]
    if mid%2==0:
        if arr[mid] == arr[mid+1]:
            return hackerrank_assignment(arr,mid+2,h)
        else:
            return hackerrank_assignment(arr,l,h)
    else:
        if arr[mid] == arr[mid-1]:
            return hackerrank_assignment(arr,mid+1,h)
        else:
            return hackerrank_assignment(arr,l,mid-1)
           
            
                        
        
    
# arr = [1,1,3,3, 4, 5, 5, 7, 7, 8, 8 ]
# # print(hackerrank_assignment(len(arr),arr))
# print(hackerrank_assignment(arr,0,len(arr)-1))

    
def duplicateelement(arr):
    # for i in range(0,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if arr[i] == 0 and arr[j] != 0:
    #             arr[i],arr[j] = arr[j],arr[i]

    # return arr
    # l=0
    # r=len(arr)-1
    # while(l<r):
    #     if arr[l] == 0 and arr[r] != 0:
    #         arr[l],arr[r] = arr[r],arr[l]
    #         l+=1
    #         r-=1
    #     else:
    #         l+=1
        
    # return arr
    # j=0
    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         arr[j],arr[i] = arr[i],arr[j]
    #         j+=1
    # print(arr) 
    
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    print(count)      
    while count < len(arr):
        arr[count] = 0
        count+=1
    return arr

        
        

                
            
            
        
    
arr=[1,2,0, 0, 3, 4]
# print(hackerrank_assignment(len(arr),arr))
# print(duplicateelement(arr))
print(duplicateelement(arr))


    


    
        
