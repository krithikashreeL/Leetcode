class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        count = 0
        for i in jewels:
            dict[i] = i
        
        for i in stones:
            if i in dict:
                count+=1
            else:
                continue
        return count