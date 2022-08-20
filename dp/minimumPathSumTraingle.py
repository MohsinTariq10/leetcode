def minimumPathSum(triangle, n):
    # Write your code here.
    dp = [[-1]*n for x in range(n)]
    return recur(triangle, 0, 0, dp)

def recur(arr, i, j, dp):
    if i == len(arr)-1:
        return arr[i][j]
    if dp[i][j] == -1:
        down = arr[i][j] + recur(arr, i+1 ,j, dp)
        diag = arr[i][j] + recur(arr, i+1, j+1, dp)
        dp[i][j] = min(down, diag)
        
    return dp[i][j]

def minimumPathSum(triangle, n):
    # Write your code here.
    dp = [-1]*n
    for i in range(n):
        dp[i] = triangle[n-1][i]
    
    i = n-2
    while(i > -1):
        j = i
        temp = [-1]*n
        while(j > -1):
            diag = triangle[i][j] + dp[j]
            down = triangle[i][j] + dp[j+1]
            temp[j] = min(diag, down)
            j-=1
        dp = temp[:]
        i -=1
    return dp[0]