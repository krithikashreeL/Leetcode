class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        stack = []
        ans = ''
        count = 0
        for i in s:
            if i =='(' :
                stack.append(i)
                count += 1
                if count > 1:
                    ans+= '('
            else:
                stack.pop()
                count -=1
                if count > 0:
                    ans+=')'
        return ans