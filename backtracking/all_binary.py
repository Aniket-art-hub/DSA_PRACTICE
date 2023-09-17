############ time complexity is 2^n and space complexity is O(N)
class Binary:
    def all_binary(self,n):
        current_string = ""
        result = []
        self.backtrack(n,current_string,result)
        return result
        
    def backtrack(self,n,current_string,result):
        if len(current_string) == n:
            result.append(current_string)
            return
        self.backtrack(n,current_string+"0",result)
        self.backtrack(n,current_string+"1",result)
    
binary_obj = Binary()
print(binary_obj.all_binary(5))
    