class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        position = n-1
        i=n-1
        while i>=0:
            if(i+nums[i]>=position):
                position = i
            i-=1
        return position == 0
        
            
            
    
        