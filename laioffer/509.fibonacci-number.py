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
# @lc code=end
