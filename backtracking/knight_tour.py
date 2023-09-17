###############  O(8^N^2)  ################ O(n^2) ##############################
class KnightTour:
    xmove = [2,2,1,-1,1,-1,-2,-2]
    ymove = [1,-1,-1,-1,2,-1,1,2]
        
    def knight_tour(self,n):
        board = [[-1 for i in range(n)] for i in range(n)]
        move  = 0
        board[0][0] = move
        x = 0
        y = 0
        if not self.traverse(x,y,move+1,n,board):
            return "solution not exist"
        else:
            for i in range(n):
                for j in range(n):
                    print(board[i][j] ,end=" ")
                print()
        
    def traverse(self,x,y,move,n,board):
        if move == n*n:
            return True
        for i in range(8):
            next_x = x+KnightTour.xmove[i]
            next_y = y+KnightTour.ymove[i]
            if self.isSafe(next_x,next_y,n,board):
                board[next_x][next_y] = move
                if(self.traverse(next_x,next_y,move+1,n,board)):
                    return True
                else:
                    board[next_x][next_y] = -1
        return False
            
    def isSafe(self,x,y,n,board):
        if (x>=0 and x<n and y>=0 and y<n and board[x][y]==-1):
            return True
        else:
            return False
    
KnightTour_obj = KnightTour()
print(KnightTour_obj.knight_tour(5))