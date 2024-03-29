#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(num)
        heapq.heapify(heap)
        for i in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
# @lc code=end
