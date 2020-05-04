#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        numJewels = 0
        charToFreqS = {}
        for ch in S:
            if ch not in charToFreqS:
                charToFreqS[ch] = 1
            else:
                charToFreqS[ch] += 1
        for ch in J:
            if ch in charToFreqS:
                numJewels += charToFreqS[ch]
        return numJewels
# @lc code=end
