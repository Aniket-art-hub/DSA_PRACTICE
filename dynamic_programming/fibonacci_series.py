class Solution:
    
    ## recursive call
    def fibrecursive(self,n):
        if n<=1:
            return n
        return self.fibrecursive(n-1)+self.fibrecursive(n-2)
    
    
    ## by memorisation technique
    def fib(self, n: int) -> int:
        array=[False]*(n+1)
        self.fibmemorisation(n,array)
        
        
    def fibmemorisation(self,n,array):
        if n<=1:
            return n
        if array[n] == False:
            array[n] =self.fibmemorisation(n-1,array) + self.fibmemorisation(n-2,array)
        return array[n]
        