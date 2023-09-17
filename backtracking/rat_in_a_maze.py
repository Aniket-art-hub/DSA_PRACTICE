class RatInAMaze:
    rowmove = [-1,1,0,0]
    colmove = [0,0,1,-1]
    posmove = ['U','D','R','L']
    result=[]
    def rat_in_maze(self):
        maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
        n  = len(maze)
        m = len(maze[0])
        visited = self.markvisited(n,m)
        move = ''
        self.traverse(maze,n,0,0,move,visited)
        return RatInAMaze.result

        
    def markvisited(self,n,m):
        return  [[-1 for i in range(n)] for j in range(m)]
    
    
    def traverse(self,maze,n,row,col,move,visited):
    
        if (row == n-1) and (col == n-1):
            RatInAMaze.result.append(move)
            return
        
        for i in range(4):
            next_row = row+RatInAMaze.rowmove[i]
            next_col = col+RatInAMaze.colmove[i]
            if self.isSafe(next_row,next_col,maze,n,visited):
                visited[row][col] = 1
                if self.traverse(maze,n,next_row,next_col,move+RatInAMaze.posmove[i],visited):
                    return True
                else:
                    visited[row][col] = -1
            
    def isSafe(self,next_row,next_col,maze,n,visited):
        if next_row <n and next_col <n and next_row >=0 and next_col>=0  and maze[next_row][next_col] == 1 and visited[next_row][next_col] == -1:
            return True
        else:
            return False
        
    
RatInAMaze_obj = RatInAMaze()
print(RatInAMaze_obj.rat_in_maze())