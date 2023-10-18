class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        paltform_needed=1
        max_platform = 1
        i=1
        j=0
        while i<len(arr) and j<len(dep):
            if arr[i] <= dep[j]:
                paltform_needed+=1
                max_platform = max(max_platform,paltform_needed)
                i+=1
            else:
                paltform_needed-=1
                j+=1
        return max_platform