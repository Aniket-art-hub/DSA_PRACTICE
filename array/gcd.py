import math
class Gcd:
    # time complexity O(min(a,b))
    def get_gcd(self,a,b):
        x = min(a,b)
        while x>0:
            if a%x==0 and b%x==0:
                break
            x-=1
        return x
    
    # time complexity O(sqrt(min(a,b)))
    def get_gcd_2(self,a,b):
        x = math.floor(math.sqrt(min(a,b)))
        while x>0:
            if a%x==0 and b%x==0:
                break
            x-=1
        return x
    
    #by euclidean approach(preferred) O(log(min(a,b)))
    
    def get_gcd_3(self,a, b):
        
        while a>0 and b>0:
            if a > b:
                a = a%b
            else:
                b = b%a
                
        if a ==0:
            return b
        else:
            return a
            
   
gcd_obj = Gcd()
print(gcd_obj.get_gcd(28,56))
print(gcd_obj.get_gcd_2(28,54))
print(gcd_obj.get_gcd_3(28,54))


        
        
            