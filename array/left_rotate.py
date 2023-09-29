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