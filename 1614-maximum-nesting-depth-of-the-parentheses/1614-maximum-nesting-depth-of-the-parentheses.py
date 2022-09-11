class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                count = max(count,len(stack))
            elif s[i] == ")":
                stack.pop()
           
               
        
        return count