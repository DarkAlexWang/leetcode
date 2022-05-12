#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        nums = []
        for letter in letters:
            nums.append(ord(letter))

        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > ord(target):
                r = mid - 1
            else:
                l = mid + 1
        return letters[l]
# @lc code=end
