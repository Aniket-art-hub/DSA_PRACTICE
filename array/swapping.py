# by using third variable

class Swapping:
    def swap_using_third_variable(self,a,b):
        c = a
        a = b
        b = c
        return "a = " + str(a) + "and b = " + str(b)
    
    def swap_without_third_variable(self,a,b):
        # a,b = b,a
        a = a + b
        b = a - b
        a = a - b
        return "a = " + str(a) + "and b = " + str(b)
    

swap_obj = Swapping()
print(swap_obj.swap_using_third_variable(4,8))

print(swap_obj.swap_without_third_variable(24,78))
        