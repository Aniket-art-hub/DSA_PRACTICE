def celebrity_problem(matrix,n):
    stack = []
    for i in range(n):
        stack.append(i)
    
    while len(stack)>=2:
        first_element = stack.pop()
        second_element = stack.pop()
        if matrix[first_element][second_element]==1 and matrix[second_element][first_element]==1:
            pass
        elif matrix[first_element][second_element]==0 and matrix[first_element][second_element]==0:
            pass
        elif matrix[first_element][second_element]==1:
            stack.append(second_element)
        elif matrix[second_element][first_element]==1:
            stack.append(first_element)
        
    if stack:
        celeb = stack.pop()
        for col in range(n):
            if matrix[celeb][col]==1:
                return -1
        for row in range(n):
            if row!=celeb and matrix[row][celeb]==0:
                return -1
        return celeb
    return -1
                
        
            
        
            