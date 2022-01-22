class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0 : return 0

        dp = [[1 for i in range(n)]for i in range(n)]
        #print(dp)
        #dp[0][0] = 1
        for i in range(1,n):
            for j in range(n-i):
                k = i+j
                if s[j] == s[k] and i ==1:
                    dp[j][k] = 2
                elif s[j] == s[k]:
                    dp[j][k] = dp[j+1][k-1]+2
                else:
                    dp[j][k] = max(dp[j+1][k],dp[j][k-1])
                
        #print(dp) 
       
        return dp[0][-1]