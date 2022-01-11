class Solution:
    def jump(self, nums: List[int]) -> int:
#         currentmax = count = position = 0
#         n = len(nums)
#         for i in range(0,n-1):
#             if(i + nums[i] > currentmax):
#                 currentmax = i + nums[i]
#                 print(currentmax)
#             if(position == i):
#                 count+=1
#                 position = currentmax
#                 print(position,count)
#         return count
        
        if nums[0] == 0:
            return 0
        left=right=0
        count = 0
        while right<len(nums)-1:
            maxreach = 0
            for i in range(left,right+1):
                maxreach = max(maxreach, nums[i]+i)
            left= right+1
            right = maxreach
            count+=1
        return count