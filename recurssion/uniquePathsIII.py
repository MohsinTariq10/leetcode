class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        non_obstacle = 0
        self.win = 0
        start_row, start_col = 0, 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] >= 0:
                    non_obstacle += 1

                if grid[i][j] == 1:
                    start_row, start_col = i, j
                
        self.recur(grid, start_row, start_col, non_obstacle)
        return self.win
    
    def recur(self, grid, i, j, non_obstacle):
        if i >= self.m or j >= self.n or i< 0 or j <0:
            return 0
    
        val = grid[i][j]
        
        if val < 0 : return 0
        if  val == 2 and non_obstacle == 1:
            self.win +=1
            return 0
        
        non_obstacle -=1
        grid[i][j] = -2
        
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.recur(grid, i + x, j + y, non_obstacle )
        
        grid[i][j] = val
        