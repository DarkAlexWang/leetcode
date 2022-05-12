#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
from functools import lru_cache
class Solution:
    @lru_cashe(maxsize=1000)
    def fib(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 1
        return self.fib(N-1) + sefl.fib(N- 2)

    def fib(self, N):
        if N <= 1:
            return N
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[N]
# @lc code=end
