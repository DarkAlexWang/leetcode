#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res = 0, 0
        dic = {}
        for end, ch in enumerate(s):
            if ch in dic and start <= dic[ch]:
                start = dic[ch] + 1
            else:
                res = max(res, end - start + 1)
            dic[ch] = end
        return res
# @lc code=end
