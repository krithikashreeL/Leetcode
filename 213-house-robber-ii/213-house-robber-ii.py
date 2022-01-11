class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) <= 3: return max(nums)
   
        
        
        def helper(nums):
            n = len(nums)+1
            dp =[0]*n
            dp[0]=0
            dp[1]=nums[0]
            for i in range(1,n-1):
                dp[i+1] = max(dp[i-1]+nums[i],dp[i])
            return dp[n-1]
    
        return max(helper(nums[1:]),helper(nums[:-1]))