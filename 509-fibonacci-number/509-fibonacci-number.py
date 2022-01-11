class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        fib1 = 0
        fib2 = 1
        fib = 0
        i = 2
        while i<=n:
            fib = fib1+fib2
            fib1 = fib2
            fib2 = fib
            i+=1
        return fib
        
    