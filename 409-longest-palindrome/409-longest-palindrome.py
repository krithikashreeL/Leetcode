class Solution:
    def longestPalindrome(self, s: str) -> int:
        # collections.counter - converts s to a dict eg ['a','a','b'] =>{a:2,b:1} 
        
        hashmap = collections.Counter(s)
        result = 0
        
        for i in hashmap.items():
            result += i[1]// 2*2
            if result %2 == 0 and i[1] %2 == 1:
                result+=1
            
        return result
    