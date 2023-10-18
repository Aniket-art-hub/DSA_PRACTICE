class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
        maximum_weight=0
        for item in arr:
            if item.weight<=W:
                W -= item.weight
                maximum_weight+=item.value
            else:
                # maximum_weight +=  (item.value // item.weight)*W
                maximum_weight += item.value * W / item.weight
                break
                
        return maximum_weight