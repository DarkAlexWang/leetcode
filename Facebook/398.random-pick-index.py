#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
