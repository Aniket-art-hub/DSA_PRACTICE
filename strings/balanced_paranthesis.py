import math
class BalanceParanthesis:
    def swap_to_balance(self,s1):
        bracket_stack =[]
        for i in range(len(s1)):
            if bracket_stack and s1[i]==']' and bracket_stack[-1]=='[':
                bracket_stack.pop()
            else:
                bracket_stack.append(s1[i])
        print(bracket_stack)
        if bracket_stack:
            return len(bracket_stack)//2
        else:
            return 0
        
    def swap_balanced(self,s):
        open=0
        close=0
        n=len(s)
        for i in range(n):
            if s[i]=='[':
                open+=1
            elif s[i]==']':
                if open>0:
                    open-=1
                else:
                    close+=1
            else:
                return -1
        pairs = open/2.0
        return math.ceil(pairs/2.0)
        
        
BalanceParanthesis=BalanceParanthesis()
s1="[[][]]"
print(BalanceParanthesis.swap_to_balance(s1))


class CheckBalanceOrNot:
    def check_balance(self,s):
        stack=[]
        for i in range(len(s)):
            if stack:
                last_paran = stack[-1]
                if last_paran=='{' and s[i]=="}":
                    stack.pop()
                elif last_paran=='[' and s[i]=="]":
                    stack.pop()
                elif last_paran=='(' and s[i]==")":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            # print(stack)
        if len(stack)>0:
            return "NO"
        else:
            return "YES"