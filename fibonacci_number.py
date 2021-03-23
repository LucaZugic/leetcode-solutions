# Given the definition F(n) = F(n - 1) + F(n - 2), fib() returns F(n)
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=30)
    def compute(self, n):
        if n <= 1:
            return n
        return self.compute(n-1) + self.compute(n-2)
    def fib(self, n: int) -> int:
        for i in range(n+1):
            answer = (self.compute(i))
        return answer
    
