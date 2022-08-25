class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        seen = 0
        
        for i in range(len(nums)):
            if total - seen - nums[i] == seen:
                return i
            seen += nums[i]
            
        return -1