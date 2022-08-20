def subsetSumToK(n, k, arr):
    dp = [[-1]*(k+1) for x in range(n)]
    return recur(n-1, k, arr, dp)

def recur(n, k, arr, dp):
    if k == 0: return True
    if n == 0: return arr[n] == k
    if dp[n][k] == -1:
        not_take = recur(n-1, k, arr, dp)
        take = False
        if k >= arr[n]:
            take  = recur(n-1, k-arr[n], arr, dp)
        dp[n][k] = not_take or take
    return dp[n][k]

def subsetSumToK(n, k, arr):
    dp = [[False]*(k+1) for x in range(n)]
    for i in range(n): dp[i][0] = True

    if arr[0] == k: dp[0][arr[0]] = True

    for i in range(1, n):
        for j in range(1, k+1):
            not_take = dp[i-1][j]
            take = False
            if k >= arr[i]:
                take  = dp[i-1][j-arr[i]]
            dp[i][j] = not_take or take
    return dp[n-1][k]
    
    

