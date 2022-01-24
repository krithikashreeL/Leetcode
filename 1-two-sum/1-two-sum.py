class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}
        for i in range (0,len(nums)):
            diff = target - nums[i]
            if diff in Hmap:
                return [Hmap[diff],i]
            else:
                Hmap[nums[i]] = i
        #return result
            
        