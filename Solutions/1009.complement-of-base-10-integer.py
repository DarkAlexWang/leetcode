#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        X = 1
        while N > X:
            X = X *2 + 1
        return X - N
# @lc code=end
