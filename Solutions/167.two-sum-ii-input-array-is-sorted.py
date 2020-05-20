#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tmp:
                    return (i+1, mid+1)
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
# @lc code=end
