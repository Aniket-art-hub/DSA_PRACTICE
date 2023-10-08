##################### steps 2^n-1 and time O(2^n) and space is O(n) ##############################

class TowerOfHanoi:
    def tower_of_hanoi(cls,n):
        source = "A"
        destination = "C"
        spare = "B"
        cls.backtrack(n,source,destination,spare)
        
        
    def backtrack(cls,n,source,destination,spare):
        if n==1:
            print("Move disk "+ str(n) + "from " + source + "to" + destination)
            return
        cls.backtrack(n-1,source,spare,destination)
        print("Move disk "+ str(n) + "from " + source + "to" + destination)
        cls.backtrack(n-1,spare,destination,source)
        
tower_obj = TowerOfHanoi()
print(tower_obj.tower_of_hanoi(2))


class Solution:
    
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N==1:
            print("move disk " + str(N) + " from rod " +  str(fromm) + " to rod " +  str(to))
            return 1
        count = 0
        count += self.toh(N-1,fromm,aux,to)
        print("move disk " + str(N) + " from rod " +  str(fromm) + " to rod " +  str(to))
        count += 1
        count += self.toh(N-1,aux,to,fromm)
        return count