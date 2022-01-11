class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentmax = totalmax = currentmin = nums[0]
        for i in range(1,len(nums)):
                tempmax = max(currentmax*nums[i],max(nums[i],currentmin*nums[i]))
                currentmin = min(currentmin*nums[i],nums[i],currentmax*nums[i])
                currentmax = tempmax
                
                totalmax = max(totalmax,currentmax)
        return totalmax
        