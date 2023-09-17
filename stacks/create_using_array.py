from tkinter import ARC


class ArrayStacks:
    array_count = -1
    array = []

    def stack_using_array(self,num):
        ArrayStacks.array.append(num)
        ArrayStacks.array_count+=1
        return True
    
    def pop_stack(self):
        top =  ArrayStacks.arr[ArrayStacks.array_count]
        ArrayStacks.array_count-=1
        return top
    
    def top(self):
        return ArrayStacks.arr[ArrayStacks.array_count]
    
    def isEmpty(self):
        return ArrayStacks.array_count == -1.

    


array_stacks = ArrayStacks()
num = 2
print(array_stacks.stack_using_array(num))

