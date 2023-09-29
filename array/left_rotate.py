class LeftRotate:
    
    ########## APPROACVH 1 BY COMPLEXITY O(N) AND SPACE O(N)
    def left_rotate(self,arr,d):
        n = len(arr)
        if n==0:
            return None
        result=[]
        for i in range(d,n):
            result.append(arr[i])
        for j in range(d):
            result.append(arr[j])
        return result
    
    ### Approach 2
    def left_rotate(self,arr,d):
        n=len(arr)
        if n==0:
            return None
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
        return arr

    def reverse(self,arr,start,end):
        while start<end:
            # arr[start],arr[end] = arr[end],arr[start]
            arr[start] = arr[start]+arr[end]
            arr[end] = arr[start]-arr[end]
            arr[start]=arr[start]-arr[end]
            start+=1
            end-=1