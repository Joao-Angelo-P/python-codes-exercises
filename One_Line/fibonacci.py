#509. Fibonacci Number
class Solution: fib=lambda self, n: n if n<2 else self.fib(n-1)+self.fib(n-2)
