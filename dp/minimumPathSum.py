import sys
sys.setrecursionlimit(10**7)

def minSumPath(grid):
    # Write your code here.
    m, n = len(grid), len(grid[0])
    dp = [[-1]*n for x in range(m)]
    return recur(grid, 0, 0, dp)
    
def recur(grid, i, j, dp):
    if i >= len(grid) or j >= len(grid[0]):
        return sys.maxsize
    if i == len(grid)-1 and j == len(grid[0])-1:
        return grid[i][j]
    if dp[i][j] == -1:
        down = grid[i][j] + recur(grid, i+1, j, dp)
        right = grid[i][j] + recur(grid, i, j+1, dp)
        dp[i][j] = min(down, right)
    return dp[i][j]

    

# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1