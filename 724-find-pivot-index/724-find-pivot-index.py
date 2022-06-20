class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        seen_sum = 0
        
        # concept here is subtract sum upto that point to total see if rreminder = seen sum meaning left sum = right sum so thats our index
        
        
        
        for i in range(len(nums)):
            if total_sum - seen_sum - nums[i] == seen_sum:
                return i
            seen_sum += nums[i]
        
        return -1
        