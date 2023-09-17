################## O(2^n) and space O(n) ###################################
class Paranthesis:
    result = []
    def generate_paranthesis(self,n):
        paranthesis = ""
        self.traverse(paranthesis,n,diff=0)
        return Paranthesis.result
        # for i in range(len(Paranthesis.result)):
        #     print(i)
        
    def traverse(cls,paranthesis,n,diff):
        if (len(paranthesis)==2*n and diff==0):
            Paranthesis.result.append(paranthesis)
        if (len(paranthesis)==2*n or diff<0 or diff>n):
            return
        cls.traverse(paranthesis+'(',n,diff+1)
        cls.traverse(paranthesis+')',n,diff-1)

        
Paranthesis_obj = Paranthesis()
print(Paranthesis_obj.generate_paranthesis(4))
        