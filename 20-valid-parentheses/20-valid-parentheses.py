class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0 : return True
        for ch in s:
            if ch == '{' or ch =='(' or ch =='[':
                stack.append(ch)
            elif ch =='}' and len(stack) >0 and stack[-1] == '{':
                stack.pop()
            elif ch ==')'and len(stack) >0 and stack[-1] == '(':
                stack.pop()
            elif ch ==']' and len(stack) >0 and stack[-1] == '[':
                stack.pop()
            else : return False
        
        
        
                
        if len(stack) >0 : return False
        return True
    
                
            
                
        