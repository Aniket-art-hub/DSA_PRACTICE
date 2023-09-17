############### time complexity is O(n!)     and space complexity is O(N^2) #######################################

class Nqueen:
    def n_queen(self,n):
        board = [['.' for i in range(n)] for i in range(n)]
        
        self.traverse_all(board,0,n)
        
    def traverse_all(self,board,col,n):
        if col == n:
            self.print_board(board,n)
            return
        for row in range(n):
            if self.isSafe(board,row,col,n):
                board[row][col] = 'Q'
                self.traverse_all(board,col+1,n)
                board[row][col] = '.'
            
            
            
    def isSafe(self,board,row,col,n):
        #left all same row
        dupcol = col
        while dupcol >=0:
            if board[row][dupcol] == 'Q':
                return False
            dupcol-=1
        
        #upper diagonal
        dupcol = col
        duprow = row
        while dupcol >=0 and duprow >=0:
            if board[duprow][dupcol] == 'Q':
                return False
            dupcol -=1
            duprow -=1
            
        #lower diagonal
        
        dupcol = col
        duprow = row
        while dupcol>=0 and duprow<n:
            if board[duprow][dupcol] == 'Q':
                return False
            dupcol -=1
            duprow +=1 
            
        return True       
    
    def print_board(self,board,n):
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=' ')
            print()
        print("--------------------")
       
        
        
        
Nqueen_obj = Nqueen()
print(Nqueen_obj.n_queen(5))