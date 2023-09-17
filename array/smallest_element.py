class Smallest:
    def smallest_element(self,arr):
        n=len(arr)
        if n !=0 and n>2:
            arr.sort()
            first_smallest = arr[0]
            second_smallest = ''
            for i in range(1,len(arr)):
                if arr[i] != arr[i-1]:
                    second_smallest = arr[i]
                    break
            if first_smallest and second_smallest:
                return first_smallest,second_smallest
            else:
                return -1
        else:
            return -1
        
    def smallest_element_app2(self,arr):
        import sys
        n=len(arr)
        if n !=0 and n>2:
            first_smallest = sys.maxsize
            second_smallest = sys.maxsize
            for i in range(n):
                if arr[i] < first_smallest:
                    first_smallest = arr[i]
            for i in range(n):
                if arr[i] < second_smallest and arr[i]>first_smallest:
                    second_smallest = arr[i]
            return first_smallest,second_smallest
        else:
            return -1
        
        
smallest = Smallest()
arr=[2,4,3,5,6]
print(smallest.smallest_element_app2(arr))
            