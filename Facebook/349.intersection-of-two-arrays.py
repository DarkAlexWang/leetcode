#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for num in nums1:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        print(dic)
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] = 0
        return res
# @lc code=end
#
