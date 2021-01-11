#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        chars = set()
        for end in range(len(s)):
            if s[end] not in chars:
                chars.add(s[end])
                res = max(res, end - start + 1)
            else:
                chars.remove(s[end])
                start += 1
        return res
# @lc code=end
