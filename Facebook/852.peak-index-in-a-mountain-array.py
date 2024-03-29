#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1] and  arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] > arr[mid + 1]:
                r = mid + 1
            else:
                l = mid
        return l

# @lc code=end
