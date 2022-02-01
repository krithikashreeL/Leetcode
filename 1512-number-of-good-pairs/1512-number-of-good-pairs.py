class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}
        count = 0
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                count += dict[i]
                dict[i] +=1
        #print(dict)
        return count
        