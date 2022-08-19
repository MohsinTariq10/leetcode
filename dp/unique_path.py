class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for i in range(m)]
        return self.recur(m-1, n-1, dp)

    def recur(self,m, n, dp):
        if m<0 or n <0:
            return 0
        if m==0 and n == 0:
            return 1
        if dp[m][n] == -1:
            l = self.recur(m-1, n, dp)
            r = self.recur(m, n-1, dp)
            dp[m][n] = l+r
        return dp[m][n]