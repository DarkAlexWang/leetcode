#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):
            self.w[i] = self.w[i - 1] + self.w[i]


    def pickIndex(self) -> int:
        x = random.randint(1, self.w[-1])
        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if self.w[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
