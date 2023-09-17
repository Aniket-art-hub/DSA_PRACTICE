def category(n,arr):
    arr.sort()
    count = 1
    total_category_sum = arr[0]
    for i in range(1,n):
        # print(arr[i])
        # print("uuuu")
        print(total_category_sum)
        if arr[i] > total_category_sum:
            count+=1
            total_category_sum += arr[i]
    return count


# arr=[14, 5, 9, 7, 2, 4]
# print(category(len(arr),arr))

def maximize(n,arr):
    arr.sort()
    l=0
    r=n-1
    num2 = []
    while l<r:
        product = arr[l]*arr[r]
        num2.append(product)
        l+=1
        r-=1
    print(num2)
    return max(num2)

   
    
arr=[-12, 17, -13, 17]
print(maximize(len(arr),arr))
    