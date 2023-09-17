def get_factorial(n):
    if n<=1:
        return 1
    else:
        return n*get_factorial(n-1)
#############################################     find nth row 2nd element of pascal trianle   ###############################################
def getpascaltraianle_element(n,r):
    n_factorial = get_factorial(n)
    r_factorial = get_factorial(r)
    n_r_factorial = get_factorial((n-r))
    result = n_factorial/(r_factorial*(n_r_factorial))
    return result


n = 5
# print(getpascaltraianle_element(n,2))

#############################################  find all nth row pascal triangle time O(n^2) space O(n^2) ###########################################
def all_nth_pascal(n):
    arr = [[0 for i in range(n)]
           for i in range(n)]
    for i in range(n):
        for j in range(0,i+1):
            if j==0 or j ==i:
                arr[i][j] = 1
                print(arr[i][j],end=" ")
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
                print(arr[i][j],end=" ")

        print("\n",end="")

# print(all_nth_pascal(5))

#O(n^2)  space O(1)
def approach2_pascal(n):
    for line in range(1, n + 1):
        c = 1; # used to represent C(line, i)
        for i in range(1, line + 1):
             
            # The first value in a
            # line is always 1
            print(c, end = " ")
            c = int(c * (line - i) / i)
        print("")
        
# print(approach2_pascal(5))


#O(n^1)  space O(1)
def nth_row_pascal(n):
        c = 1
        result = []
        for i in range(1, n + 1):
            result.append(c)
            c = int(c * (n - i) / i)
        return result
        
# print(nth_row_pascal(5))
