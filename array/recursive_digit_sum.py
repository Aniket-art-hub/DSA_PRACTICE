class recursive:
    def recursive_digit_sum(self,n,k):
        if len(str(n)) ==0:
            return 0
        if k > 1:
            n = n*k
        if len(str(n))==1:
            return n

        sum = 0
        for i in str(n):
            sum += int(i)
        return self.recursive_digit_sum(str(sum),k=0)
            
recursive = recursive()
n=9875
print(recursive.recursive_digit_sum(n,3))