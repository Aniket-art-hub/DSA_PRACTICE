class sum_power:

    def power_nth_natural_sum(cls,n,k):
        result = []
        return cls.get_sum_power(n,k,1,result)
    
    def get_sum_power(cls,n,k,temp,result):
        if n==0:
            print(result)
            return 1
        if n <0 or temp>n:
            return 0
        
        ## ignore not accept
        cls.get_sum_power(n,k,temp+1,result)
        ## accept
        result.append(n-pow(temp,k))
        cls.get_sum_power(n-pow(temp,k),k,temp+1,result)
        # return a+b
        

sum_power = sum_power()
n=10
k=2
print(sum_power.power_nth_natural_sum(n,k))