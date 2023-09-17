import math
class PrimeNumber:
    # Approach 1 time complexity is O(n)
    def check_prime(self,n):
        for i in range(2,n):
            if n % i==0:
                return False
        return True
    
    # Approach2 time complexity O(sqrt(n))
    def check_prime_number(self,n):
        i =2
        for i in range(i*i,n):
            if n %i == 0:
                return False
        return True
    
    
    #find all prime number from 1 to n
    def get_all_prime(self,n):
        all_prime = []
        for i  in range(2,n+1):
            is_prime = self.check_prime_or_not(i)
            if is_prime:
                all_prime.append(i)
        return all_prime
    
    def check_prime_or_not(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
                
    # by using sieve of eratosthenes
    def all_prime_by_sieve_eratosthenes(self,n):
        is_prime = []
        count = 0
        for i in range(2,int(math.sqrt(n))+1):
            j = i+i
            if len(is_prime[i]) and  is_prime[i]== True:
                while j<=n:
                    is_prime[j] = False
                    j = j+i
        
        count = 0
        for i in range(2,n+1):
            if is_prime[i] == True:
                count+=1
        return count 
           
    
    
    
    
PrimeNumber_obj = PrimeNumber()
print(PrimeNumber_obj.check_prime(7))
print(PrimeNumber_obj.check_prime_number(5))
print(PrimeNumber_obj.get_all_prime(11))
print(PrimeNumber_obj.all_prime_by_sieve_eratosthenes(11))


        
    