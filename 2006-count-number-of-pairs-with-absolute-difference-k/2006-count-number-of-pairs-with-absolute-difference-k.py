class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        result = 0
        for i in count:
            if i + k in count:
                result+= (count[i] * count[i+k])
        #print(count)        
        return result