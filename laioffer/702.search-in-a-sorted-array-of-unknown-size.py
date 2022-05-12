#
# @lc app=leetcode id=702 lang=python3
#
# [702] Search in a Sorted Array of Unknown Size
#

# @lc code=start
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo = 0
        hi = 1
        while reader.get(hi) < target:
            lo = hi
            hi *= 2
        while lo <= hi:
            mid = (lo + hi) // 2
            if reader.get(mid) < target:
                lo = mid + 1
            elif reader.get(mid) > target:
                hi = mid - 1
            else:
                return mid
        return -1

# @lc code=end
