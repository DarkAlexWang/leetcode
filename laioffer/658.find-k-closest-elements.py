#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 0 or not arr:
            return arr
        if k <= 0:
            return [0]
        left = self.largestsmallerequal(arr, x)
        right = left + 1
        result = [0] * k
        for i in range(k):
            if right >= len(arr) or left >= 0 and x - arr[left] <= arr[right] - x:
                result[i] = arr[left]
                left -= 1
            else:
                result[i] = arr[right]
                right += 1

        return sorted(result)

    def largestsmallerequal(self, arr, x):
        left = 0
        right = len(arr) - 1
        while left < right -1:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        if arr[left] <= x:
            return left
        elif arr[right] <= x:
            return right
        else:
            return -1


# @lc code=end
