class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Hset = set()
        right_pointer = left_pointer = count = 0
        while right_pointer < len(s):
            if s[right_pointer] not in Hset:
                Hset.add(s[right_pointer])
                count = max(len(Hset),count)
                right_pointer +=1
            else :
                Hset.remove(s[left_pointer])
                left_pointer +=1
        
        return count
        