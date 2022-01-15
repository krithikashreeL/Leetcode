class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [0]*(n+1)
        count = 0
        for i in range (2,n):
            if(nums[i]-nums[i-1] == nums[i-1]-nums[i-2]):
                dp[i]  += 1+dp[i-1]
                count += dp[i]
                
        return count
        