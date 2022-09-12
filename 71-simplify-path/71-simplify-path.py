class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        x = path.split("/")

        for i in range(len(x)):
            if x[i] == "." or x[i] == "":
                continue
            if x[i] == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(x[i])
            
        return("/"+"/".join(stack))