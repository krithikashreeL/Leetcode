class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if (s[i] == '(') or (s[i] == '{') or (s[i] =='['):
                stack.append(s[i])
                # print(stack)
            elif s[i] == ')':
                    if  len(stack) == 0 or stack[-1] != '(':
                        return False
                    else:
                        top = stack.pop()
            elif s[i] == '}':
                    if len(stack) == 0 or stack[-1] != '{' :
                        return False
                    else:
                        top = stack.pop()
            elif s[i] == ']':
                    if  len(stack) == 0 or stack[-1] != '[':
                        return False
                    else:
                        top = stack.pop()
        if len(stack) == 0:return True
        return False