class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = maxsum = nums[0]
        n = len(nums) 
        for i in range(1,n):
            currentsum = max(currentsum+nums[i],nums[i])
            print(currentsum)
            if(currentsum>maxsum):
                maxsum = currentsum
        return maxsum
            
        