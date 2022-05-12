#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x <= arr[mid]:
                right = mid
            elif x >= arr[mid + k]:
                left = mid + 1
            elif x - arr[mid] > arr[mid + k]  - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
# @lc code=end
