from tkinter import NO, YES


class ValidParanthesis:
    def check_valid_paranthesis(self,s):
        stack = []
        for i in range(len(s)):
            if stack and self.check_paranthesis_pair(stack[-1],s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        return self.isempty(stack)



    def check_paranthesis_pair(self,openpair,closepair):
        return (openpair=='(' and closepair==')') or (openpair=='{' and closepair=='}') or (openpair=='[' and closepair==']')


    def isempty(self,stack):
        if stack:
            return 'NO'
        else:
            return 'YES'

