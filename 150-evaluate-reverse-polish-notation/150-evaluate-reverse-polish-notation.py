class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in (tokens):
            if token not in "+-*/":
                stack.append(int(token))
            else:               
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(first + second)
                
                if token == "-":
                    stack.append(second - first)
                
                if token == "*":
                    stack.append(second * first)
                
                if token == "/":
                    stack.append(int(second/first))
                 
            
            # return sum(stack)
    
        return sum(stack)
        