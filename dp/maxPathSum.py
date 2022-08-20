from sys import stdin, setrecursionlimit, maxsize
setrecursionlimit(10**7)

def getMaxPathSum(matrix):
    maxi = -maxsize
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1]*n for x in range(m)]
    
    for i in range(n):
        maxi = max(maxi, recur(matrix, 0, i, dp))
    return maxi

def recur(matrix, i, j, dp):
    if j < 0 or j > len(matrix[0])-1: return -maxsize
    val = matrix[i][j]
    
    if i == len(matrix)-1: return val
    if dp[i][j] == -1:
        down= val + recur(matrix, i+1, j, dp)
        downr = val + recur(matrix, i+1, j+1, dp)
        downl = val + recur(matrix, i+1, j-1, dp)
        dp[i][j] = max(down, downr, downl)
    return dp[i][j]

from sys import stdin, setrecursionlimit, maxsize
setrecursionlimit(10**7)

def getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [-1]*n
    for i in range(n):
        dp[i] = matrix[m-1][i]
    
    i = m-2
    while(i > -1):
        j = n-1
        temp = [-1] * n
        while(j > -1):
            val = matrix[i][j]
            downl, downr = -maxsize, -maxsize
            down = val + dp[j]
            if j+1 < n: 
                downl = val + dp[j+1]
            if j-1 > -1:
                downr = val + dp[j-1]
            temp[j] = max(down, downr, downl)
            j-=1
        dp = temp[:]
        i-=1
    return max(dp) 
    















