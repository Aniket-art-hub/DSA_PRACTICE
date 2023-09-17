
# time complexity is O(n)
class Fibonacci:
    def get_fibonacci_at_position(self,n):
        x = 0
        y= 1
        for i in range(2,n):
            c = x+y
            x = y
            y = c
        return c 
    
    def get_all_fibonacci(self,n):
        x = 0
        y= 1
        series = [x,y]
        for i in range(2,n+1):
            c = x+y
            x = y
            y = c
            series.append(c)

        return series
    
    
fib = Fibonacci()
print(fib.get_fibonacci_at_position(6))
print(fib.get_all_fibonacci(6))