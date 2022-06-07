#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = set()
        slow, fast, longest = 0, 0, 0
        array = list(s)
        while fast < len(array):
            if array[fast] in distinct:
                distinct.remove(array[slow])
                slow += 1
            else:
                distinct.add(array[fast])
                fast += 1
                longest = max(longest, fast - slow)
        return longest

# @lc code=end
