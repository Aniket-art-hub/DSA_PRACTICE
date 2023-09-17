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