class StringProblem:
    #approach 1 Brute force O(n)
    def reverse_string(self,string):
        temp_string = ""
        result = ""
        for i in range(len(string)):
            if string[i]==" ":
                reverseString = temp_string
                result =  reverseString + " " + result
                temp_string = ""
            else:
                temp_string += string[i]
        result = temp_string + " " + result
        return result
    
    #approach 2 using stack
    def reverse_using_stack(self,string):
        string_stack = []
        temp_string = ""
        reverse_result=""
        for i in range(len(string)):
            if string[i]==" ":
                string_stack.append(temp_string)
                temp_string = ""
            else:
                temp_string += string[i]
        if temp_string:
            string_stack.append(temp_string)
        while len(string_stack)>0:
            reverse_result =  reverse_result + " " + string_stack.pop()
        return reverse_result
    
    def reverseString(n, arr):
        # Write your code here
        reverse_string=""
        n = len(arr)
        for i in range(n):
            reverse_string = arr[i]+" "+reverse_string
        return reverse_string

    def reverseString_twopinter(self,arr):
        # Write your code here
        n = len(arr)
        point1=0
        point2=n-1
        while point1<point2:
            arr[point1],arr[point2] = arr[point2],arr[point1]
            point1+=1
            point2-=1
        return arr
    
    def remove_dublicate(self,string):
        hash_data = {}
        result_string = ""
        n = len(string)
        for i in range(n):
            if string[i] not in hash_data:
                hash_data[string[i]]=1
        for key,data in hash_data.items():
            result_string += key
        return result_string
    
    def remove_dublicate_using_stack(self,s):
        stack_data = []
        result_string = ""
        n = len(s)
        for i in range(n):
            if stack_data and stack_data[-1] != s[i]:
                stack_data.append(s[i])
            elif not stack_data:
                stack_data.append(s[i]) 
        while len(stack_data)>0:
            result_string = stack_data[-1] + result_string
            stack_data.pop()
        return result_string
            
        
                           
    
    
    
StringProblem = StringProblem()
string = "this is a DSA course"
# print(StringProblem.reverse_using_stack(string))
arr = ['h','e','l','l','o']
# print(StringProblem.reverseString(arr))
# print(StringProblem.reverseString_twopinter(arr))
string = "abbbcccdefg"
# print(StringProblem.remove_dublicate(string))
print(StringProblem.remove_dublicate_using_stack(string))

        