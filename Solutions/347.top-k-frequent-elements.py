#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] +1
            else:
                dic[i] = 1

        arr = sorted(dic, key = dic.get, reverse = True)
        return arr[:k]
# @lc code=end
