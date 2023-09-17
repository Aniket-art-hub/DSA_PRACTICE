def stock_problem(arr): ### APPROACH 1 NAIVE APPROACH  O(n^2)
    n = len(arr)
    stock_value =[]
    for i in range(n):
        count=1
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                count+=1
            else:
                break
        stock_value.append(count)
                
    return stock_value          
        
        
#################3 APPROACH 2 BY USING STACK OPTIMIZE WAY  O(n) both tiem and space #######################
def stock_problem_using_stack(arr):
    n = len(arr)
    stack_stock = []
    stock_increase_consistence=[]
    for i in range(n):
        while stack_stock and arr[stack_stock[-1]]<=arr[i]:
            stack_stock.pop()
        stock_increase_consistence.append(i-stack_stock[-1]) if stack_stock else stock_increase_consistence.append(i+1)
        stack_stock.append(i)
    return stock_increase_consistence




        
arr=[100,80,70,60,75,60,85]  
print(stock_problem_using_stack(arr))