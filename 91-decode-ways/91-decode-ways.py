class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0: return 0
        n = len(s)+1
        dp = [0]*n
        dp[0]= 1 #edge cases like -ve or 0
        dp[1]= 1 #number of ways to decode singe digit is 1
        for i in range(2,n):
            onedigit = int(s[i-1:i])
            twodigit = int(s[i-2:i])
            if 0< onedigit < 10:
                dp[i] += dp[i-1]
            if 9 < twodigit <27:
                dp[i] += dp[i-2]
        return dp[n-1]