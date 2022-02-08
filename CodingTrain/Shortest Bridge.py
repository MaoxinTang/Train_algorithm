class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def paint(grid,i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return 
            if grid[i][j]==1:
                grid[i][j] = 2
                paint(grid,i-1,j)
                paint(grid,i+1,j)
                paint(grid,i,j-1)
                paint(grid,i,j+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    paint(grid,i,j)
                    break 
            else:
                continue 
            break 
        
        # print(grid)
        def expand(grid,i,j,n):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return   
            if grid[i][j]==0:
                grid[i][j] = n+1
            return grid[i][j]==1
        
        n = 2
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==n and (expand(grid,i-1,j,n) or expand(grid,i+1,j,n) or expand(grid,i,j+1,n) or\
                                          expand(grid,i,j-1,n)):
                        return n-2
            n += 1