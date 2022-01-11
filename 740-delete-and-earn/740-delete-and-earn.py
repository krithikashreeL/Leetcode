class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
       #similar to houserober 
        n= len(nums)
        if n == 0: return 0
        freq = [0]* (max(nums)+1)
        for i in nums:
            freq[i]+=1
        
        dp = [0]*len(freq)
        dp[1] = freq[1]
        for i in range(2,len(freq)):
            dp[i] = max(dp[i-2]+(freq[i]*i),dp[i-1])
        return dp[len(freq)-1]
            
        
    
    