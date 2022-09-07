class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i in range(len(s)):
            if s[i] != '#':
                stack_s.append(s[i])
            else:
                if len(stack_s) > 0:
                    stack_s.pop()
                
        for i in range(len(t)):      
            if t[i] != '#' :
                stack_t.append(t[i])               
            else:
                if len(stack_t) > 0:
                    stack_t.pop()
                
         
        # print(stack_s,stack_t)
        if "".join(stack_s) == "".join(stack_t): return True
        return False