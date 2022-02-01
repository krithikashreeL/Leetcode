class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        dict = {}
        result = []
        for i in range (0,len(sorted_arr)):
            if sorted_arr[i] not in dict:
                dict[sorted_arr[i]] = i
                
        for i in range(len(nums)):
            result.append(dict[nums[i]])
            
        return result
        
    
        