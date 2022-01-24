class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =  [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        
        return dp[m-1][n-1]