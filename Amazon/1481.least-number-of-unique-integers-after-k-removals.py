#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == len(arr):
            return 0
        dic = {}
        nums = [None for _ in range(len(arr))]
        index = 0
        for n in arr:
            nums[index] = n
            index += 1
            dic[n] = dic.get(n, 0) + 1
        if k == 0:
            return len(dic)
        nums.sort()
        res = []
        for i in range(k, len(nums)):
            res.append(nums[i])
        res = set(res)
        return len(res)
# @lc code=end
