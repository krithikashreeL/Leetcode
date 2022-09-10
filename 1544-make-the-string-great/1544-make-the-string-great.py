class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for i in range(len(s)):
            if len(stack) > 0 and s[i].lower() == stack[-1].lower() and (s[i].islower() == stack[-1].isupper() or s[i].islower() == stack[-1].isupper()):
                stack.pop()
            else:
                stack.append(s[i])
                
        # print(stack)
        return "".join(stack)
        

                