class Solution:
    def solveSudoku(self, board):
        n = 9
        self.sudoku_backtrack(board,n)

    def sudoku_backtrack(self,board,n):
        row = -1
        col = -1
        isempty = False
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    isempty = True
                    row=i
                    col=j
            if isempty:
                break
        if not isempty:
            return True
        num = ['1','2','3','4','5','6','7','8','9']
        for value in num:
            if self.is_safe(board,row,col,n,value):
                board[row][col] = value
                if self.sudoku_backtrack(board,n):
                    return True
                board[row][col]= "."
            return False
        return True

    def is_safe(self,board,row,col,n,value):
        min_row = row-(row%3)
        max_row = min_row+(3-1)
        min_col = col-(col%3)
        max_col = min_col+(3-1)
        for row in range(min_row,max_row):
            for column in range(min_col,max_col):
                if board[row][column] == value:
                    return False

        for i in range(n):
            if board[row][i] == value:
                return False
        for i in range(n):
            if board[col][i] == value:
                return False
        return True     