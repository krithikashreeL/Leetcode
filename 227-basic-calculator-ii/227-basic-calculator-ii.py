class Solution:
    def calculate(self, s: str) -> int:
        s = list(s)
        stack = []
        current_number = 0
        current_operation = "+"
        for i in range(len(s)):
            if s[i] in "0123456789":
                current_number  = current_number * 10  + int(s[i])
            if s[i] in "+-*/" or i == len(s)-1 :
                if current_operation == '+':
                    stack.append(current_number)
                elif current_operation == "-":
                    stack.append(-current_number)
                elif current_operation == "*":
                    stack.append(stack.pop() * current_number)
                else:
                    stack.append(int(stack.pop() / current_number))
                current_number = 0
                current_operation = s[i]
        
        return sum(stack)
                